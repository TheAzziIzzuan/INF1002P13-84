import sys, csv
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

# Initialize the lists for X and Y 
data = pd.read_csv('datasets\Resale_Flat_Prices_Jan_2013_to_Sep_2023.csv') 
  
df = pd.DataFrame(data) 
  
X = list(df.iloc[:, 1]) 
Y = list(df.iloc[:, 9]) 

# Plot the data using bar() method 
plt.barh(X, Y, color='g') 
plt.title("Resale Price by Towns") 
plt.xlabel("Resale Price") 
plt.ylabel("Towns") 
  
# Show the plot 
plt.show() 