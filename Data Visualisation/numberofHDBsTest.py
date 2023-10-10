import pandas as pd
import matplotlib.pyplot as plt

def noHDBs():
    df = pd.read_csv('datasets\HDBPropertyInformation.csv')
    pivot = df.pivot_table(index =['bldg_contract_town'],  
                        values =['total_dwelling_units'], aggfunc ='sum') 
    return df['bldg_contract_town'], df['total_dwelling_units'] 

noHDBs()