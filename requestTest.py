import json
import requests
import credentials

api_key = credentials.QPX
url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=' + api_key
headers = {'content-type': 'application/json'}

params = {
  "request": {
    "passengers": {
      "adultCount": 1
    },
    "solutions": 20,
    "slice": [
      {
        "origin": "BOS",
        "destination": "LAX",
        "date": "2015-10-26"
      },
      {
        "origin": "LAX",
        "destination": "BOS",
        "date": "2015-11-29"
      }
    ]
  }
}

response = requests.post(url, data=json.dumps(params), headers=headers)
data = response.json()
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

#print data