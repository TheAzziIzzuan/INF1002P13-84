import pandas as pd
import matplotlib.pyplot as plt


#pivot table the big data set to show amount of units in each area
df = pd.read_csv("project.py\HDBPropertyInformation.csv")
pivot = df.pivot_table(index =['bldg_contract_town'],  
                       values =['total_dwelling_units'], aggfunc ='sum') 

#plot data frame 
df = pd.read_csv("project.py\SumDwellingUnit(2013-2023).csv")
bargraph = df.plot.bar(x='Row Labels')
# df.head() #file structure

plt.show()
