import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

df = pd.read_csv('/Users/praveenvudumu/downloads/goepy_address.csv')

geolocator = Nominatim()

# store in a df
df["Cor1"] = df["loc1"].apply(geolocator.geocode)
df["Cor2"] = df["loc2"].apply(geolocator.geocode)

df["lat1"] = df['Cor1'].apply(lambda x: x.latitude if x != None else None)
df["lon1"] = df['Cor1'].apply(lambda x: x.longitude if x != None else None)

df["lat2"] = df['Cor2'].apply(lambda x: x.latitude if x != None else None)
df["lon2"] = df['Cor2'].apply(lambda x: x.longitude if x != None else None)

def distance(row):
    add1 = (row['lat1'], row['lon1'])
    add2 = (row['lat2'], row['lon2'])
    try:
        return (geodesic(add1, add2).miles)
    except ValueError:
        return np.nan

df['dist_btw'] = df.apply(lambda row: distance(row), axis = 1 )
