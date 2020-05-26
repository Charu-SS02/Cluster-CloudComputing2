import requests
import json
import geopy
from geopy.geocoders import Nominatim

url = "http://group26:group26@172.26.133.189:5984/tweet/_design/newview/_view/languages"
headers = {"content-type": "application/json", "Accept-Charset": "UTF-8"}

r = requests.get(url, headers=headers)

data = r.json()

states = ["New South Wales", "Victoria", "Queensland", "Western Australia", "Tasmania", "South Australia","Northern Territory"]

locator = Nominatim(user_agent="myGeocoder")

tags = {}

json_data = data["rows"]

nsw = {}
vic = {}
qld = {}
was = {}
tas = {}
sas = {}
ntr = {}

languages = {'am' : 'Amharic', 'ar' : 'Arabic', 'bg' : 'Bulgarian', 'bn' : 'Bengali', 'bo' : 'Tibetan', 'bs' : 'Bosnian', 'ca' : 'Catalan', 'ckb' : 'Sorani Kurdish', 'cs' :
             'Czech', 'cy' : 'Welsh', 'da' : 'Danish', 'de' : 'German', 'dv' : 'Maldivian', 'el' : 'Greek', 'en' : 'English', 'es' : 'Spanish', 'et' : 'Estonian', 'eu' : 'Basque', 'fa' : 'Persian', 'fi' : 'Finnish', 'fr' : 'French', 'gu' : 'Gujarati', 'he' : 'Hebrew', 'hi' : 'Hindi', 'hi-Latn' : 'Latinized Hindi', 'hr' : 'Croatian', 'ht' : 'Haitian Creole', 'hu' : 'Hungarian', 'hy' : 'Armenian', 'id' : 'Indonesian', 'is' : 'Icelandic', 'it' : 'Italian', 'ja' : 'Japanese', 'ka' : 'Georgian', 'km' : 'Khmer', 'kn' : 'Kannada', 'ko' : 'Korean', 'lo' : 'Lao', 'lt' : 'Lithuanian', 'lv' : 'Latvian', 'ml' : 'Malayalam', 'mr' : 'Marathi', 'ms' : 'Malay', 'my' : 'Burmese', 'ne' : 'Nepali', 'nl' : 'Dutch', 'no' : 'Norwegian', 'pa' : 'Punjabi', 'pl' : 'Polish', 'ps' : 'Pashto', 'pt' : 'Portuguese', 'ro' : 'Romanian', 'ru' : 'Russian', 'sd' : 'Sindhi', 'si' : 'Sinhala', 'sk' : 'Slovak', 'sl' : 'Slovenian', 'sr' : 'Serbian', 'sv' : 'Swedish', 'ta' : 'Tamil', 'te' : 'Telugu', 'th' : 'Thai', 'tl' : 'Tagalog', 'tr' : 'Turkish', 'ug' : 'Uyghur', 'uk' : 'Ukrainian', 'ur' : 'Urdu', 'vi' : 'Vietnamese', 'zh-CN' : 'Simplified Chinese', 'zh-TW' : 'Traditional Chinese', 'und' : 'Undefined', 'en-gb' : 'English UK', 'zh' : 'Chinese', 'in' : 'Indonesian'}

for data in json_data:

    try:
        
        temp = data["value"]
        lang = data["key"]
        
        if temp == "Australia":
            tas[lang] = tas.get(lang,0) + 1
            continue
            
        temp = temp.split(',')
        
        check = False
        for t in temp:
            
            t = t.strip()
        
            if t == "New South Wales":
                nsw[lang] = nsw.get(lang,0) + 1
                check = True
                break
                
            elif t == "Victoria":
                vic[lang] = vic.get(lang,0) + 1
                check = True
                break
                
            elif t == "Queensland":
                qld[lang] = qld.get(lang,0) + 1
                check = True
                break
                
            elif t == "Western Australia":
                was[lang] = was.get(lang,0) + 1
                check = True
                break
                
            elif t == "South Australia":
                sas[lang] = sas.get(lang,0) + 1
                check = True
                break
            
            elif t == "Northern Territory":
                ntr[lang] = ntr.get(lang,0) + 1
                check = True
                break
        
        if check == False:
            #print("hey2")
            for t in temp:
                t = t + ", Australia"
                location = locator.geocode(t)
                t1 = location.raw['display_name']
                t1 = t1.split(',')
                for index in t1:
                    index = index.strip()
                    if index == "New South Wales":
                        nsw[lang] = nsw.get(lang,0) + 1
                        check = True
                        break

                    elif index == "Victoria":
                        vic[lang] = vic.get(lang,0) + 1
                        check = True
                        break

                    elif index == "Queensland":
                        qld[lang] = qld.get(lang,0) + 1
                        check = True
                        break

                    elif index == "Western Australia":
                        was[lang] = was.get(lang,0) + 1
                        check = True
                        break

                    elif index == "South Australia":
                        sas[lang] = sas.get(lang,0) + 1
                        check = True
                        break

                    elif index == "Northern Territory":
                        ntr[lang] = ntr.get(lang,0) + 1
                        check = True
                        break
                break
        
    except:
        
        continue
        
#print(hey3)
        
topnsw = sorted(nsw.items(), reverse = True, key = lambda item : item[1])[0]
topvic = sorted(vic.items(), reverse = True, key = lambda item : item[1])[0]
topwas = sorted(was.items(), reverse = True, key = lambda item : item[1])[0]
topsas = sorted(sas.items(), reverse = True, key = lambda item : item[1])[0]
toptas = sorted(tas.items(), reverse = True, key = lambda item : item[1])[0]
topqld = sorted(qld.items(), reverse = True, key = lambda item : item[1])[0]
topntr = sorted(ntr.items(), reverse = True, key = lambda item : item[1])[0]

total = {"New South Wales":[languages[topnsw[0]],topnsw[1]], "Victoria":[languages[topvic[0]],topvic[1]], "Queensland":[languages[topqld[0]],topqld[1]], "Western Australia":[languages[topwas[0]],topwas[1]], "Tasmania":[languages[toptas[0]],toptas[1]], "South Australia":[languages[topsas[0]],topsas[1]],"Northern Territory":[languages[topntr[0]],topntr[1]]}

print(total)
        
with open ("total-tweets-per-state-and-languages.json", 'w') as jsonFile:
    jsonFile.write(json.dumps(total))

