import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from tkinter import messagebox

df2 = None

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

def rentalbyflattype():
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

def resalerentalapplications():
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

def resalepriceprogression():
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
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
    fig = plt.gcf()
    return fig