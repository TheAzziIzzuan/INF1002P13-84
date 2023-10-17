import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk


def unit_distribution(parent_frame):
    # Load the dataset
    df = pd.read_csv('datasets\BTOLaunchList2010to2023.csv')
    
    # Ensure 'No. of Units' is in numeric format
    df['No. of Units'] = df['No. of Units'].str.replace(',', '').astype(int)

    # Pivot the data for stacked bar chart
    df_pivot = df.pivot_table(index='Estate', columns='Room Type', values='No. of Units', aggfunc='sum')

    # Set the style (optional)
    sns.set_style("whitegrid")

    # Create a figure
    fig, ax = plt.subplots(figsize=(14, 8))

    # Stacked bar chart
    df_pivot.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title('Distribution of Units by Room Type and Estate')
    ax.set_xlabel('Estate')
    ax.set_ylabel('No. of Units')

    # Rotate x-axis labels for better visibility
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

    # Adjust the layout
    plt.tight_layout()

    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    canvas = FigureCanvasTkAgg(plt.gcf(), master=parent_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)
    plt.close()

    # Calculate the top 3 estates based on "No. of Units"
    top_3_estates = df.groupby('Estate')['No. of Units'].sum().nlargest(3).reset_index()

    # Display the top 3 estates
    for idx, row in top_3_estates.iterrows():
        msg = f"Estate: {row['Estate']}, No. of Units: {row['No. of Units']}"
        label = tk.Label(parent_frame, text=msg, font=('Helvetica', 20))
        label.pack(pady=5)

    return fig
