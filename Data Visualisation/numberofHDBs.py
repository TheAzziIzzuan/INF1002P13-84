import pandas as pd
import matplotlib.pyplot as plt


#pivot table the big data set to show amount of units in each area
df = pd.read_csv("project.py\HDBPropertyInformation.csv")
pivot = df.pivot_table(index =['bldg_contract_town'],  
                       values =['total_dwelling_units'], aggfunc ='sum') 

#plot data frame 

plt.bar(df['bldg_contract_town'], df['total_dwelling_units'])
plt.xlabel('bldg_contract_town')
plt.ylabel('total_dwelling_units')
plt.title('Amount of Units in Each Area in Singapore')
plt.xticks(rotation='vertical')
plt.show()
