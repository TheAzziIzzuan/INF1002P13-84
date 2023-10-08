import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read in CSV
df = pd.read_csv("datasets\ResaleAndRentalApplications.csv")

#assign values to variables
resale = df['resale'].tolist()
rental = df['rental'].tolist()
year = df['year'].tolist()
total = df['total'].tolist()

#generate resale bars
resaleBars = plt.barh(year,resale,label="Resale")
#generate rental bars
rentalBars = plt.barh(year,rental,label="Rental")
#label bars with values
plt.bar_label(resaleBars,labels=resale,label_type="center")
plt.bar_label(rentalBars,labels=rental,label_type="center")

#visible grid lines
plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='x', alpha=0.7)
plt.ylabel("Years")
plt.xlabel("Applications Registered")
plt.title("Resale vs. Rental Applications Registered")
plt.yticks(year)
plt.legend(loc="lower right")
plt.show()