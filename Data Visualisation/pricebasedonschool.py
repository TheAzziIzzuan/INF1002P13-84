import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#data are randomly selected, room size and unit type are the same, remaining years are simlar, just the distance to nearest school
df  = pd.read_csv("datasets\schoolandprice(cleaned).csv")
# df.plot(df['resale_price'], df['nearest_distance_to_mrt'])
df.plot(kind='scatter',x='Distance From Nearest School',y='Resale Price') # scatter plot
plt.title('Price of 4-room HDBs in relation to distance from MRT (AMK area)')

#best fit line
# linear regression to calculate the best-fit line
x = df['Distance From Nearest School']
y = df['Resale Price']
coefficients = np.polyfit(x, y, 1)  # Fit a first-degree (linear) polynomial

# Create the best-fit line using the coefficients
best_fit_line = np.poly1d(coefficients)

# Plot the best-fit line
plt.plot(x, best_fit_line(x), color='red', linestyle='-', label='Best Fit Line')

plt.show()
