import json
import requests
from time import sleep
from random import randint
from datetime import datetime
from db_commands import FlightTrackerCluster
from env_variables import QPX_API_KEY, ORIGIN_ONE, DESTINATION_ONE, ORIGIN_TWO, DESTINATION_TWO, DEPARTURE_DATE
from env_variables import QPX_API_KEY_TWO, ORIGIN_THREE, DESTINATION_THREE, ORIGIN_FOUR, DESTINATION_FOUR
# from env_variables import RETURN_DATE

############################################## Set-Up ################################################
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

myCluster = FlightTrackerCluster()
myCluster.createKeySpace('plane')
myCluster.changeKeySpace('plane')

#Uncomment the first time to create the table
myCluster.createTable('tickets', ['hour', 'date', 'day', 'carrier', 'origin', 'destination', 'departure_date', 'price'], ['day', 'date', 'origin', 'destination', 'price', 'hour'])


params_one = myCluster.getParams(ORIGIN_ONE, DESTINATION_ONE, DEPARTURE_DATE, 100)
params_two = myCluster.getParams(ORIGIN_TWO, DESTINATION_TWO, DEPARTURE_DATE, 100)
params_three = myCluster.getParams(ORIGIN_THREE, DESTINATION_THREE, DEPARTURE_DATE, 100)
params_four = myCluster.getParams(ORIGIN_FOUR, DESTINATION_FOUR, DEPARTURE_DATE, 100)
# params = myCluster.getParams(ORIGIN_ONE, DESTINATION_ONE, DEPARTURE_DATE, RETURN_DATE, 100)

last = None

def writeToCassandra(params, hour, date, day_of_week, origin, destination, departure_date, api_key):
    url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=' + QPX_API_KEY
    headers = {'content-type': 'application/json'}
    
    response = requests.post(url, data=json.dumps(params), headers=headers)
    data = response.json()
    
    #price = data['trips']['tripOption'][0]['saleTotal']
    #carrier = data['trips']['tripOption'][0]['slice'][0]['segment'][0]['flight']['carrier']
 
    price = "USD100.20";
    carrier = "placeholder";
    
    concat = hour + ", " + date + ", " +  day_of_week + ", " + price + ", " + carrier + ", " + origin + ", " + destination + ", " + departure_date
    print concat + "    [" + concat + "]"
    myCluster.insertData('tickets', ['hour', 'date', 'day', 'carrier', 'origin', 'destination', 'departure_date', 'price'],
        [hour, date, day_of_week, carrier, origin, destination, departure_date, price[3:]])


############################################## Set-Up ################################################

############################################## SCRIPT ################################################
print "DATA:   Hour, Day-Month-Year, Price, Carrier, Origin, Destination, Date"
print "---------------------------------------------------------------------------------------------"

hour = str(datetime.now().hour)
date = str(datetime.now().day) + "-" + str(datetime.now().month) + "-" + str(datetime.now().year)
day_of_week = datetime.today().weekday()
which_day = days[day_of_week]

writeToCassandra(params_one, hour, date, which_day, ORIGIN_ONE, DESTINATION_ONE, DEPARTURE_DATE, QPX_API_KEY)
writeToCassandra(params_two, hour, date, which_day, ORIGIN_TWO, DESTINATION_TWO, DEPARTURE_DATE, QPX_API_KEY)
writeToCassandra(params_three, hour, date, which_day, ORIGIN_THREE, DESTINATION_THREE, DEPARTURE_DATE, QPX_API_KEY_TWO)
writeToCassandra(params_four, hour, date, which_day, ORIGIN_FOUR, DESTINATION_FOUR, DEPARTURE_DATE, QPX_API_KEY_TWO)

############################################## SCRIPT ################################################








