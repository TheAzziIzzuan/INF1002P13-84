import tkinter as tk
from tkinter import ttk, LEFT, TOP, RIGHT, LabelFrame, Button
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure
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
from PIL import Image, ImageTk

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

tab4 = ttk.Frame(notebook) #adding my tab
notebook.add(tab4, text="HDBs in Singapore")

# Define a function to display HDB information in a canvas
def displayHDBinSingapore(tab4):
    canvas = tk.Canvas(tab4,width=400, height=400)
    canvas.pack(fill=tk.BOTH, expand=True)

    #Displaying the Map
    image = Image.open("Data Visualisation\HDBinSG.png")
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(canvas, image=photo)
    image_label.photo = photo  #reference to avoid garbage collection
    image_label.pack(pady=25)
    
    #Details related to the Image Label
    explanation_text = """
    This is the overall view of the HDBs in Singapore.
    """
    explanation_label = tk.Label(canvas, text=explanation_text, justify='center', font=("Helvetica", 16))
    canvas.create_window(250, 470, anchor=tk.W, window=explanation_label)

    def open_link(event): #function for the hyperlink
        webbrowser.open("Data Visualisation\scatter_map.html")

    text_before_link = "To view a clearer version, click "
    hyperlink_text = "HERE"
    text_after_link = "to view the interactive map!"
    hyperlink_label = tk.Label(canvas, text=text_before_link, cursor="hand2", font=("Helvetica", 12))
    canvas.create_window(270, 510, anchor=tk.W, window=hyperlink_label) #For the sentence before hyperlink
    hyperlink_label.bind("<Button-1>", open_link)

    hyperlink_label = tk.Label(canvas, text=hyperlink_text, cursor="hand2", fg="blue", font=("Helvetica", 12))
    canvas.create_window(490, 510, anchor=tk.W, window=hyperlink_label) #hyperlink part
    hyperlink_label.bind("<Button-1>", open_link)

    text_label = tk.Label(canvas, text=text_after_link, font=("Helvetica", 12))
    canvas.create_window(540, 510, anchor=tk.W, window=text_label)

#################################### END OF TAB 4 ####################################

#################################### START OF TAB 5 ####################################

tab5 = ttk.Frame(notebook) #adding my tab
notebook.add(tab5, text="How Distance To Amenities Affect Resale Prices")

def dislayPriceandAmenities(tab5):

    # Create a frame to contain both figures
    figures_frame = ttk.Frame(tab5)
    figures_frame.grid(row=0, column=0, padx=10, pady=10)

    #frame for Graph 1 (SCHOOL)
    frame1 = ttk.Frame(figures_frame)
    frame1.grid(row=0, column=0, padx=10, pady=10)

    # School and Resale Price Graph 1
    df = pd.read_csv("datasets\schoolandprice(cleaned).csv")

    figure1 = Figure(figsize=(7, 5), dpi=87)  # Adjust the figure size
    subplot1 = figure1.add_subplot(111) 

    x = df['Distance From Nearest School']
    y = df['Resale Price']
    coefficients = np.polyfit(x, y, 1)
    best_fit_line = np.poly1d(coefficients)

    subplot1.scatter(x, y)
    subplot1.plot(x, best_fit_line(x), color='red', linestyle='-', label='Best Fit Line')

    #Graph Title and Labels
    subplot1.set_title('Price of HDB Based on Distance from Nearest School')
    subplot1.set_xlabel('Distance From Nearest School')
    subplot1.set_ylabel('Resale Price')  

    # Add canvas1
    canvas1 = FigureCanvasTkAgg(figure1, master=frame1)
    canvas1.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, sticky="N")

    # Explanation of Canvas1
    explanation1 = tk.Label(frame1, text="Based on the results above, we can see that HDBs that are approximately less than \n0.4km or more than 1.3km from schools are less desirable. Those closer to schools \nmay be disturbed by the noise and those further away are inconvenienced \ndue to the distance or travel time.\n\n.", font=("Helvetica", 12))

    # Adjusting location of graph and description
    explanation1.grid(row=2, column=0, padx=10, pady=10, sticky="N")

    # Create frame for Graph 2 (MRT)
    frame2 = ttk.Frame(figures_frame)
    frame2.grid(row=0, column=1, padx=10, pady=10)

    # MRT and Resale Price Graph 2
    figure2 = Figure(figsize=(7, 5), dpi=87)  #Figure Size
    subplot2 = figure2.add_subplot(111)

    data2 = pd.read_csv("datasets\HDBandNearestMrtCoords.csv")
    x2 = data2['nearest_distance_to_mrt']
    y2 = data2['resale_price']

    # Create a figure and add subplots
    coefficients = np.polyfit(x2, y2, 1)
    best_fit_line = np.poly1d(coefficients)

    subplot2.scatter(x2, y2)
    subplot2.plot(x2, best_fit_line(x2), color='red', linestyle='-', label='Best Fit Line')

    subplot2.set_title('Price of HDBs based on distance from MRT (AMK area)')
    subplot2.set_xlabel('Distance From Nearest MRT Station')
    subplot2.set_ylabel('Resale Price') 

    canvas2 = FigureCanvasTkAgg(figure2, master=frame2)
    canvas2.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, sticky="N")

    # Explanation of Canvas2
    explanation2 = tk.Label(frame2, text="The graph above focuses on HDBs near Ang Mo Kio (AMK) MRT station which \noperates above the ground. We can see that the resale price for those in 0.2km \nproximity to the station is noticeably lower. This may be due to the noise which \ncomes from the MRT whenever it passes by. As the MRT operates until 12am,\n this can cause a disturbance to families. However, we can also see that the \nresale price of HDBs that are further away from the station is lower compared \nto the rest as it is due to the lack of convenience. ", font=("Helvetica", 12))
    explanation2.grid(row=1, column=0, padx=10, pady=10, sticky="N")
    
#################################### END OF TAB 5 ####################################

displayCovidGraph(tab1) 
displayHDB(tab2)
displayHDBinSingapore(tab4)
dislayPriceandAmenities(tab5)

window.mainloop()