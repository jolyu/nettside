import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from datetime import datetime, timedelta
import pandas as pd


def GetDbRef():
    """ Gets a database reference for the whole site. Can oly be one ref"""
    cred = credentials.Certificate("data/key.json")

    firebase_admin.initialize_app(cred, dict(
        databaseURL = 'https://jolyu-ntnu.firebaseio.com/'
    ))

    # Create the actual reference
    return db.reference()


def GetFirstAndLastDate(dbRef):
    """ Gets the first and last valid dates in the database """ 
    first = dbRef.order_by_child('time').limit_to_first(1).get()
    last = dbRef.order_by_child('time').limit_to_last(1).get()

    # Translate into datetimes
    firstDate = datetime.fromtimestamp(int(next(iter(first.keys()))))
    lastDate = datetime.fromtimestamp(int(next(iter(last.keys()))))

    return [firstDate, lastDate]


def GetDataJSON(dbRef, dates):
    """ Query the database with start and end dates. Can take a long time """
    return dbRef.order_by_child('time').start_at(dates[0].timestamp()).end_at(dates[1].timestamp()).get()


def GetDataDF(dbRef, dates):
    """ Query the database and create a dataframe from the JSON returned. Can take a long time """
    # The actual query
    data = GetDataJSON(dbRef, dates)

    # Create dataframe from json with the json-keys as index
    df = pd.DataFrame.from_dict(data, orient='index')
    # Remove the time column as this is only used to search in the database
    df = df.drop(columns='time')
    # Parse dataframe indexes to datetime objects
    df.index = pd.to_datetime(df.index, unit='s')
    return df


def GetInitialDates(dbRef, days):
    """ Returns the initial days, the last days of the database """
    # Query to get the last day
    dates = GetFirstAndLastDate(dbRef)
    # Check if the database has more dates than the initial days
    if dates[1] - dates[0] > timedelta(days=days):
        return [dates[1] - timedelta(days=days), dates[1]]
    else:
        return dates
    