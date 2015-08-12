from cassandra.cluster import Cluster

class FlightTrackerCluster(object):
    def __init__(self):
        cluster = Cluster()
        self.session = cluster.connect()

    def createKeySpace(self, title, class_type='SimpleStrategy', replication_factor='1'):
        self.session.execute("CREATE KEYSPACE {} WITH REPLICATION = \
        {{ 'class' : '{}', 'replication_factor' : {} }};\
        ".format(title, class_type, replication_factor))

    def changeKeySpace(self, newkeyspace='plane'):
        self.session.set_keyspace('{}'.format(newkeyspace))

    def insertData(self, tableName, paramTypes, params):
        for each in range(len(params)):
            params[each] = '\'' + params[each] + '\''        
        parameterTypes = ', '.join(paramTypes)
        parameters = ', '.join(params)
        self.session.execute("INSERT INTO {} ({}) VALUES ({});".format(tableName, parameterTypes, parameters))

    def createTable(self, tableName, params):
        for each in range(len(params)):
            params[each] += ' text'
        params[0] += ' PRIMARY KEY'
        parameters = ', \n'.join(params)
        self.session.execute("CREATE TABLE {} ({});".format(tableName, parameters))

    def deleteTable(self, tableName):
        double_check = raw_input('Are you REALLY sure? Type "Y" to confirm: ')
        if double_check == 'Y':
            self.session.execute("DROP TABLE {};".format(tableName))
        else:
            print "Exiting."

    def selectFromTable(self, value, tableName):
        return self.session.execute("SELECT {} FROM {}".format(value, tableName))

    def getParams(self, origin, destination, departure_date, return_date=None, solutions=5):
        slice = [
            {
              "origin": origin,
              "destination": destination,
              "date": departure_date
            }
        ]

        if return_date == True:
            slice.append({
                    "origin": destination,
                    "destination": origin,
                    "date": return_date
                })
        params = {
            "request": {
                "passengers": {
                    "adultCount": 1
                },
                "solutions": solutions,
                "slice": slice 
                }
            }    
        return params