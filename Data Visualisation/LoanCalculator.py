import sys
import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
import customtkinter


def fifteen_years_loan(income):
    if income <= 1000:
        estimated_loan_amount = "$42,000"
    elif income <= 2000:
        estimated_loan_amount = "$86,000"
    elif income <= 3000:
        estimated_loan_amount = "$130,000"
    elif income <= 4000:
        estimated_loan_amount = "$173,000"
    elif income <= 5000:
        estimated_loan_amount = "$217,000"
    elif income <= 6000:
        estimated_loan_amount = "$260,000"
    elif income <= 7000:
        estimated_loan_amount = "$304,000"
    elif income <= 8000:
        estimated_loan_amount = "$347,000"
    elif income <= 9000:
        estimated_loan_amount = "$390,000"
    elif income <= 10000:
        estimated_loan_amount = "$434,000"
    elif income <= 11000:
        estimated_loan_amount = "$477,000"
    elif income <= 12000:
        estimated_loan_amount = "$521,000"
    elif income <= 13000:
        estimated_loan_amount = "$564,000"
    else:
        estimated_loan_amount = "$608,000"

    return estimated_loan_amount


def twenty_years_loan(income):
    if income <= 1000:
        estimated_loan_amount = "$54,000"
    elif income <= 2000:
        estimated_loan_amount = "$108,000"
    elif income <= 3000:
        estimated_loan_amount = "$162,000"
    elif income <= 4000:
        estimated_loan_amount = "$216,000"
    elif income <= 5000:
        estimated_loan_amount = "$270,000"
    elif income <= 6000:
        estimated_loan_amount = "$324,000"
    elif income <= 7000:
        estimated_loan_amount = "$378,000"
    elif income <= 8000:
        estimated_loan_amount = "$432,000"
    elif income <= 9000:
        estimated_loan_amount = "$486,000"
    elif income <= 10000:
        estimated_loan_amount = "$540,000"
    elif income <= 11000:
        estimated_loan_amount = "$595,000"
    elif income <= 12000:
        estimated_loan_amount = "$649,000"
    elif income <= 13000:
        estimated_loan_amount = "$703,000"
    else:
        estimated_loan_amount = "$757,000"

    return estimated_loan_amount


def twenty_five_years_loan(income):
    if income <= 1000:
        estimated_loan_amount = "$62,000"
    elif income <= 2000:
        estimated_loan_amount = "$126,000"
    elif income <= 3000:
        estimated_loan_amount = "$189,000"
    elif income <= 4000:
        estimated_loan_amount = "$253,000"
    elif income <= 5000:
        estimated_loan_amount = "$316,000"
    elif income <= 6000:
        estimated_loan_amount = "$379,000"
    elif income <= 7000:
        estimated_loan_amount = "$442,000"
    elif income <= 8000:
        estimated_loan_amount = "$506,000"
    elif income <= 9000:
        estimated_loan_amount = "$569,000"
    elif income <= 10000:
        estimated_loan_amount = "$632,000"
    elif income <= 11000:
        estimated_loan_amount = "$695,000"
    elif income <= 12000:
        estimated_loan_amount = "$759,000"
    elif income <= 13000:
        estimated_loan_amount = "$822,000"
    else:
        estimated_loan_amount = "$885,000"

    return estimated_loan_amount


def loancalculate(incomeinput,yearsvariable,loanresult):

    try:
        income = int(incomeinput.get())
    except ValueError:
        loanresult.config(text=f"Please enter a your income without spaces and in numbers only")
        return

    year = yearsvariable.get()

    if not year:
        loanresult.config(text=f"Please select how many loan years")
        return

    year = int(year.split()[0])
    if year == 15:
        loanamount = fifteen_years_loan(income)
    elif year == 20:
        loanamount = twenty_years_loan(income)
    elif year == 25:
        loanamount = twenty_five_years_loan(income)
    else:
        loanamount = "Invalid"

    loanresult.config(text=f"Estimated Loan Amount: {loanamount}")

#####################tkinter section########################

# customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("blue")

# gui = customtkinter.CTk()

# style = ttk.Style()
# gui.title("Estimated HDB Loan Calculator")
# gui.geometry("520x180")

# message = "Estimated HDB Loan Calculator"
# label = customtkinter.CTkLabel(gui, text=message, font=("Arial", 25))
# label.pack(anchor="center")

# income = ttk.Label(gui, text="Income:")
# income.pack()

# incomeinput = ttk.Entry(gui)
# incomeinput.pack()

# years = ttk.Label(gui, text="Loan Duration:")
# years.pack()

# yearsvariable = tk.StringVar()
# yearsselect = ttk.Combobox(gui, textvariable=yearsvariable, values=["15 years", "20 years", "25 years"], state="readonly")
# yearsselect.pack()

# calculate = customtkinter.CTkButton(gui, text="Calculate", command=loancalculate)
# calculate.place(relx=0.5, rely=0.90, anchor=customtkinter.CENTER)

# loanresult = ttk.Label(gui, text="Loan Amount: ")
# loanresult.pack()

# gui.mainloop()
