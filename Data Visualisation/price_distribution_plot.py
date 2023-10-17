import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import seaborn as sns

df = pd.read_csv('datasets\BTOLaunchList2010to2023.csv')
df['Launch Date'] = pd.to_datetime(df['BTO Launch Month'] + ' ' + df['BTO Launch Year'].astype(str), format='%B %Y')
df['Year'] = df['Launch Date'].dt.year
df['MIN Indicative Price Range'] = pd.to_numeric(df['MIN Indicative Price Range'].str.replace(',', ''), errors='coerce')
df['MAX Indicative Price Range'] = pd.to_numeric(df['MAX Indicative Price Range'].str.replace(',', ''), errors='coerce')

def draw_default_plot(frame):
    min_prices_per_year = df.groupby('Year')['MIN Indicative Price Range'].mean()
    max_prices_per_year = df.groupby('Year')['MAX Indicative Price Range'].mean()
    return draw_plot(frame, min_prices_per_year, max_prices_per_year, 'BTO Price Analysis', [])

def draw_plot(frame, min_prices, max_prices, title, selected_rooms):
    # Create a copy to avoid modifying the original dataframe
    filtered_df = df[df['Room Type'].isin(selected_rooms)].copy() if selected_rooms else df.copy()

    # Combining the 'BTO Launch Month' and 'BTO Launch Year' columns into a single date column
    filtered_df['Launch Date'] = pd.to_datetime(filtered_df['BTO Launch Month'] + ' ' + filtered_df['BTO Launch Year'].astype(str), format='%B %Y')
    
    # Create a 'Year' column for easier grouping
    filtered_df['Year'] = filtered_df['Launch Date'].dt.year
    
    # Ensure price columns are numeric after removing commas
    if not pd.api.types.is_numeric_dtype(filtered_df['MIN Indicative Price Range']):
        filtered_df['MIN Indicative Price Range'] = pd.to_numeric(filtered_df['MIN Indicative Price Range'].str.replace(',', ''), errors='coerce')
        
    if not pd.api.types.is_numeric_dtype(filtered_df['MAX Indicative Price Range']):
        filtered_df['MAX Indicative Price Range'] = pd.to_numeric(filtered_df['MAX Indicative Price Range'].str.replace(',', ''), errors='coerce')

    min_prices_per_year = filtered_df.groupby('Year')['MIN Indicative Price Range'].mean()
    max_prices_per_year = filtered_df.groupby('Year')['MAX Indicative Price Range'].mean()

    fig, axs = plt.subplots(2, 1, figsize=(15, 10))
    
    # Plot minimum prices over the years
    min_prices_per_year.plot(ax=axs[0], marker='o', color='b', label="Minimum Price")
    axs[0].set_title("Minimum BTO Prices Over the Years")
    axs[0].set_xlabel("Year")
    axs[0].set_ylabel("Price")
    axs[0].grid(True)
    axs[0].legend()

    # Plot maximum prices over the years
    max_prices_per_year.plot(ax=axs[1], marker='o', color='r', label="Maximum Price")
    axs[1].set_title("Maximum BTO Prices Over the Years")
    axs[1].set_xlabel("Year")
    axs[1].set_ylabel("Price")
    axs[1].grid(True)
    axs[1].legend()

    fig.tight_layout()
    fig.subplots_adjust(hspace=0.5)  # Adjust space between plots
    fig.suptitle('BTO Price Analysis for Selected Room Types', y=1.02)

    # Render the plot on the canvas in the given frame
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=3, column=0, columnspan=3, padx=10, pady=10)  # Added padding for better layout

    return fig


def plot_prices_for_selected_rooms(frame, selected_rooms=[]):
    if not selected_rooms:  # No room types selected, display default
        return draw_default_plot(frame)

    filtered_df = df[df['Room Type'].isin(selected_rooms)]
    min_prices_per_year = filtered_df.groupby('Year')['MIN Indicative Price Range'].mean()
    max_prices_per_year = filtered_df.groupby('Year')['MAX Indicative Price Range'].mean()

    return draw_plot(frame, min_prices_per_year, max_prices_per_year, 'BTO Price Analysis for Selected Room Types', selected_rooms)

def destroy_canvas(frame):
    for widget in frame.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg):
            widget.get_tk_widget().destroy()  # Destroy only the canvas


def plot_price_analysis(master_frame):
    master_frame.columnconfigure(1, weight=1)
    master_frame.rowconfigure(0, weight=1)

    # Frame for filter (listbox + buttons)
    filter_frame = tk.Frame(master_frame)
    filter_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ns')

    # Frame for the plot
    plot_frame = tk.Frame(master_frame)
    plot_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

    label = tk.Label(filter_frame, text="Select Room Types:")
    label.grid(row=0, column=0, pady=(0, 10), sticky='w')

    # Listbox within the filter frame
    listbox = tk.Listbox(filter_frame, selectmode=tk.MULTIPLE)
    unique_room_types = df['Room Type'].unique()
    for room_type in unique_room_types:
        listbox.insert(tk.END, room_type)
    listbox.grid(row=1, column=0, sticky='nsew')

    update_button = tk.Button(filter_frame, text="Update", command=lambda: plot_prices_for_selected_rooms(plot_frame, [listbox.get(i) for i in listbox.curselection()]))
    update_button.grid(row=2, column=0, pady=(10, 5))

    clear_button = tk.Button(filter_frame, text="Clear", command=lambda: [listbox.selection_clear(0, tk.END), plot_prices_for_selected_rooms(plot_frame)])
    clear_button.grid(row=3, column=0, pady=(5, 10))

    plot_prices_for_selected_rooms(plot_frame)  # Initially show the default plot

    return master_frame


