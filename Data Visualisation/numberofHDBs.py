import pandas as pd
import matplotlib.pyplot as plt

#plot data frame 
df = pd.read_csv("project.py\SumDwellingUnit(2013-2023).csv")
bargraph = df.plot.bar(x='Row Labels')
# df.head() #file structure

plt.show()