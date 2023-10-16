import pandas as pd
import requests

df = pd.read_csv(r"datasets\\HDBPropertyInformation.csv")
df.head()

df['Address'] = df['blk_no'] + " " + df['street']
addresslist = list(df['Address'])

def getcoordinates(address):
    req = requests.get('https://developers.onemap.sg/commonapi/search?searchVal='+address+'&returnGeom=Y&getAddrDetails=Y&pageNum=1')
    resultsdict = eval(req.text)
    if len(resultsdict['results'])>0:
        return resultsdict['results'][0]['LATITUDE'], resultsdict['results'][0]['LONGITUDE']
    else:
        pass

coordinateslist= []
count = 0
failed_count = 0
for address in addresslist:
    try:
        if len(getcoordinates(address))>0:
            count = count + 1
            print('Extracting',count,'out of',len(addresslist),'addresses')
            coordinateslist.append(getcoordinates(address))
    except:
        count = count + 1           
        failed_count = failed_count + 1
        print('Failed to extract',count,'out of',len(addresslist),'addresses')
        coordinateslist.append(None)
print('Total Number of Addresses With No Coordinates',failed_count)

df_coordinates = pd.DataFrame(coordinateslist)
df_combined = df.join(df_coordinates)
df_combined  = df_combined .rename(columns={0:'Latitude', 1:'Longitude'})
df_combined.to_csv('hdb-property-coords(FULL).csv',index=False)

