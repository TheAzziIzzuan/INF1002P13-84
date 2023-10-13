import pandas as pd
import matplotlib.pyplot as plt
import csv

with open("project\datasets\HDBvsPrimarySchool.csv", "r") as source: 
    reader = csv.reader(source) 
      
    with open("schoolandprice(clean).csv", "w") as result: 
        writer = csv.writer(result) 
        for r in reader: 
            # copies only resale price and distance
            writer.writerow((r[5],r[11]))
