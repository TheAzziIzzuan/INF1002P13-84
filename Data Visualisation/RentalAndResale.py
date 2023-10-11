import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

########################### FUNCTIONS TO GENERATE GRAPHS ##################################

def RentalbyFlatType():
    #read in CSV
    df = pd.read_csv("datasets\RentalByFlatType.csv")
    #plots figure with 3 rows and 4 columns with figure size of 15x15
    fig, axes = plt.subplots(3, 4, figsize=(15, 15))

    #generates each pie chart
    for i, (idx, row) in enumerate(df.set_index('year').iterrows()):
        ax = axes[i // 4, i % 4]
        row = row[row.gt(row.sum() * .01)]
        ax.pie(row, autopct='%2.1f%%', labels=row.index, textprops={'fontsize': 8}, startangle=30)
        ax.set_title(idx)

    fig.subplots_adjust(wspace=.2)
    fig.delaxes(axes[2,3])
    plt.suptitle("Number of Approved Renting Out Applications by Flat Type")
    return fig

def ResaleAndRentalApplications():
    #read in CSV
    df = pd.read_csv("datasets\ResaleAndRentalApplications.csv")

    #assign values to variables
    resale = df['resale'].tolist()
    rental = df['rental'].tolist()
    year = df['year'].tolist()

    fig, ax = plt.subplots()
    resaleBars = ax.barh(year, resale,label="Resale")
    rentalBars = ax.barh(year, rental,label="Rental")
    plt.bar_label(resaleBars,labels=resale,label_type="center")
    plt.bar_label(rentalBars,labels=rental,label_type="center")

    #visible grid lines
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='x', alpha=0.7)
    plt.ylabel("Years")
    plt.xlabel("Applications Registered")
    plt.title("Applications Registered For Resale and Rental Flats")
    plt.yticks(year)
    plt.legend(loc="lower right")
    
    return fig

############################ TKINTER WINDOW SECTION ###############################################

#Initialize window
root = tk.Tk()
#Set size of window
root.geometry("640x480")
#Title of window
root.title("Rental and Resale")
frame = Frame(root)

canvas = None

def update_canvas(plot_function):
    global canvas
    if canvas is not None:
        canvas.get_tk_widget().destroy()
        canvas = None
        fig = plot_function()
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill='both', expand=True)
    else:
        # Generate and display the selected plot
        fig = plot_function()
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill='both', expand=True)

#Upper frame showing buttons
controls_frame = LabelFrame(root, text='List of Graphs', background='light grey', height=5)
controls_frame.pack(fill='both', expand='0', side=TOP, padx=20, pady=10)
RBFTbutton = Button(controls_frame, text = 'Renting out of Applications by Flat Type', command=lambda: update_canvas(RentalbyFlatType))
RBFTbutton.pack( side = LEFT)
RVRAbutton = Button(controls_frame, text = 'Resale vs Rental Applications Registered', command=lambda: update_canvas(ResaleAndRentalApplications))
RVRAbutton.pack( side = RIGHT )

frame.pack(fill='both', expand=True)

root.mainloop()