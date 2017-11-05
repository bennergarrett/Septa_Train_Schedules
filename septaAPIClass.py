import requests
import json
import string
#Septa API website
#http://www3.septa.org/hackathon/
septa_API = "http://www3.septa.org/hackathon/Arrivals"
stationID = 90815
numTrains = 5 #number of scheduled results
parameters = {"req1": stationID, "req2": numTrains} #req1 = Septa train station code / req2 number of results
direction = 1 # 0 for north / 1 for south
traintime = 1 # temp, used to parse out train schedules from numTrains (can only go up to numTrains)
class Septa(object):
    def traintimes(self,septa_API, parameters, direction, traintime):
        response = requests.get(septa_API, params=parameters)
        #print(response.content)

        trainTimes = response.json()
        #print(response.content)
        #print(trainTimes)

        for key, value in trainTimes.items():
            key1 = key
            #print(key1)
        final = (trainTimes[key1][direction])
        print(final) #null values for next station

        #print("\n\n\n\n")
        for key2, value in final.items():
            key3 = key2
            #print("\n\nkey3: ")
            #print(key3)
        #print(final[key3])
        #final[key3].replace(None, "NANANANANANA")


        sort = (json.dumps(final[key3], sort_keys=True, indent=4))
        #print(sort)
        #print sort #next station: becomes null
        s = sort.strip('[]')
        trains = s.split('{')
        fullschedule = (trains[traintime])
        print(a)
        return(fullschedule.split('"')[1::2]) # the [1::2] is a slicing which extracts odd values


if (direction ==1):
    direc = "Southbound"
else:
    direc = "Northbound"


x = Septa()
y = x.traintimes(septa_API, parameters, direction, traintime)
z = x.traintimes(septa_API, parameters, direction, 2)
print("\n\n\n" + direc)
print("----------------")
trainline = y[7]
destination = y[3]
depart = y[1][11:16]
status = y[22]
filtered = (trainline, destination, depart, status)
print("line: " + filtered[0])
print("Destination: " + filtered[1])
print("Depature: " + filtered[2])
print("Status: " + filtered[3])
#strings = y
#strings = strings.replace("LOCAL", "NANANANAAN")
#print("________________\n")
#print(strings)

print("----------------")
trainline = z[7]
destination = z[3]
depart = z[1][11:16]
status = z[21]
filtered2 = (trainline, destination, depart, status)
print("line: " + filtered2[0])
print("Destination: " + filtered2[1])
print("Depature: " + filtered2[2])
print("Status: " + filtered2[3])

print("\n\n\n")
