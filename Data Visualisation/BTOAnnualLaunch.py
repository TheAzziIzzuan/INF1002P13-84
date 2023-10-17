import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

def annual_bto_plot(parent_frame):
    df = pd.read_csv('datasets\BTOLaunchList2010to2023.csv')
    
    # Combining the 'BTO Launch Month' and 'BTO Launch Year' columns into a single date column
    df['Launch Date'] = pd.to_datetime(df['BTO Launch Month'] + ' ' + df['BTO Launch Year'].astype(str), format='%B %Y')

    # Count the number of unique launch dates for each year
    unique_launches_per_year = df[['Launch Date']].drop_duplicates()['Launch Date'].dt.year.value_counts().sort_index()

    # Create a figure and axis objects
    fig, ax = plt.subplots(figsize=(6,3))
    
    # Modify the plotting commands to use the ax object
    ax.bar(unique_launches_per_year.index, unique_launches_per_year.values)
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Launches')
    ax.set_title('Total Number of BTO Sale Launch Annually')
    
    # Adding data labels above each bar
    for year, launches in zip(unique_launches_per_year.index, unique_launches_per_year.values):
        plt.text(year, launches + 1, str(launches), ha='center', va='bottom')
    
    # Add a text message at the bottom of the plot with text size 20
    message = "The BTO Sale Launch is maintaining at around 4 launches per year."
    ax.text(0.5, -0.1, message, transform=ax.transAxes, fontsize=20, ha='center')
    
    
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    canvas = FigureCanvasTkAgg(plt.gcf(), master=parent_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)
    plt.close()
    
    return fig
