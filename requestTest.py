import json
import requests
import credentials

api_key = credentials.QPX
url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=' + api_key
headers = {'content-type': 'application/json'}

##############################
######### Parameters #########
origin = "BOS"
destination = "LAX"
round_trip = True
departure_date = "2015-10-26"
return_date = "2015-11-29"
##############################
##############################

params = getParams(origin, destination, round_trip, departure_date, return_date)

response = requests.post(url, data=json.dumps(params), headers=headers)
data = response.json()
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile, indent=4)
print data

"""
  CREATE TABLE {} (
    id text PRIMARY KEY,
    age int,
    state text
);
"""

tableData = ['id text PRIMARY KEY', 'age int', 'state text']
newTableData = ['id', 'age', 'state']


def getParams(origin, destination, round_trip, departure_date, return_date=None):
    slice = [
        {
          "origin": origin,
          "destination": destination,
          "date": round_trip
        }
    ]

    if round_trip == True 
        if return_date == None:
            return "Please add your return date"
        else:
            slice.append({
                    "origin": destination,
                    "destination": origin,
                    "date": departure_date
                })
    params = {
        "request": {
            "passengers": {
                "adultCount": 1
            },
            "solutions": 2,
            "slice": slice 
            }
        }    
    return params


