import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns


def create_price_distribution_app(parent):
    # Load your dataset
    df = pd.read_csv('..\datasets\BTOLaunchList2010to2023.csv')

    def update_plot():
        nonlocal df, room_type_var, estate_var, plot_frame
        # Get the selected variables from the custom dropdowns
        room_type = room_type_var.get()
        estate = estate_var.get()

        # Filter the data based on the selected variables
        if room_type == 'All' and estate == 'All':
            filtered_data = df
        elif room_type == 'All':
            filtered_data = df[df['Estate'] == estate]
        elif estate == 'All':
            filtered_data = df[df['Room Type'] == room_type]
        else:
            filtered_data = df[(df['Room Type'] == room_type) &
                               (df['Estate'] == estate)]

        # Create a figure for the plot
        fig, ax = plt.subplots(1, 2, figsize=(26, 16))

        # Create a box plot for MIN Indicative Price Range
        sns.boxplot(x='Room Type', y='MIN Indicative Price Range', data=filtered_data, ax=ax[0])
        ax[0].set_title('MIN Price Box Plot', fontsize=16)
        ax[0].set_xticklabels(ax[0].get_xticklabels(), rotation=35)

        # Create a box plot for MAX Indicative Price Range
        sns.boxplot(x='Room Type', y='MAX Indicative Price Range', data=filtered_data, ax=ax[1])
        ax[1].set_title('MAX Price Box Plot', fontsize=16)
        ax[1].set_xticklabels(ax[1].get_xticklabels(), rotation=35)

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, padx=10, pady=10)

    # Create a frame for the plot within the provided parent
    plot_frame = ttk.Frame(parent)
    plot_frame.grid(row=1, column=0, columnspan=4)

    # Create labels and custom dropdowns for Room Type and Estate
    room_type_var = tk.StringVar()
    room_type_options = ['All'] + list(df['Room Type'].unique())
    room_type_var.set(room_type_options[0])  # Set initial value
    room_type_label = tk.Label(parent, text="Select the Room Type:", font=('Helvetica', 12))
    room_type_label.grid(row=0, column=0, padx=2, pady=10, sticky='e')
    room_type_dropdown = tk.Menubutton(parent,
                                       textvariable=room_type_var,
                                       indicatoron=True,
                                       borderwidth=1,
                                       relief="raised", width=20)
    room_type_dropdown.grid(row=0, column=1, padx=2, pady=10, sticky='w')
    room_type_menu = tk.Menu(room_type_dropdown, tearoff=False)
    room_type_dropdown.configure(menu=room_type_menu)
    for option in room_type_options:
        room_type_menu.add_radiobutton(label=option, variable=room_type_var, value=option)

    estate_var = tk.StringVar()
    estate_options = ['All'] + list(df['Estate'].unique())
    estate_var.set(estate_options[0])  # Set initial value
    estate_label = tk.Label(parent, text="Select the Estate:", font=('Helvetica', 12))
    estate_label.grid(row=0, column=2, padx=2, pady=10, sticky='e')
    estate_dropdown = tk.Menubutton(parent,
                                    textvariable=estate_var,
                                    indicatoron=True,
                                    borderwidth=1,
                                    relief="raised",
                                    width=20)
    estate_dropdown.grid(row=0, column=3, padx=2, pady=10, sticky='w')
    estate_menu = tk.Menu(estate_dropdown, tearoff=False)
    estate_dropdown.configure(menu=estate_menu)
    for option in estate_options:
        estate_menu.add_radiobutton(label=option, variable=estate_var, value=option)

    # Create a button to update the plot
    update_button = ttk.Button(parent, text='Update Plot', command=update_plot, width=20)
    update_button.grid(row=0, column=4, padx=10, pady=10)

    # Initialize the plot
    update_plot()


if __name__ == '__main__':
    test_root = tk.Tk()
    test_frame = ttk.Frame(test_root)
    test_frame.pack(padx=10, pady=10, expand=True, fill="both")
    create_price_distribution_app(test_frame)
    test_root.mainloop()
