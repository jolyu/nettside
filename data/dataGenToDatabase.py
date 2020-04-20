import random
import json
from datetime import timedelta, datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import math

cred = credentials.Certificate("data/key.json")

d1 = datetime(2020, 1, 1)
d2 = datetime(2021, 1, 1)


def GenJSON(start, end, deltaMinute):
    current = start
    d = {}
    while current <= end:
        d.update({str(current.timestamp())[:-2]:{
            'time': current.timestamp(),
            'birds': GenRandomSin(current.timestamp(), 2, 2, 5, 6, 5, True, 0),
            'temperature': - GenRandomSin(current.timestamp(), 1, 1,10,0,-5,False, 1), #Lage tilfeldig data
            'wind': GenRandomSin(current.timestamp(), 5,1,5,0,5,True, 1)
        }})
        current = current + timedelta(minutes=deltaMinute)

    print(len(d))
    return d

def GenRandomSin(time, periods, rand, amplitude, delayHour, centerline, removeUnder0, roundNr):
    """ Generates a sinus with random values added, with a amplitude and delay, periods per day"""
    value = amplitude * math.sin((((time * periods)/ 86400)  * 2 * math.pi) - (delayHour * 3600)) + centerline + random.randint(-rand, rand)
    if removeUnder0:
        value = max(0, value)
        
    value = round(value, roundNr)
    return value
#database = firebase_admin.initialize_app(cred)
#ref = db.reference()

data = GenJSON(d1, d2, 5)

#ref.push(data)
#print("Data pushed")


with open("data/data.json", 'w') as outfile:
    json.dump(data, outfile, sort_keys=True, indent=4)