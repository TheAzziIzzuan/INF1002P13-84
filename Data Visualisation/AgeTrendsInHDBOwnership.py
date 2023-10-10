import pandas as pd
import matplotlib.pyplot as plt

# fit the graph in the figure
plt.rcParams['figure.figsize'] = [7.00, 3.50]
plt.rcParams['figure.autolayout'] = True

# read the data from csv file
data = pd.read_csv("datasets\AgeTrendInHDBOwnership.csv")

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

# set the x and y labels
plt.xlabel('Year')
plt.ylabel('Household Reference Person')
plt.xticks(year)

# show legend at top right corner
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)

plt.show()
























