import datetime as dt
import pandas as pd
import math


def DataToMonths(data):
    df = data.resample('M').sum()
    return(df)

def DataToDays(df):
    df = df.resample('D').sum()
    return(df)

def SumOfBirds(df, countKey):
    total = 0
    for index, row in df.iterrows():
        total += row[countKey]
    return total

def TimeSliderToDate(tS):
    times = []
    for i in tS:
        year = math.floor(i)
        month = round((i - year) * 12)
        times.append(dt.datetime(year, month + 1, 1))
    return times

def FilterData(df, startDate, endDate):
    dff = df.loc[(df.index > startDate)
        & (df.index < endDate)]
    return dff

def TotalSelBirds(df, timeSlider):
    times = TimeSliderToDate(timeSlider)
    dff = FilterData(df, times[0], times[1])
    total = 0
    for i in dff["birds"]:
        # print(i)
        total += i
    return total

def AverageBirdDay(df, timeSlider):
    times = TimeSliderToDate(timeSlider)
    dff = FilterData(df, times[0], times[1])
    dff = DataToDays(dff)
    total, count = 0,0
    for i in dff["birds"]:
        total += i
        count += 1
    return round(total/count,1)

def DaySelectorString(dates):
    dates = [d.replace("T", " ") for d in dates]
    #dates = [pd.to_datetime(d) for d in dates]
    try:
        dates = [dt.datetime.strptime(d, '%Y-%m-%d %H:%M:%S.%f') for d in dates]
    except:
        dates = [dt.datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in dates]
    return dates

def DayAverage(df):
    head = list(df.head())
    d = {}
    days = 1
    lastDay = [0,0,0]
    for index, row in df.iterrows():
        day = [row["dates"].year,row["dates"].month,row["dates"].day]
        if lastDay[0] < day[0] or lastDay[1] < day[1] or lastDay[2] < day[2]:
            days += 1
            lastDay = day
        hour = row["dates"].hour
        minute = row["dates"].minute
        if hour not in d:
            d[hour] = {}
        if minute not in d[hour]:
            d[hour][minute] = {}
        for col in head[1:]:
            if col not in d[hour][minute]:
                d[hour][minute][col] = 0
            d[hour][minute][col] += row[col]
    for h in d:
        for m in d[h]:
            for c in d[h][m]:
                d[h][m][c] *= 1

    #print(d)
        
def HourAverage(df):
    df = df.resample('H').sum()
    return(df)
                    

