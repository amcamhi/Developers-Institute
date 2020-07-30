import sqlite3 as sl  #Builtin python library for connecting to SQLITE Databases


def get_details():
	connection = sl.connect('example.db')  #Make a connection to the database
	cursor = connection.cursor() #Think of the cursor as the place that executes queries

	name = input("What is your name? ")
	pin = input("What is your pin number? ")

	query_result = cursor.execute(f"SELECT * FROM employees WHERE first_name = '{name}' AND pin_number = '{pin}';")  #Cursor runs the query

	connection.commit()  #Finalize the result. "Write" it to the DB

	results = cursor.fetchall() #Fetch theh results back from the cursor into python variable

	connection.close()  #Close the connection

	for item in results:  #Do whatever you want with the results
		print(item)


#TRY name = Adam and pin = ' or '' = '