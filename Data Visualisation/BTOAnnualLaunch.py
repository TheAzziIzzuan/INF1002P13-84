import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel('BTO Launch List 2010 - 2023.xlsx')

# Data preprocessing as needed

# Create the main application window
root = tk.Tk()
root.title("HDB BTO Launch Analysis")


# Create a button to generate the first plot
def generate_first_plot():
    # Combining the 'BTO Launch Month' and 'BTO Launch Year' columns into a single date column
    df['Launch Date'] = pd.to_datetime(df['BTO Launch Month'] + ' ' + df['BTO Launch Year'].astype(str), format='%B %Y')

    # Count the number of unique launch dates for each year
    unique_launches_per_year = df[['Launch Date']].drop_duplicates()['Launch Date'].dt.year.value_counts().sort_index()

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.bar(unique_launches_per_year.index, unique_launches_per_year.values)
    plt.xlabel('Year')
    plt.ylabel('Number of Launches')
    plt.title('Total Number of BTO Sale Launch Annually')
    # Adding data labels above each bar
    for year, launches in zip(unique_launches_per_year.index, unique_launches_per_year.values):
        plt.text(year, launches + 1, str(launches), ha='center', va='bottom')

    plt.show()


first_plot_button = tk.Button(root, text="Annual Launch Plot", command=generate_first_plot)
first_plot_button.pack()

# Start the GUI main loop
root.mainloop()
