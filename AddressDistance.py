#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:03:40 2020

@author: praveenvudumu
"""

from geopy.geocoders import Nominatim
geolocator = Nominatim()

from1 = geolocator.geocode("8510 e 29th st n, wichita")
fromcor = ((from1.latitude, from1.longitude))

to = geolocator.geocode("4111 e 37th st n, wichita")
tocor = ((to.latitude, to.longitude))

from geopy.distance import geodesic
print(geodesic(fromcor, tocor).miles)

from geopy.distance import great_circle
print(great_circle(fromcor, tocor).miles)

#df[full_add] = df["st"]+", "+df["st2"]+", "+df["city"]

###########################################################################

import pandas as pd
df = pd.read_csv('/Users/praveenvudumu/downloads/goepy_address.csv')
from geopy.geocoders import Nominatim
geolocator = Nominatim()

# store in a df
df["Cor1"] = df["loc1"].apply(geolocator.geocode)
df["Cor2"] = df["loc2"].apply(geolocator.geocode)

df["lat1"] = df['Cor1'].apply(lambda x: x.latitude if x != None else None)
df["lon1"] = df['Cor1'].apply(lambda x: x.longitude if x != None else None)

df["lat2"] = df['Cor2'].apply(lambda x: x.latitude if x != None else None)
df["lon2"] = df['Cor2'].apply(lambda x: x.longitude if x != None else None)

#df = df.dropna()

from geopy.distance import geodesic

def distance(row):
    add1 = (row['lat1'], row['lon1'])
    add2 = (row['lat2'], row['lon2'])
    return (geodesic(add1, add2).miles)

#df['dist_btw'] = df.apply(lambda row: distance(row), axis = 1 )

df['dist_btw'] = df.apply(lambda row: distance(row), axis = 1 )
