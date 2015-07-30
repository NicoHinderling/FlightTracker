from cassandra.cluster import Cluster
import dbcommands

######## Available Commands ########
#
# createKeySpace(session, title, opt: class_type, opt: rep. factor) - Create a keyspace
#
# insertInto(session, table_name, parameters, values)
#
# 


#initialize Cluster
cluster = Cluster()
session = cluster.connect()
session.set_keyspace('plane')


# session.execute("""
#   CREATE TABLE users (
#     id text PRIMARY KEY,
#     age int,
#     state text
# );
# """)

#session.execute("INSERT INTO users JSON '{"id": "user123", "age": 42, "state": "TX"}';  ")
session.execute("INSERT INTO users (id, age, state) VALUES ('user123', 42, 'TX');")
# result = session.execute("SELECT * FROM users WHERE lastname='Jones' ")[0]
# print result.firstname, result.age

session.execute("SELECT id FROM users")