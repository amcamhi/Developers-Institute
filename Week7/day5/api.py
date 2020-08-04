import requests

response = requests.get("http://api.open-notify.org/astros.json")
# Print the content of the response (the data the server returned)
data = response.json()
print(data)
