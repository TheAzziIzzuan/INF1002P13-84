import datetime
import tkinter
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import ttk
import customtkinter
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

canvas = None
currentroomtype = None


# export function
def exportcsv(room_type):
    if currentroomtype is not None:  # if the global current room type is not empty
        data = remainingYearImpactonSale(room_type)  # get its data from remainingYearsImpactonSale Function
        filename = f"List of {room_type}.csv"  # get name of room_type user selected
        df = pd.DataFrame(data)  # select the data that has the room_type
        df.to_csv(filename, index=False)
    else:
        tkinter.messagebox.showinfo("ERROR!",
                                    "No Room Type is selected!")  # if global current room type is empty it will return a error pop up


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
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(room_data["remaining_years"], room_data["resale_price"], alpha=0.5)
    ax.set_title(f"{room_type} Resale Flat Prices.")
    ax.set_xlabel("Age Left")
    ax.set_ylabel("Resale Price")
    ax.grid(True)

    global canvas  # declares a global canvas
    if canvas is not None:  # if there is a graph displayed on the the canvas
        canvas.get_tk_widget().destroy()  # it will destroy before displaying another graph

    canvas = FigureCanvasTkAgg(fig, master=gui)
    canvas.get_tk_widget().pack()
    canvas.draw()
    return room_data


# Get Remaining Year Impact on Sale for all type of room
# remainingYearImpactonSale("2 ROOM")
# remainingYearImpactonSale("3 ROOM")
# remainingYearImpactonSale("4 ROOM")
# remainingYearImpactonSale("5 ROOM")
# remainingYearImpactonSale("EXECUTIVE")


# this function is when a button is click,it executes the command that calls the graph which is remainingYearImpactonSale(room_type)
def click_button(room_type):
    global currentroomtype
    currentroomtype = room_type
    remainingYearImpactonSale(room_type)


#####################tkinter section########################
# this function uses customtkinter to set the colours of background and buttons.
customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

gui = customtkinter.CTk()

style = ttk.Style()
gui.title("Remaining years of HDB(the Age) affects the resale price")
gui.geometry("1080x720")

room_types = ["2 ROOM", "3 ROOM", "4 ROOM", "5 ROOM", "EXECUTIVE"]

# text section
message = "Remaining years of HDB(the Age) affects the resale price"
label = customtkinter.CTkLabel(gui, text=message, font=("Arial", 25))
label.pack(anchor="center")

# buttons section
# from two,three,four,five and executive buttons, the buttons will call the function of showing the graph depending on the room type that user selected
TWO_ROOM_BUTTON = customtkinter.CTkButton(gui, text=room_types[0], command=lambda: click_button(room_types[0]))
TWO_ROOM_BUTTON.place(relx=0.1, rely=0.92, anchor=customtkinter.CENTER)

THREE_ROOM_BUTTON = customtkinter.CTkButton(gui, text=room_types[1], command=lambda: click_button(room_types[1]))
THREE_ROOM_BUTTON.place(relx=0.3, rely=0.92, anchor=customtkinter.CENTER)

FOUR_ROOM_BUTTON = customtkinter.CTkButton(gui, text=room_types[2], command=lambda: click_button(room_types[2]))
FOUR_ROOM_BUTTON.place(relx=0.5, rely=0.92, anchor=customtkinter.CENTER)

FIVE_ROOM_BUTTON = customtkinter.CTkButton(gui, text=room_types[3], command=lambda: click_button(room_types[3]))
FIVE_ROOM_BUTTON.place(relx=0.7, rely=0.92, anchor=customtkinter.CENTER)

EXECUTIVE_ROOM_BUTTON = customtkinter.CTkButton(gui, text=room_types[4], command=lambda: click_button(room_types[4]))
EXECUTIVE_ROOM_BUTTON.place(relx=0.9, rely=0.92, anchor=customtkinter.CENTER)

EXPORT = customtkinter.CTkButton(gui, text="EXPORT TO CSV", command=lambda: exportcsv(currentroomtype))
EXPORT.place(relx=0.5, rely=0.97, anchor=customtkinter.CENTER)

gui.mainloop()
