import tkinter as tk
from tkinter import ttk, LEFT, TOP, RIGHT, LabelFrame, Button
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
import priceCovid 
import numberofHDBs
from tkinter import simpledialog
from tkinter import messagebox
import os
import mplcursors
import customtkinter
import LoanCalculator
from LoanCalculator import loancalculate




df = None

def df_to_csv(data, filename_prefix):
    filename = f"{filename_prefix}.csv"
    df = pd.DataFrame(data)                                                                     # convert to dataframe
    df.to_csv(filename, index=False)                                                            # export to csv, index=false ensure that the index is not exported

#################################### TAB 1 ####################################

def welcomePage(tab1):
    welcomeFrame = ttk.Frame(tab1)
    welcomeFrame.pack(fill=tk.BOTH, expand=True)

    # Create a label with a welcome message
    label = tk.Label(welcomeFrame, text="Welcome to the analysis of HDBs!", font=("Arial", 30))
    label2 = tk.Label(welcomeFrame, text="Click on the different tabs to get some insights on the different stats compiled on HDB", font=("Arial", 20))
    label.pack(pady=50)  # Adjust the padding
    label2.pack(pady=30)





#################################### TAB 2 ####################################

def displayCovidGraph(tab2):
    global df
    x, y  = priceCovid.priceCovid()
    df = pd.DataFrame({'Year': x, 'Resale Price': y})                                           # convert to dataframe
    fig = plt.figure(figsize=(10, 6))                                                           # Adjust the figure size
    plt.xticks(range(2018, 2023))                                                               # set number of ticksplt.xticks(range(2018, 2023)) #set number of ticks
    plt.plot(x, y, marker='X', linestyle='-')
    plt.xlabel('Year')
    plt.ylabel('Resale Price [$]')
    plt.title('Resale Price Over the Years')
    plt.grid(True)                                                                              # Display grid
                                
    # Display the plot
    canvas = FigureCanvasTkAgg(fig, master=tab2)                                                # Embed the graph in a canvas
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)
    mplcursors.cursor(hover=True)                                                               # Enable mplcursors for hover-over functionality

    
        

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


#################################### TAB 3 ####################################

def displayHDB(tab3):
    x, y  = numberofHDBs.noHDBs()
    df = pd.DataFrame({'bldg_contract_town': x, 'total_dwelling_units': y})
    df.to_csv('hdb_data.csv', index=False)
    fig = plt.figure(figsize=(10, 6))
    plt.bar(x, y)
    plt.xlabel('bldg_contract_town')
    plt.ylabel('total_dwelling_units')
    plt.title('Amount of Units in Each Area in Singapore')
    plt.xticks(rotation='vertical')
    canvas = FigureCanvasTkAgg(fig, master=tab3)   
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True) 
    



window = tk.Tk() 
window.title("Resale Price Graph")

# create a style for the tabs
customed_style = ttk.Style()
customed_style.configure('Custom.TNotebook.Tab', padding=[12, 12], font=('Arial', 15))

# Create a notebook with tabs
notebook = ttk.Notebook(window, style='Custom.TNotebook') #widget that manages a collection of windows/displays
tab1 = ttk.Frame(notebook) 
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)
tab7 = ttk.Frame(notebook)
tab8 = ttk.Frame(notebook)
tab9 = ttk.Frame(notebook)
notebook.add(tab1, text="Welcome")
notebook.add(tab2, text="Resale Price before and after COVID-19")
notebook.add(tab3, text="Number of HDBs")   
notebook.add(tab4, text="Rental and Resale") 
notebook.add(tab5, text="Estimated Loan Calculator")
notebook.add(tab7, text="HDB Unit Types By Household Income")
notebook.add(tab8, text="Age Trends In HDB Owners")
notebook.add(tab9, text="BTO Sale Launch Analysis")
notebook.pack(expand=True, fill="both") #fill the entire space of the window

exportButton = tk.Button(tab2, text="Export!", command=exportfile)
exportButton.pack(side=tk.BOTTOM, pady=15)                                               # the side option specifices the sie of the parent widget to which the child widget should be packed



#################################### TAB 4 ####################################

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
        canvas = FigureCanvasTkAgg(fig, master=tab4)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill='both', expand=True)
    else:
        # Generate and display the selected plot
        fig = plot_function()
        canvas = FigureCanvasTkAgg(fig, master=tab4)
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

