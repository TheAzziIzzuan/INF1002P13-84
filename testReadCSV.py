import sys, csv

#test reading of CSV file
with open('datasets/Resale_Flat_Prices_Jan_2015_to_Dec_2016.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)