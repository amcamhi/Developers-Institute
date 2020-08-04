import json

# sampleJson = """{
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payble":{
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# data = json.loads(sampleJson)

# print(data['company']['employee']['payble']['salary'])


sampleJson = {"id": 1, "name": "value2", "age": 29}

# Expected Output:

# {
#     "age": 29,
#     "id": 1,
#     "name": "value2"
# }

data = sampleJson

json_file = 'my_file.json'
with open(json_file, 'w') as file_obj:
    json.dump(data, file_obj, indent=2, sort_keys=True)


with open(json_file, 'r') as file_obj:
    sampleJson = json.load(file_obj)

print(sampleJson)
