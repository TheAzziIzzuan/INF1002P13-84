import matplotlib.pyplot as plt 
import pandas as pd 
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


def priceCovid():
    df = pd.read_csv('datasets\Resale_Flat_Prices_Jan_2013_to_Sep_2023.csv') 
    df.drop(columns= "block", inplace=True)
    df.drop(columns= "town", inplace=True)
    df.drop(columns= "street_name", inplace=True) 
    df.drop(columns= "storey_range", inplace=True)
    df.drop(columns= "floor_area_sqm", inplace=True)
    df.drop(columns= "flat_model", inplace=True)
    df.drop(columns= "flat_type", inplace=True)
    df.drop(columns= "lease_commence_date", inplace=True)

    df['Year'] = df['month'].str.extract(r'(\d{4})') #extract year from month
    df.drop(columns= "month", inplace=True)          #drop month column
    df['Year'] = df['Year'].astype(int)              #convert year to int

    df_filtered = df[~df['Year'].isin([2013, 2014, 2015, 2016, 2017, 2023])] #filter out 2013, 2014, 2015, 2016, 2017, 2023
    df_filtered = df_filtered.groupby('Year').mean() #group by year and get mean of resale price
    df_filtered.reset_index(inplace=True) #reset index
    return df_filtered['Year'], df_filtered['resale_price']
    

  
priceCovid()
