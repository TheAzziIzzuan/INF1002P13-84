import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import priceCovidTest 
import numberofHDBsTest
from tkinter import simpledialog
from tkinter import messagebox

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
notebook.add(tab1, text="Resale Price before and after COVID-19")
notebook.add(tab2, text="Other Tab")  
notebook.pack(expand=True, fill="both") #fill the entire space of the window

exportButton = tk.Button(tab1, text="Export!", command=exportfile)
exportButton.pack(side=tk.BOTTOM, pady=15)                                               # the side option specifices the sie of the parent widget to which the child widget should be packed

button2 = tk.Button(tab2, text="Click Me!", command=displayHDB)
button2.pack()

displayCovidGraph(tab1) 
displayHDB(tab2)

window.mainloop()