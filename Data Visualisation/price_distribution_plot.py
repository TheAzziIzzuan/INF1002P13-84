import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk



def price_distribution(parent_frame):
    # Load the dataset
    df = pd.read_csv('datasets\BTOLaunchList2010to2023.csv')

    # Remove commas and convert to numeric
    df['MIN Indicative Price Range'] = df['MIN Indicative Price Range'].str.replace(',', '').astype(float)
    df['MAX Indicative Price Range'] = df['MAX Indicative Price Range'].str.replace(',', '').astype(float)

    # Group the data by 'BTO Launch Year' and 'Room Type' and calculate the mean price for each group
    price_trend_data = df.groupby(['BTO Launch Year', 'Room Type'])[['MIN Indicative Price Range', 'MAX Indicative Price Range']].mean().reset_index()

    # Set the style for the Seaborn plots (optional)
    sns.set(style="whitegrid")

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Plot the price trend for 'MIN Indicative Price Range'
    sns.lineplot(data=price_trend_data, x='BTO Launch Year', y='MIN Indicative Price Range', hue='Room Type', ax=ax1)
    ax1.set_title('MIN Indicative Price Range')
    ax1.set_xlabel('BTO Launch Year')
    ax1.set_ylabel('Price Range')

    # Plot the price trend for 'MAX Indicative Price Range'
    sns.lineplot(data=price_trend_data, x='BTO Launch Year', y='MAX Indicative Price Range', hue='Room Type', ax=ax2)
    ax2.set_title('MAX Indicative Price Range')
    ax2.set_xlabel('BTO Launch Year')
    ax2.set_ylabel('Price Range')

    # Show the legend for both subplots
    ax1.legend(title='Room Type', loc='upper left', bbox_to_anchor=(1, 1))
    ax2.legend(title='Room Type', loc='upper left', bbox_to_anchor=(1, 1))

    # Adjust the layout
    plt.tight_layout()

    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    canvas = FigureCanvasTkAgg(plt.gcf(), master=parent_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)
    plt.close()