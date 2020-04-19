#####################################################################
#####################################################################
#####                                                           #####
#####  db   db d88888b db      d8888b. d88888b d8888b. .d8888.  #####
#####  88   88 88'     88      88  `8D 88'     88  `8D 88'  YP  #####
#####  88ooo88 88ooooo 88      88oodD' 88ooooo 88oobY' `8bo.    #####
#####  88~~~88 88~~~~~ 88      88~~~   88~~~~~ 88`8b     `Y8b.  #####
#####  88   88 88.     88booo. 88      88.     88 `88. db   8D  #####
#####  YP   YP Y88888P Y88888P 88      Y88888P 88   YD `8888Y'  #####
#####                                                           #####
#####################################################################
#####################################################################

import datetime as dt
import pandas as pd
import math

def DataToMonths(data):
    df = data.resample('M').sum()
    return(df)

def DataToWeeks(data):
    df = data.resample('W').sum()
    return(df)

def DataToDays(df):
    df = df.resample('D').sum()
    return(df)

def DataToHours(df):
    df = df.resample('H').sum()
    return(df)

def DataToTimescale(df):
    firstAndLast = GetFirstLastIndex(df)
    timeDiff = firstAndLast[1] - firstAndLast[0]
    if timeDiff > dt.timedelta(weeks=51):
        return DataToMonths(df), "month"
    elif timeDiff > dt.timedelta(weeks=11):
        return DataToWeeks(df), "week"
    elif timeDiff > dt.timedelta(days=6):
        return DataToDays(df), "day"
    else:
        return DataToHours(df), "hour"

def GetFirstLastIndex(df):
    return [df.first_valid_index(), df.last_valid_index()]

def FilterData(df, startDate, endDate):
    dff = df.loc[(df.index > startDate)
        & (df.index < endDate)]
    return dff

        

                    