controls_frame = LabelFrame(tab4, text='List of Graphs', background='light grey', height=5)
RBFTbutton = Button(controls_frame, text = 'Renting out of Applications by Flat Type', padx=10, pady=5,command=lambda: update_canvas(RentalbyFlatType))
RBFTbutton.pack( side = LEFT)
RVRAbutton = Button(controls_frame, text = 'Resale vs Rental Applications Registered', padx=10, pady=5,command=lambda: update_canvas(ResaleAndRentalApplications))
RVRAbutton.pack( side = LEFT )
RPPBTbutton = Button(controls_frame, text = 'Resale Price Progression by Towns', padx=10, pady=5,command=lambda: update_canvas(ResalePriceProgression))
RPPBTbutton.pack( side = LEFT )
exportbutton = Button(controls_frame, text = 'Export CSV', padx=10, pady=5,command=export_file)
exportbutton.pack( side = RIGHT )
controls_frame.pack(fill='both', expand='0', side=TOP, padx=20, pady=10)
#################################### END OF TAB 4 ####################################

#################################### TAB 5 ###########################################
def display_loan(tab5):

    frame = ttk.Frame(tab5)
    frame.pack(fill="both", expand=True)
    message = "Estimated HDB Loan Calculator"
    label = customtkinter.CTkLabel(frame, text=message, font=("Arial", 25))
    label.pack(anchor="center")

    income = ttk.Label(frame, text="Income:")
    income.pack()

    incomeinput = ttk.Entry(frame)
    incomeinput.pack()

    years = ttk.Label(frame, text="Loan Duration:")
    years.pack()

    yearsvariable = tk.StringVar()
    yearsselect = ttk.Combobox(frame, textvariable=yearsvariable, values=["15 years", "20 years", "25 years"], state="readonly")
    yearsselect.pack()

    calculate = customtkinter.CTkButton(frame, text="Calculate", command=lambda:loancalculate(incomeinput, yearsvariable,loanresult))
    calculate.place(relx=0.5, rely=0.90, anchor=customtkinter.CENTER)

    loanresult = ttk.Label(frame, text="Loan Amount: ")
    loanresult.pack()
    
#################################### END OF TAB 5 ###########################################
#################################### TAB 6 ###########################################

#################################### END OF TAB 6 ###########################################

#################################### TAB 7 ############################################

def displayHDBTypesByIncome(tab7):
    # read the data from csv file
    data = pd.read_csv("datasets\HDBUnitTypeByIncome.csv")
    hdbtypes = data['HDBUnits']
    income = data['HouseholdIncome']

    fig = plt.figure(figsize=(10, 6))

    # plot the bars
    plt.bar(hdbtypes,income)

    # name the title for the graph
    plt.title("HDB Units By Household Income")

    # set the x and y labels
    plt.xlabel('HDB Unit Types')
    plt.ylabel('Average Monthly Household Income')

    canvas = FigureCanvasTkAgg(fig, master=tab7)   
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

#################################### END OF TAB 7 ############################################

#################################### Tab 8 ################################################

def displayAgeOfHDBOwners(tab8):
    # fit the graph in the figure
    plt.rcParams['figure.figsize'] = [7.00, 3.50]
    plt.rcParams['figure.autolayout'] = True

    # read the data from csv file
    data = pd.read_csv("datasets\AgeTrendInHDBOwnership.csv")

    fig = plt.figure(figsize=(10, 6))

    line1 = data['Below 35']
    line2 = data['35 - 49']
    line3 = data['50 - 64']
    line4 = data['65 and above']
    year = data['Year']

    # plot the line graphs
    plt.plot(year, line1, label='Age Below 35')
    plt.plot(year, line2, label='Age 35 - 49')
    plt.plot(year, line3, label='Age 50 - 64')
    plt.plot(year, line4, label='Age 65 and above')
    plt.grid(True)

    # set the x and y labels
    plt.xlabel('Year')
    plt.ylabel('Household Reference Person')
    plt.xticks(year)

    # name the title for the graph
    plt.title("Age Trends in HDB Owners")

    # show legend at top right corner
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)

    canvas = FigureCanvasTkAgg(fig, master=tab8)   
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

#################################### END OF TAB 8 ############################################
#################################### TAB 9 ############################################
def displayBTOSaleLaunchAnalysis(tab9):
#################################### END OF TAB 9 ############################################

welcomePage(tab1)
displayCovidGraph(tab2) 
displayHDB(tab3)
display_loan(tab5)
displayHDBTypesByIncome(tab7)
displayAgeOfHDBOwners(tab8)
displayBTOSaleLaunchAnalysis(tab9)

window.mainloop()
