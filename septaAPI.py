import requests
import json
from datetime import datetime
time = datetime.now().strftime('%B %d, %Y, %I:%M %p')

parameters = {"req1": 90815, "req2": 3}
response = requests.get("http://www3.septa.org/hackathon/Arrivals", params=parameters)


#print(response.status_code)
#print(response.content)
data = response.json()
print(data)
#print(json.dumps(data, sort_keys=True, indent=4))
for key, value in data.items():
    key1 = key

#    print("key: ")
    print(key1)
#print list(data[key1][1])
#direction = (data[key1][1])
#for train in data[key1]:
#    print("\n\n\n")
#    print("train")
#    print(train)
#print("\n\n\n\n -------------")
#print("test:")
#print(data[key1][1])
final = (data[key1][0])
print(json.dumps(final, sort_keys=True, indent=4))
#print(response.content)
