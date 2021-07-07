import numpy as np
import pandas as pd
import requests
from geopy.geocoders import Nominatim 
from bs4 import BeautifulSoup

html_data = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')

soup = BeautifulSoup(html_data.text, 'html.parser')
table = soup.find("table",{"rules":"all"})

table_data = []

for row in table.find_all('td'):
    cell = {}
    if row.span.text=='Not assigned':
        pass
    else:
        cell['PostalCode'] = row.p.text[:3]
        cell['Borough'] = (row.span.text).split('(')[0]
        cell['Neighborhood'] = (((((row.span.text).split('(')[1]).strip(')')).replace(' /',',')).replace(')',' ')).strip(' ')
        table_data.append(cell)

df=pd.DataFrame(table_data)

df

for i, tr in enumerate(table_rows):
    cells = tr.find_all('td')
    row = []
    for j, cell in enumerate(cells):
        row.append(cell.text.replace('\n',' ').strip())
    table_data.append(row)

table_data[1:]
df = pd.DataFrame(data=table_data[1:])    
df.columns=['CDN','DSGN_NBHD','BOROUGH','NBHD_CVD','4','5']
df.drop({'4','5'},axis=1,inplace=True)
df.head()

locator = Nominatim(user_agent='myGeocoder')
lat=[]
long=[]
for i in range(0,df.shape[1]):
    address = df['DSGN_NBHD']+', '+df['BOROUGH']+', Toronto, Ontario, Canada'
    print(address)
    location = locator.geocode(address)
    print(location)



    lat.append(location.latitude)
    long.append(location.longitude)

loc

location = locator.geocode('Banbury-Don Mills, North York, Toronto, Ontario, Canada')
print(location)
