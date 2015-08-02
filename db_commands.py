from cassandra.cluster import Cluster
# from db_commands_helpers import 

class FlightTrackerCluster(object):
    def __init__(self):
        cluster = Cluster()
        self.session = cluster.connect()

    def createKeySpace(self, title, class_type='SimpleStrategy', replication_factor='3'):
        self.session.execute("CREATE KEYSPACE {} \
        WITH REPLICATION = { 'class' : '{}', 'replication_factor' : {} };\
        ".format(title, class_type, replication_factor))

    def changeKeySpace(self, newkeyspace='plane'):
        self.session.set_keyspace('{}'.format(newkeyspace))

    def insertData(self, tableName, paramTypes, params):
        parameterTypes = ', \n'.join(paramTypes)
        parameters = ', \n'.join(params)
        self.session.execute("INSERT INTO {} ({}) VALUES ({});".format(tableName, parameterTypes, parameters))

    def createTable(self, tableName, params):
        for each in params:
            each += '  text'
        params[0] += ' PRIMARY KEY'
        parameters = ', \n'.join(params)

        self.session.execute("CREATE TABLE {} ({});".format(tableName, parameters))

    def selectFromTable(self, value, tableName):
        self.session.execute("SELECT {} FROM {}".format(value, tableName))
