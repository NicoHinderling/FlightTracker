
import json
import requests
from datetime import datetime
from db_commands import FlightTrackerCluster
from env_variables import QPX_API_KEY, ORIGIN, DESTINATION, DEPARTURE_DATE
# from env_variables import RETURN_DATE

############################################## Set-Up ################################################
url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=' + QPX_API_KEY
headers = {'content-type': 'application/json'}

myCluster = FlightTrackerCluster()
myCluster.changeKeySpace('plane')


first = raw_input('Are we starting Fresh? (Type Y if so): ')
if first == 'Y':
    # myCluster.deleteTable('Tickets')
    myCluster.createTable('Tickets', ['time', 'day', 'price', 'carrier', 'origin', 'destination', 'departure_date'])
    print("Starting up the script! \n")
else:
    print("Starting up the script! \n")

params = myCluster.getParams(ORIGIN, DESTINATION, DEPARTURE_DATE, 100)
# params = myCluster.getParams(ORIGIN, DESTINATION, DEPARTURE_DATE, RETURN_DATE, 100)

last = None
############################################## Set-Up ################################################

############################################## SCRIPT ################################################

while True:
    if last != datetime.now().hour:
        last = datetime.now().hour
        response = requests.post(url, data=json.dumps(params), headers=headers)
        data = response.json()

        time = str(datetime.now().hour) + "-" + str(datetime.now().day) + "-" + \
            str(datetime.now().month) + "-" + str(datetime.now().year)
        day_of_week = datetime.today().weekday()
        price = data['trips']['tripOption'][0]['saleTotal']
        carrier = data['trips']['tripOption'][0]['slice'][0]['segment'][0]['flight']['carrier']

        print time + ", " + price + ", " + carrier + ", " + ORIGIN + ", " + DESTINATION + ", " + DEPARTURE_DATE

        myCluster.insertData('Tickets', ['time', 'day', 'price', 'carrier', 'origin', 'destination', 'departure_date'], 
            [time, str(day_of_week), price, carrier, ORIGIN, DESTINATION, DEPARTURE_DATE])