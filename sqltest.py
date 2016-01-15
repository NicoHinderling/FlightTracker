import MySQLdb
from env_variables import password

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd=password,	  # your password
                     db="plane")          # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

cur.execute("INSERT INTO plane.ticketOne (query_id, origin,day,date,destination,price,hour,carrier,departure_date) VALUES (102, 'peenwik', '14-1-2016', 'my ass', 'destination', 10, '10', 'suckme', 'ok');");

# Use all the SQL you like
cur.execute("SELECT * FROM ticketOne")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row




db.close()
