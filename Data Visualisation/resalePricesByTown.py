import sys, csv
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

# #test reading of CSV file
# with open('datasets/Resale_Flat_Prices_Jan_2015_to_Dec_2016.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         print(row)

# Initialize the lists for X and Y 
data = pd.read_csv('datasets\Resale_Flat_Prices_Jan_2013_to_Sep_2023.csv') 
  
df = pd.DataFrame(data) 
  
X = list(df.iloc[:, 1]) 
Y = list(df.iloc[:, 9]) 

# Plot the data using bar() method 
plt.barh(X, Y, color='g') 
plt.title("Resale Price by Towns") 
plt.xlabel("Town") 
plt.ylabel("Resale Price") 
  
# Show the plot 
plt.show() 