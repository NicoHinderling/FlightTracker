import json
import requests
from datetime import datetime
from time import sleep
from db_commands import FlightTrackerCluster
from env_variables import QPX_API_KEY, ORIGIN_ONE, DESTINATION_ONE, ORIGIN_TWO, DESTINATION_TWO, DEPARTURE_DATE
# from env_variables import RETURN_DATE

############################################## Set-Up ################################################
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

myCluster = FlightTrackerCluster()

#Comment out this line after you've created the Key Space the first time
myCluster.createKeySpace('Tickets')

myCluster.changeKeySpace('Tickets')

first = raw_input('Are we starting Fresh? (Type Y if so): ')
if first == 'Y':
    myCluster.createTable('Tickets', ['time', 'day', 'price', 'carrier', 'origin', 'destination', 'departure_date', 'concat'])
    print("\nStarting up the script! \n")
else:
    print("\nStarting up the script! \n")

params_one = myCluster.getParams(ORIGIN_ONE, DESTINATION_ONE, DEPARTURE_DATE, 100)
params_two = myCluster.getParams(ORIGIN_TWO, DESTINATION_TWO, DEPARTURE_DATE, 100)
# params = myCluster.getParams(ORIGIN_ONE, DESTINATION_ONE, DEPARTURE_DATE, RETURN_DATE, 100)

last = None

def writeToCassandra(params, time, day_of_week, origin, destination, departure_date):
        url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=' + QPX_API_KEY
        headers = {'content-type': 'application/json'}
        
        response = requests.post(url, data=json.dumps(params), headers=headers)
        data = response.json()

        price = data['trips']['tripOption'][0]['saleTotal']
        carrier = data['trips']['tripOption'][0]['slice'][0]['segment'][0]['flight']['carrier']

        concat = time + ", " +  day_of_week + ", " + price + ", " + carrier + ", " + origin + ", " + destination + ", " + departure_date
        print concat + "    [" + concat + "]"

        myCluster.insertData('Tickets', ['time', 'day', 'price', 'carrier', 'origin', 'destination', 'departure_date', 'concat'], 
            [time, day_of_week, price, carrier, origin, destination, departure_date, concat])
############################################## Set-Up ################################################

############################################## SCRIPT ################################################

while True:
    if last != datetime.now().hour:
        last = datetime.now().hour
        print "DATA:   Hour-Day-Month-Year, Price, Carrier, Origin, Destination, Date, [Everything together]"
        print "---------------------------------------------------------------------------------------------"

        time = str(datetime.now().hour) + "-" + str(datetime.now().day) + "-" + \
            str(datetime.now().month) + "-" + str(datetime.now().year)
        day_of_week = datetime.today().weekday()
        which_day = days[day_of_week]

        writeToCassandra(params_one, time, which_day, ORIGIN_ONE, DESTINATION_ONE, DEPARTURE_DATE)
        writeToCassandra(params_two, time, which_day, ORIGIN_TWO, DESTINATION_TWO, DEPARTURE_DATE)

############################################## SCRIPT ################################################
