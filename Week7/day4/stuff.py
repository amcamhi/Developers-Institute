import json

json_file = "my_file.json"

def write_to_json():
	
	my_family = {
		'parents': ['Beth', 'Jerry'],
		'children': ['Summer', 'Morty']
	}

	with open(json_file, 'w') as f:
		json.dump(my_family, f, indent=4, sort_keys=True)



def read_from_json():
	
	with open(json_file, 'r') as f:
		data = json.load(f)

		print(data)



# JSON is for transferring data.
# Its a complex string with brackets, braces and stuff 
# that looks similar to a python dictionary
# You can have it indented to be human readable, but you don't have to.

# Every language can convert its particular structure to JSON
# and every language can convert JSON back to some data structure.

# in python, you have the json module, which you can access by "import json"

# DUMP - Converts to JSON
# LOAD - Converts from JSON

# 4 main functions.

# json.dump  - converts to json and dumps into a file.
# json.dumps - converts to json and returns the json string

# json.load - reads from a json file and converts back to python
# json.loads - reads a json string and converts back to python


