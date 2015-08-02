from cassandra.cluster import Cluster #Check if necessary
from db_commands import FlightTrackerCluster

######## Available Commands ########
#
# createKeySpace(session, title, opt: class_type, opt: rep. factor) - Create a keyspace
#
# insertInto(session, table_name, parameters, values)
#
# 


#initialize Cluster
cluster = FlightTrackerCluster()


# session.execute("""
#   CREATE TABLE users (
#     id text PRIMARY KEY,
#     age text,
#     state text
# );
# """)

#session.execute("INSERT INTO users JSON '{"id": "user123", "age": 42, "state": "TX"}';  ")
session.execute("INSERT INTO users (id, age, state) VALUES ('user123', '42', 'TX');")
# result = session.execute("SELECT * FROM users WHERE lastname='Jones' ")[0]
# print result.firstname, result.age

session.execute("SELECT id FROM users")

# import json
 
# prepared = session.prepare('INSERT INTO users JSON ?')
 
# while True:
#     user = {'id': get_username(user_input),
#             'age': get_age(user_input),
#             'state': get_state(user_input) or 'TX'}
 
#     session.execute(prepared, [json.dumps(user)])