def plot_prices_for_estate_and_room(master_frame):
    master_frame.columnconfigure(1, weight=1)
    master_frame.rowconfigure(0, weight=1)

    # Frame for filter (listbox + buttons)
    filter_frame = tk.Frame(master_frame)
    filter_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ns')

    # Frame for the plot
    plot_frame = tk.Frame(master_frame)
    plot_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

    label1 = tk.Label(filter_frame, text="Select Estate:")
    label1.grid(row=0, column=0, pady=(0, 10), sticky='w')
    
    estate_listbox = tk.Listbox(filter_frame, selectmode=tk.SINGLE)
    unique_estates = df['Estate'].unique()
    for estate in unique_estates:
        estate_listbox.insert(tk.END, estate)
    estate_listbox.grid(row=1, column=0, sticky='nsew')


    update_button = tk.Button(filter_frame, text="Update", command=lambda: plot_prices_for_selected_estate_and_rooms(plot_frame, estate_listbox.get(estate_listbox.curselection())))
    update_button.grid(row=4, column=0, pady=(10, 5))

    clear_button = tk.Button(filter_frame, text="Clear", command=lambda: [estate_listbox.selection_clear(0, tk.END), plot_prices_for_selected_estate_and_rooms(plot_frame)])
    clear_button.grid(row=5, column=0, pady=(5, 10))

    plot_prices_for_selected_estate_and_rooms(plot_frame)  # Initially show the default plot

    return master_frame

def plot_prices_for_selected_estate_and_rooms(frame, selected_estate=None, selected_rooms=[]):
    if not selected_rooms and not selected_estate:  # No room types and estate selected, display default
        return draw_default_plot(frame)

    # Filter dataframe by selected estate and rooms
    filtered_df = df.copy()
    if selected_estate:
        filtered_df = filtered_df[filtered_df['Estate'] == selected_estate]
    if selected_rooms:
        filtered_df = filtered_df[filtered_df['Room Type'].isin(selected_rooms)]
    
    min_prices_per_year = filtered_df.groupby(['Year', 'Room Type'])['MIN Indicative Price Range'].mean().unstack()
    max_prices_per_year = filtered_df.groupby(['Year', 'Room Type'])['MAX Indicative Price Range'].mean().unstack()

    return draw_detailed_plot(frame, min_prices_per_year, max_prices_per_year, 'BTO Price Analysis for Selected Estate and Room Types')

def draw_detailed_plot(frame, min_prices, max_prices, title):
    fig, axs = plt.subplots(2, 1, figsize=(15, 10))
    
    min_prices.plot(ax=axs[0], marker='o')
    axs[0].set_title("Minimum BTO Prices Over the Years")
    axs[0].set_xlabel("Year")
    axs[0].set_ylabel("Price")
    axs[0].grid(True)
    axs[0].legend(loc="upper left")

    max_prices.plot(ax=axs[1], marker='o')
    axs[1].set_title("Maximum BTO Prices Over the Years")
    axs[1].set_xlabel("Year")
    axs[1].set_ylabel("Price")
    axs[1].grid(True)
    axs[1].legend(loc="upper left")

    fig.tight_layout()
    fig.subplots_adjust(hspace=0.5)
    fig.suptitle(title, y=1.02)

    # Render the plot on the canvas in the given frame
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    return fig


def plot_prices_by_maturity_and_roomtype(tab):
    # GUI Layout
    tab.grid_rowconfigure(0, weight=1)
    tab.grid_columnconfigure(1, weight=1)

    plot_frame = tk.Frame(tab)
    plot_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

    def draw_plots(plot_frame):
        for widget in plot_frame.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()

        default_maturities = df['Estate Maturity'].unique()[:3]  # Display min and max prices for the first 3 estate maturities
        fig, axes = plt.subplots(2, 3, figsize=(20, 10))

        for idx, maturity in enumerate(default_maturities):
            filtered_df = df[df['Estate Maturity'] == maturity]

            min_prices_per_year = filtered_df.groupby('Year')['MIN Indicative Price Range'].mean()
            max_prices_per_year = filtered_df.groupby('Year')['MAX Indicative Price Range'].mean()

            # Plot for Min Price
            row_idx = idx // 3  # Determine the row index for the subplot
            col_idx = idx % 3   # Determine the column index for the subplot
            axes[row_idx][col_idx].plot(min_prices_per_year.index, min_prices_per_year.values, label='Min Price', marker='o', color='blue')
            axes[row_idx][col_idx].set_title(f'Min Price ({maturity})')
            axes[row_idx][col_idx].legend()
            axes[row_idx][col_idx].grid(True)

            # Plot for Max Price
            axes[row_idx+1][col_idx].plot(max_prices_per_year.index, max_prices_per_year.values, label='Max Price', marker='o', color='red')
            axes[row_idx+1][col_idx].set_title(f'Max Price ({maturity})')
            axes[row_idx+1][col_idx].legend()
            axes[row_idx+1][col_idx].grid(True)

        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    draw_plots(plot_frame)
