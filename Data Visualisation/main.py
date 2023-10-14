import tkinter as tk
from tkinter import ttk, LEFT, TOP, RIGHT, LabelFrame, Button
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
import priceCovidTest 
import numberofHDBsTest
from tkinter import simpledialog
from tkinter import messagebox
import os
import webbrowser
from tkinter import PhotoImage

df = None

def df_to_csv(data, filename_prefix):
    filename = f"{filename_prefix}.csv"
    df = pd.DataFrame(data)                                                                     # convert to dataframe
    df.to_csv(filename, index=False)                                                            # export to csv, index=false ensure that the index is not exported

def displayCovidGraph(tab1):
    global df
    x, y  = priceCovidTest.priceCovidTest()
    df = pd.DataFrame({'Year': x, 'Resale Price': y})                                           # convert to dataframe
    fig = plt.figure(figsize=(10, 6))                                                           # Adjust the figure size
    plt.xticks(range(2018, 2023))                                                               # set number of ticksplt.xticks(range(2018, 2023)) #set number of ticks
    plt.plot(x, y, marker='X', linestyle='-')
    plt.xlabel('Year')
    plt.ylabel('Resale Price [$]')
    plt.title('Resale Price Over the Years')
    plt.grid(True)                                                                              # Display grid
                                
    # Display the plot
    canvas = FigureCanvasTkAgg(fig, master=tab1)                                                # Embed the graph in a canvas
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

def exportfile():
    while True:                                                                                 # loop until user enters a filename or no data to export
        if df is not None:                                                                      # if df is not empty
            filename_prefix = simpledialog.askstring("Filename", "Filename:")
            if filename_prefix:                                                                 # if user enters a filename
                df_to_csv(df, filename_prefix)
                messagebox.showinfo("Export Successful", f"Data exported to CSV file: {filename_prefix}")
                break
            else:
                messagebox.showinfo("Export Unsuccessful!", "No filename entered!")
        else:
            messagebox.showinfo("Export Unsuccessful!", "No data to export!")
            break

def displayHDB(tab2):
    x, y  = numberofHDBsTest.noHDBs()
    df = pd.DataFrame({'bldg_contract_town': x, 'total_dwelling_units': y})
    df.to_csv('hdb_data.csv', index=False)
    fig = plt.figure(figsize=(10, 6))
    plt.bar(x, y)
    plt.xlabel('bldg_contract_town')
    plt.ylabel('total_dwelling_units')
    plt.title('Amount of Units in Each Area in Singapore')
    plt.xticks(rotation='vertical')
    canvas = FigureCanvasTkAgg(fig, master=tab2)   
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True) 
    



window = tk.Tk() 
window.title("Resale Price Graph")

# Create a notebook with tabs
notebook = ttk.Notebook(window) #widget that manages a collection of windows/displays
tab1 = ttk.Frame(notebook) 
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
notebook.add(tab1, text="Resale Price before and after COVID-19")
notebook.add(tab2, text="Other Tab")
notebook.add(tab3, text="Rental and Resale")   
notebook.pack(expand=True, fill="both") #fill the entire space of the window

exportButton = tk.Button(tab1, text="Export!", command=exportfile)
exportButton.pack(side=tk.BOTTOM, pady=15)                                               # the side option specifices the sie of the parent widget to which the child widget should be packed

button2 = tk.Button(tab2, text="Click Me!", command=displayHDB)
button2.pack()

#################################### TAB 3 ####################################

def RentalbyFlatType():
    global df2
    #read in CSV
    df2 = pd.read_csv("datasets\RentalByFlatType.csv")
    #plots figure with 3 rows and 4 columns with figure size of 15x15
    fig, axes = plt.subplots(3, 4, figsize=(15, 15))

    #generates each pie chart
    for i, (idx, row) in enumerate(df2.set_index('year').iterrows()):
        ax = axes[i // 4, i % 4]
        row = row[row.gt(row.sum() * .01)]
        ax.pie(row, autopct='%2.1f%%', labels=row.index, textprops={'fontsize': 8}, startangle=30)
        ax.set_title(idx)

    fig.subplots_adjust(wspace=.2)
    fig.delaxes(axes[2,3])
    plt.suptitle("Number of Approved Renting Out Applications by Flat Type")
    return fig

def ResaleAndRentalApplications():
    global df2
    #read in CSV
    df2 = pd.read_csv("datasets\ResaleAndRentalApplications.csv")

    #assign values to variables
    resale = df2['resale'].tolist()
    rental = df2['rental'].tolist()
    year = df2['year'].tolist()

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

def ResalePriceProgression():
    global df2
    #read in CSV
    df2 = pd.read_csv("datasets\Resale_Flat_Prices_Jan_2013_to_Sep_2023.csv")

    #drop unwanted columns
    df2 = df2.drop('flat_type', axis=1)
    df2 = df2.drop('block', axis=1)
    df2 = df2.drop('street_name', axis=1)
    df2 = df2.drop('storey_range', axis=1)
    df2 = df2.drop('floor_area_sqm', axis=1)
    df2 = df2.drop('flat_model', axis=1)
    df2 = df2.drop('lease_commence_date', axis=1)

    #converts month to quarter
    df2['month'] = pd.PeriodIndex(df2.month, freq='Q')
    df2.set_index('month', inplace=True)
    df2 = df2.groupby(['month','town'])['resale_price'].mean()
    df2 = df2.unstack(level='town')
    df2.columns.name = 'Resale Price'

    ax = df2.plot()
    ax.set_xlabel("Years by Quarter")
    ax.set_ylabel("Resale Price ($)")
    ax.set_ylim([300000, 1000000])
    values = np.arange(300000, 1000000, 50000)
    plt.yticks(values)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='x', alpha=0.7,which='both')
    plt.title("Average Resale Price Progression of Towns from 2013 to 2023")
    plt.legend(bbox_to_anchor=(1.05, 1.05), loc='upper left')
    plt.tight_layout()
    fig = plt.gcf()
    return fig

