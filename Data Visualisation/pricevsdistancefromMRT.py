import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#data are randomly selected, room size and unit type are the same, remaining years are simlar, just the distance to the mrt is different
df  = pd.read_csv("datasets\HDBandNearestMrtCoords.csv")
# df.plot(df['resale_price'], df['nearest_distance_to_mrt'])  # plots all columns against index
df.plot(kind='scatter',x='nearest_distance_to_mrt',y='resale_price') # scatter plot
plt.title('Price of 4-room HDBs in relation to distance from MRT (AMK area)')

#best fit line
# Perform linear regression to calculate the best-fit line
x = df['nearest_distance_to_mrt']
y = df['resale_price']
coefficients = np.polyfit(x, y, 1)  # Fit a first-degree (linear) polynomial

# Create the best-fit line using the coefficients
best_fit_line = np.poly1d(coefficients)

# Plot the best-fit line
plt.plot(x, best_fit_line(x), color='red', linestyle='-', label='Best Fit Line')

plt.show()
