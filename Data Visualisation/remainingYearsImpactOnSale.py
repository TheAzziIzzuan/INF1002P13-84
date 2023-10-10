import datetime
import tkinter

import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import ttk
import customtkinter
from tkinter import filedialog


def df_to_csv(room_data, filename_prefix):
    filename = f"{filename_prefix}.csv"
    df = pd.DataFrame(room_data)
    df.to_csv(filename, index=False)


# gets data from csv and split them into individual data
def remainingYearImpactonSale(room_type):
    data = pd.read_csv('..\datasets\Resale_Flat_Prices_Jan_2013_to_Sep_2023.csv')

    room_data = data[data["flat_type"] == room_type].copy()

    # gets data of prices and lease commence date
    # two_room_prices = two_room_data["resale_price"]
    # lease_commence_date = two_room_data["lease_commence_date"]

    # get the current year
    current_year = datetime.datetime.now().year
    # get remaining lease year by subtracting 99 - (current year - lease commence date)
    room_data.loc[:, "remaining_years"] = 99 - (current_year - room_data["lease_commence_date"].astype(int))

    # plot scatter plot using scatter()
    plt.figure(figsize=(10, 6))
    plt.scatter(room_data["remaining_years"], room_data["resale_price"], alpha=0.5)
    plt.title(f"{room_type} Resale Flat Prices.")
    plt.xlabel("Age Left")
    plt.ylabel("Resale Price")
    plt.grid(True)

    exportbutton = tkinter.Button(text="Export", command=lambda: df_to_csv(room_data, room_type))
    exportbutton.pack()

    plt.show()


# Get Remaining Year Impact on Sale for all type of room
# remainingYearImpactonSale("2 ROOM")
# remainingYearImpactonSale("3 ROOM")
# remainingYearImpactonSale("4 ROOM")
# remainingYearImpactonSale("5 ROOM")
# remainingYearImpactonSale("EXECUTIVE")


# this function is when a button is click,it executes the command that calls the graph which is remainingYearImpactonSale(room_type)
def click_button(room_type):
    remainingYearImpactonSale(room_type)


customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

gui = customtkinter.CTk()

style = ttk.Style()
gui.title("Resale Flat Prices")
gui.geometry("1080x720")

room_types = ["2 ROOM", "3 ROOM", "4 ROOM", "5 ROOM", "EXECUTIVE"]

# text section
message = "This page shows if the remaining years of HDB(the Age) affects the resale price"
label = customtkinter.CTkLabel(gui, text=message, font=("Arial", 30))
label.pack(anchor="center", expand=True)

# buttons section
TWO_ROOM_BUTTON = customtkinter.CTkButton(gui, text=room_types[0], command=lambda: click_button(room_types[0]))
TWO_ROOM_BUTTON.place(relx=0.1, rely=0.8, anchor=customtkinter.CENTER)

THREE_ROOM_BUTTON = customtkinter.CTkButton(gui, text=room_types[1], command=lambda: click_button(room_types[1]))
THREE_ROOM_BUTTON.place(relx=0.3, rely=0.8, anchor=customtkinter.CENTER)

FOUR_ROOM_BUTTON = customtkinter.CTkButton(gui, text=room_types[2], command=lambda: click_button(room_types[2]))
FOUR_ROOM_BUTTON.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

FIVE_ROOM_BUTTON = customtkinter.CTkButton(gui, text=room_types[3], command=lambda: click_button(room_types[3]))
FIVE_ROOM_BUTTON.place(relx=0.7, rely=0.8, anchor=customtkinter.CENTER)

EXECUTIVE_ROOM_BUTTON = customtkinter.CTkButton(gui, text=room_types[4], command=lambda: click_button(room_types[4]))
EXECUTIVE_ROOM_BUTTON.place(relx=0.9, rely=0.8, anchor=customtkinter.CENTER)

gui.mainloop()
