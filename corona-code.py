import requests
import csv
from collections import Counter 

date=input("date in mm-dd-yyyy: ")
obj = requests.get(f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{date}.csv").text
lines= obj.splitlines()
rawdata=csv.reader(lines)
data=[row for row in rawdata]

bystate={}
#get state
for place in data:
    if place[0] == place[1]: #aka france, france or denmark, denmark
        continue
    elif place[0] == "":  #just a country
        continue
    bystate.update({f"{place[0]}, {place[1]}":[place[2],place[3],place[4],place[5]]})  #data for each place is Last Update, Confirmed, Deaths, Recovered

#print(bystate)

bycountry={}
#get countries
for place in data:
    if place[0] == "":
        bycountry.update({place[1]:[place[2],place[3],place[4],place[5]]})

#add up the ones counted as states, with more than 1 entry, such as USA and China
places=[]
for place in bystate:
    places.append(place.split(","))

countries=[]
for place in places:
    countries.append(place[1])  #countries is a list which can be referenced so that all the states can be added up to get a country
print(countries)

counted = Counter(countries) 
countries_cleanedup=[place for place in countries if counted[place] > 1]#what countries was supposed to be

#for 

 
