import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import json

from datetime import timedelta, datetime

cred = credentials.Certificate("data/key.json")

firebase_admin.initialize_app(cred, dict(
    databaseURL = 'https://jolyu-ntnu.firebaseio.com/'
))
ref = db.reference()

first = ref.order_by_child('time').limit_to_first(1).get()
last = ref.order_by_child('time').limit_to_last(1).get()
firstDate = datetime.fromtimestamp(int(next(iter(first.keys()))))
lastDate = datetime.fromtimestamp(int(next(iter(last.keys()))))


results = ref.order_by_child('time').start_at(datetime(2020,1,1).timestamp()).end_at(datetime(2020,1,2).timestamp()).get()



print(firstDate, lastDate)

print(json.dumps(results[next(iter(results.keys()))], indent=4))