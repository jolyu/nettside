import random
import json
from datetime import timedelta, datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("data/key.json")

d1 = datetime(2019, 1, 1)
d2 = datetime(2020, 12, 31)


def GenJSON(start, end, deltaMinute):
    current = start
    d = {}
    while current <= end:
        d.update({str(current.timestamp())[:-2]:{
            'time': current.timestamp(),
            'birds': random.randint(1,50),
            'temperature': random.randint(-20, 30), #Lage tilfeldig data
            'wind': random.randint(0,30)
        }})
        current = current + timedelta(minutes=deltaMinute)

    print(len(d))
    return d

#database = firebase_admin.initialize_app(cred)
#ref = db.reference()

data = GenJSON(d1, d2, 5)

#ref.push(data)
#print("Data pushed")


with open("data/data.json", 'w') as outfile:
    json.dump(data, outfile, sort_keys=True, indent=4)