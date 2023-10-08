import googlemaps
import pandas as pd

addresses = pd.read_csv("HDBPropertyInformation.csv")

gmaps = googlemaps.Client(key = 'AIzaSyAfPjwRuZlBF0g7Ed8fInVYdAO38UWcnkM')
addresses['lat'] = None
addresses['long'] = None

for x in range(len(addresses)):
    geocode_result = gmaps.geocode(addresses.loc[x, 'Full_Address'])
    try:
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        addresses.loc[x,'Lat'] = lat
        addresses.loc[x,'Lon'] = lng
    except:
        lat = None
        lng = None

addresses.to_csv('address_coords.csv')
