import sqlite3 as sl  #Builtin python library for connecting to SQLITE Databases

connection = sl.connect('example.db')  #Make a connection to the database

cursor = connection.cursor() #Think of the cursor as the place that executes queries

query = input("What is your query? ")

query_result = cursor.execute(f'{query}')  #Cursor runs the query

connection.commit()  #Finalize the result. "Write" it to the DB

results = cursor.fetchall() #Fetch theh results back from the cursor into python variable

connection.close()  #Close the connection

for item in results:  #Do whatever you want with the results
	print(item)

