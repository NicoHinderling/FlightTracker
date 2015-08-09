from db_commands import FlightTrackerCluster

myCluster = FlightTrackerCluster()
myCluster.changeKeySpace('plane')
first = raw_input('Are you sure you want to delete the table "tickets"? Type "Y" to confirm: ')
if first == 'Y':
    myCluster.deleteTable('tickets')