import requests
import json
import geopy
from geopy.geocoders import Nominatim

url = "http://group26:group26@172.26.133.189:5984/tweet/_design/newview/_view/new-view"
headers = {"content-type": "application/json", "Accept-Charset": "UTF-8"}

r = requests.get(url, headers=headers)

data = r.json()

states = ["New South Wales", "Victoria", "Queensland", "Western Australia", "Tasmania", "South Australia","Northern Territory"]

locator = Nominatim(user_agent="myGeocoder")

tags = {}

json_data = data["rows"]

for data in json_data:

    try:
        temp = data["value"]
        
        if temp == "Australia":
            tags["Tasmania"] = tags.get("Tasmania",0) + 1
            continue
        
        temp = temp.split(',')
        
        check = False
        for t in temp:
            t = t.strip()
            if t in states:
                tags[t] = tags.get(t,0) + 1
                check = True
                break
            
        if check == False:
            for t in temp:
                t = t + ", Australia"
                location = locator.geocode(t)
                t1 = location.raw['display_name']
                t1 = t1.split(',')
                for index in t1:
                    index = index.strip()
                    if index in states:
                        tags[index] = tags.get(index,0) + 1
                        check = True
                        break
                break
    except:
        continue
        
print(tags)
                
with open ("foreign-tweets-per-state.json", 'w') as jsonFile:
    jsonFile.write(json.dumps(tags))