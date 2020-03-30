import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from datetime import datetime
import pandas as pd


def GetDbRef():
    cred = credentials.Certificate("data/key.json")

    firebase_admin.initialize_app(cred, dict(
        databaseURL = 'https://jolyu-ntnu.firebaseio.com/'
    ))
    ref = db.reference()

    return ref

def GetFirstAndLastDate(dbRef):
    first = dbRef.order_by_child('time').limit_to_first(1).get()
    last = dbRef.order_by_child('time').limit_to_last(1).get()

    firstDate = datetime.fromtimestamp(int(next(iter(first.keys()))))
    lastDate = datetime.fromtimestamp(int(next(iter(last.keys()))))

    return [firstDate, lastDate]

def GetDataJSON(dbRef, dates):
    return dbRef.order_by_child('time').start_at(dates[0].timestamp()).end_at(dates[1].timestamp()).get()

def GetDataDF(dbRef, dates):
    data = GetDataJSON(dbRef, dates)
    df = pd.DataFrame.from_dict(data, orient='index')
    df = df.drop(columns='time')
    df.index = pd.to_datetime(df.index, unit='s')
    return df