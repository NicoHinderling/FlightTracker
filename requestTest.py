import json
import requests
import credentials

api_key = credentials.QPX
url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=' + api_key
headers = {'content-type': 'application/json'}

##############################
######### Parameters #########
origin = "BOS"
destination = "LAX"
departure_date = "2015-10-26"
return_date = "2015-11-29"
##############################
##############################

params = getParams(origin, destination, departure_date, return_date, 100)

response = requests.post(url, data=json.dumps(params), headers=headers)
data = response.json()

for index in range(len(data['trips']['tripOption'])):
    print data['trips']['tripOption'][index]['saleTotal']
    print data['trips']['tripOption'][index]['slice'][0]['segment'][0]['flight']['carrier']
    print "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"

# with open('datb.txt', 'w') as outfile:
#     json.dump(data, outfile, indent=4)
# print data

# """
#   CREATE TABLE {} (
#     id text PRIMARY KEY,
#     age int,
#     state text
# );
# """

# tableData = ['id text PRIMARY KEY', 'age int', 'state text']
# newTableData = ['id', 'age', 'state']


# cluster.selectFromTable('id', 'user')
# cluster.insertData('user', ['id', 'age', 'state'], ['user1234', '42', 'TX'])

######## Available Commands ########
#
# createKeySpace(session, title, opt: class_type, opt: rep. factor) - Create a keyspace
#
# insertInto(session, table_name, parameters, values)
#
# 


#initialize Cluster


# session.execute("""
#   CREATE TABLE users (
#     id text PRIMARY KEY,
#     age text,
#     state text
# );
# """)

#session.execute("INSERT INTO users JSON '{"id": "user123", "age": 42, "state": "TX"}';  ")
# session.execute("INSERT INTO users (id, age, state) VALUES ('user123', '42', 'TX');")
# result = session.execute("SELECT * FROM users WHERE lastname='Jones' ")[0]
# print result.firstname, result.age

# session.execute("SELECT id FROM users")

# import json
 
# prepared = session.prepare('INSERT INTO users JSON ?')
 
# while True:
#     user = {'id': get_username(user_input),
#             'age': get_age(user_input),
#             'state': get_state(user_input) or 'TX'}
 
#     session.execute(prepared, [json.dumps(user)])