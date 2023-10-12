import csv  
 
with open("dataset\hdb-property-coords.csv", "r") as source: 
    reader = csv.reader(source) 
      
    with open("output.csv", "w") as result: 
        writer = csv.writer(result) 
        for r in reader: 
            
            # Use CSV Index to remove a everything except blk num, street, longitude and latitude
            writer.writerow((r[0], r[1], r[25], r[26]))
