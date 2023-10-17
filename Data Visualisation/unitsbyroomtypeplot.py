import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

df = pd.read_csv('datasets\BTOLaunchList2010to2023.csv')

def plot_units_by_roomtype_each_year(frame):
    # Combining the 'BTO Launch Month' and 'BTO Launch Year' columns into a single date column
    df['Launch Date'] = pd.to_datetime(df['BTO Launch Month'] + ' ' + df['BTO Launch Year'].astype(str), format='%B %Y')
    
    # Ensure 'No. of Units' is numeric
    df['No. of Units'] = pd.to_numeric(df['No. of Units'], errors='coerce')

    # Grouping by year and room type and then summing up units
    yearly_units_by_room = df.groupby([df['Launch Date'].dt.year, 'Room Type'])['No. of Units'].sum().unstack()

    fig, ax = plt.subplots(figsize=(16, 8))
    yearly_units_by_room.plot(kind='bar', stacked=True, ax=ax)

    ax.set_title("Total Number of BTO Units Launched Each Year by Room Type")
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Number of Units")
    ax.grid(axis='y')
    ax.legend(title='Room Type', loc='center left', bbox_to_anchor=(1, 0.5))

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=3, column=0, columnspan=3)
    
    # Create a StringVar to hold text
    text_var = tk.StringVar()

    # Here's where you set up a label or another widget to display your text.
    # The 'font' option is where you can specify the text size.
    info_label = tk.Label(frame, textvariable=text_var, font=("Helvetica", 20))  # for example, text size 16
    info_label.grid(row=4, column=0, columnspan=3)  # adjust grid parameters as needed


    # Getting the top 3 room types over all the years combined
    # Now, you can set or change the text with the set() method of your StringVar
    
    total_units_by_room = df.groupby('Room Type')['No. of Units'].sum()
    top_3_rooms = total_units_by_room.nlargest(3).index.tolist()
    
    # Displaying the top 3 room types
    text_var.set(f"The top 3 room types in terms of units launched are: {', '.join(top_3_rooms)}")


    return fig
