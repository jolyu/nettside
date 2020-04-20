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



#############################
#############################
##### Sort into periods #####
#############################
#############################

def DataToMonths(df):
    """ Sort data in dataframe into months """
    df = df.resample('M').sum()
    return df


def DataToWeeks(df):
    """ Sort data in dataframe into weeks """
    df = df.resample('W').sum()
    return df


def DataToDays(df):
    """ Sort data in dataframe into days """
    df = df.resample('D').sum()
    return df


def DataToHours(df):
    """ Sort data in dataframe into hours """
    df = df.resample('H').sum()
    return df


def DataToTimescale(df):
    """ Finds the appropriate timescale for a given dataframe """
    # Get the first and last valid index in dataframe
    firstAndLast = GetFirstLastIndex(df)
    # Get the timedifference
    timeDiff = firstAndLast[1] - firstAndLast[0]

    # Return the sorted dataframe and the used method
    if timeDiff > dt.timedelta(weeks=51):
        return DataToMonths(df), "month"
    elif timeDiff > dt.timedelta(weeks=11):
        return DataToWeeks(df), "week"
    elif timeDiff > dt.timedelta(days=6):
        return DataToDays(df), "day"
    else:
        return DataToHours(df), "hour"



#########################
#########################
##### Other helpers #####
#########################
#########################

def GetFirstLastIndex(df):
    """ Gets the first and last valid index in a given dataframe """
    return [df.first_valid_index(), df.last_valid_index()]

def FilterData(df, startDate, endDate):
    """ Filter out a partition of a dataframe """
    dff = df.loc[(df.index > startDate)
        & (df.index < endDate)]
    return dff

        

                    

