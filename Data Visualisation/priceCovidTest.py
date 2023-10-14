









# import matplotlib.pyplot as plt 
# import pandas as pd 


# df = pd.read_csv('datasets\Resale_Flat_Prices_Jan_2013_to_Sep_2023.csv') 
# df.drop(columns= "block", inplace=True)
# df.drop(columns= "town", inplace=True)
# df.drop(columns= "street_name", inplace=True) 
# df.drop(columns= "storey_range", inplace=True)
# df.drop(columns= "floor_area_sqm", inplace=True)
# df.drop(columns= "flat_model", inplace=True)
# df.drop(columns= "flat_type", inplace=True)
# df.drop(columns= "lease_commence_date", inplace=True)

# df['Year'] = df['month'].str.extract(r'(\d{4})') #extract year from month
# df.drop(columns= "month", inplace=True)          #drop month column
# df['Year'] = df['Year'].astype(int)              #convert year to int

# df_filtered = df[~df['Year'].isin([2013, 2014, 2015, 2016, 2017, 2023])] #filter out 2013, 2014, 2015, 2016, 2017, 2023
# df_filtered = df_filtered.groupby('Year').mean() #group by year and get mean of resale price
# df_filtered.reset_index(inplace=True) #reset index

# plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

# plt.xticks(range(2018, 2023)) #set number of ticks
# plt.plot(df_filtered['Year'], df_filtered['resale_price'], marker='X', linestyle='-') 

# # Adding labels and title
# plt.xlabel('Year')
# plt.ylabel('Resale Price[$]')
# plt.title('Resale Price Over the Years')

# # Display the plot
# plt.grid(True)

# plt.tight_layout()
# plt.show()