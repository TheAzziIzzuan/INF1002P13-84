import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

def annual_bto_plot(parent_frame):
    df = pd.read_csv('datasets\BTOLaunchList2010to2023.csv')
    
    # Combining the 'BTO Launch Month' and 'BTO Launch Year' columns into a single date column
    df['Launch Date'] = pd.to_datetime(df['BTO Launch Month'] + ' ' + df['BTO Launch Year'].astype(str), format='%B %Y')

    # Count the number of unique launch dates for each year
    unique_launches_per_year = df[['Launch Date']].drop_duplicates()['Launch Date'].dt.year.value_counts().sort_index()

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.bar(unique_launches_per_year.index, unique_launches_per_year.values)
    plt.xlabel('Year')
    plt.ylabel('Number of Launches')
    plt.title('Total Number of BTO Sale Launch Annually')
    # Adding data labels above each bar
    for year, launches in zip(unique_launches_per_year.index, unique_launches_per_year.values):
        plt.text(year, launches + 1, str(launches), ha='center', va='bottom')

    
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    canvas = FigureCanvasTkAgg(plt.gcf(), master=parent_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)
    plt.close()
