import datetime

import matplotlib.pyplot as plt
import pandas as pd


def remainingYearImpactonSale(room_type):
    data = pd.read_csv('..\datasets\Resale_Flat_Prices_Jan_2013_to_Sep_2023.csv')

    two_room_data = data[data["flat_type"] == room_type].copy()

    # gets data of prices and lease commence date
    # two_room_prices = two_room_data["resale_price"]
    # lease_commence_date = two_room_data["lease_commence_date"]

    # get the current year
    current_year = datetime.datetime.now().year
    # get remaining lease year by subtracting 99 - (current year - lease commence date)
    two_room_data.loc[:, "remaining_years"] = 99 - (current_year - two_room_data["lease_commence_date"].astype(int))

    # plot scatter plot using scatter()
    plt.figure(figsize=(10, 6))
    plt.scatter(two_room_data["remaining_years"], two_room_data["resale_price"], alpha=0.5)
    plt.title(f"{room_type} Resale Flat Prices.")
    plt.xlabel("Age Left")
    plt.ylabel("Resale Price")
    plt.grid(True)
    plt.show()


# Get Remaining Year Impact on Sale for all type of room
remainingYearImpactonSale("2 ROOM")
remainingYearImpactonSale("3 ROOM")
remainingYearImpactonSale("4 ROOM")
remainingYearImpactonSale("5 ROOM")
remainingYearImpactonSale("EXECUTIVE")
