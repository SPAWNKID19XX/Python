import json
import requests

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

json_str = json.dumps(data, indent=4)
print("Type var data:", type(data))
print("Total persons: ",data['number'])

#print(json_str)
for obj in data['people']:
    print("Name:{:>20}, Possition:{:>12}".format(obj['name'], obj['craft']))
