import pandas as pd
import matplotlib.pyplot as plt

# fit the graph in the figure
plt.rcParams['figure.figsize'] = [7.00, 3.50]
plt.rcParams['figure.autolayout'] = True

# read the data from csv file
data = pd.read_csv("datasets\HDBUnitTypeByIncome.csv")
x = data['HDBUnits']
y = data['HouseholdIncome']

# plot the bars
plt.bar(x,y)

# name the title for the graph
plt.title("HDB Units By Household Income")

# set the x and y labels
plt.xlabel('HDB Unit Types')
plt.ylabel('Average Monthly Household Income')

plt.show()