import json
import requests
from datetime import datetime
from db_commands import FlightTrackerCluster
from env_variables import QPX_API_KEY, ORIGIN_TWO, DESTINATION_TWO, DEPARTURE_DATE
# from env_variables import RETURN_DATE

############################################## Set-Up ################################################
url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=' + QPX_API_KEY
headers = {'content-type': 'application/json'}

myCluster = FlightTrackerCluster()
myCluster.changeKeySpace('plane')


first = raw_input('Are we starting Fresh? (Type Y if so): ')
if first == 'Y':
    myCluster.createTable('Tickets', ['time', 'day', 'price', 'carrier', 'origin', 'destination', 'departure_date', 'concat'])
    print("\nStarting up the script! \n")
else:
    print("\nStarting up the script! \n")

params = myCluster.getParams(ORIGIN_TWO, DESTINATION_TWO, DEPARTURE_DATE, 100)
# params = myCluster.getParams(ORIGIN_TWO, DESTINATION_TWO, DEPARTURE_DATE, RETURN_DATE, 100)

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

        concat = time + ", " + price + ", " + carrier + ", " + ORIGIN_TWO + ", " + DESTINATION_TWO + ", " + DEPARTURE_DATE
        print "DATA:   Hour-Day-Month-Year, Price, Carrier, Origin, Destination, Date, [Everything together]"
        print "---------------------------------------------------------------------------------------------"
        print concat + "    [" + concat + "]"

        myCluster.insertData('Tickets', ['time', 'day', 'price', 'carrier', 'origin', 'destination', 'departure_date', 'concat'], 
            [time, str(day_of_week), price, carrier, ORIGIN_TWO, DESTINATION_TWO, DEPARTURE_DATE, concat])

############################################## SCRIPT ################################################