df2 = None
canvas = None

def update_canvas(plot_function):
    global canvas
    if canvas is not None:
        canvas.get_tk_widget().destroy()
        canvas = None
        fig = plot_function()
        canvas = FigureCanvasTkAgg(fig, master=tab3)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill='both', expand=True)
    else:
        # Generate and display the selected plot
        fig = plot_function()
        canvas = FigureCanvasTkAgg(fig, master=tab3)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill='both', expand=True)

def DFtoCSV(data):
    df2 = pd.DataFrame(data)                                                                     
    downloads_folder = os.path.expanduser('~/Downloads')
    csv_file_path = os.path.join(downloads_folder, 'canvas_data.csv')
    df2.to_csv(csv_file_path, index=False)    

def export_file():
    while True:                                                                                
        if df2 is not None:                                                                     
            DFtoCSV(df2)
            messagebox.showinfo("Export Successful", f"Data exported to CSV file: 'canvas_data.csv'")
            break
        else:
            messagebox.showinfo("Export Unsuccessful!", "No data to export!")
            break

controls_frame = LabelFrame(tab3, text='List of Graphs', background='light grey', height=5)
RBFTbutton = Button(controls_frame, text = 'Renting out of Applications by Flat Type', padx=10, pady=5,command=lambda: update_canvas(RentalbyFlatType))
RBFTbutton.pack( side = LEFT)
RVRAbutton = Button(controls_frame, text = 'Resale vs Rental Applications Registered', padx=10, pady=5,command=lambda: update_canvas(ResaleAndRentalApplications))
RVRAbutton.pack( side = LEFT )
RPPBTbutton = Button(controls_frame, text = 'Resale Price Progression by Towns', padx=10, pady=5,command=lambda: update_canvas(ResalePriceProgression))
RPPBTbutton.pack( side = LEFT )
exportbutton = Button(controls_frame, text = 'Export CSV', padx=10, pady=5,command=export_file)
exportbutton.pack( side = RIGHT )
controls_frame.pack(fill='both', expand='0', side=TOP, padx=20, pady=10)
#################################### END OF TAB 3 ####################################

#################################### START OF TAB 4 ####################################
# Define a function to display HDB information in a canvas
def displayHDBinSingapore(tab4):
    canvas = tk.Canvas(tab4,width=400, height=400)
    canvas.pack(fill=tk.BOTH, expand=True)

    image = PhotoImage(file="Data Visualisation\HDBinSG.png")
    image_label = tk.Label(canvas, image=image)
    canvas.create_window(10, 10, anchor=tk.NW, window=image_label)
    image_label.pack()

    explanation_text = """
    This is the overall view of the HDBs in Singapore.
    """
    explanation_label = tk.Label(canvas, text=explanation_text, justify='center')
    canvas.create_window(10, 200, anchor=tk.W, window=explanation_label)

    def open_link(event):
        webbrowser.open("Data Visualisation\scatter_map.html")

    text_before_link = "To see a clearer version, click "
    hyperlink_text = "HERE"
    text_after_link = "to view the interactive map!"
    hyperlink_label = tk.Label(canvas, text=text_before_link, cursor="hand2")
    canvas.create_window(10, 300, anchor=tk.W, window=hyperlink_label)
    hyperlink_label.bind("<Button-1>", open_link)

    hyperlink_label = tk.Label(canvas, text=hyperlink_text, cursor="hand2", fg="blue")
    canvas.create_window(10, 330, anchor=tk.W, window=hyperlink_label)
    hyperlink_label.bind("<Button-1>", open_link)

    text_label = tk.Label(canvas, text=text_after_link)
    canvas.create_window(10, 360, anchor=tk.W, window=text_label)

# Create a Tkinter window
window.title("Resale Price Graph")

tab4 = ttk.Frame(notebook) #adding my tab

# Add tabs to the notebook
notebook.add(tab4, text="HDBs in Singapore")



displayCovidGraph(tab1) 
displayHDB(tab2)
displayHDBinSingapore(tab4)

window.mainloop()