import pandas as pd
import matplotlib.pyplot as plt
import csv

with open("datasets\hdb_latest.csv", "r") as source: 
    reader = csv.reader(source) 
      
    with open("priceanddist.csv", "w") as result: 
        writer = csv.writer(result) 
        for r in reader: 
            # copies only resale price and distance
            writer.writerow((r[6], r[17]))
