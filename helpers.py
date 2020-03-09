import datetime as dt
import pandas as pd
import math


def DataToMonths(data):
    head = list(data.head())
    d = {}
    for index, row in data.iterrows():
        year = row[head[0]].year
        month = row[head[0]].month
        if year not in d:
            d[year] = {}
        if month not in d[year]:
            d[year][month] = {}
        d[year][month][head[0]] = dt.datetime(year, month)
        for col in head[1:]:
            if col not in d[year][month]:
                d[year][month][col] = 0
            d[year][month][col] += row[col]
    l = []
    for y in d:
        for m in d[y]:
            ll = []
            for col in d[y][m]:
                ll.append(d[y][m][col])
            l.append(ll)
    df = pd.DataFrame(l, columns=list(data.head()))
    return(df)

def DataToDays(df):
    head = list(df.head())
    d = {}
    for index, row in df.iterrows():
        year = row[head[0]].year
        month = row[head[0]].month
        day = row[head[0]].day
        if year not in d:
            d[year] = {}
        if month not in d[year]:
            d[year][month] = {}
        if day not in d[year][month]:
            d[year][month][day] = {}
        d[year][month][day][head[0]] = dt.datetime(year, month, day)
        for col in head[1:]:
            if col not in d[year][month][day]:
                d[year][month][day][col] = 0
            d[year][month][day][col] += row[col]
    l = []
    for y in d:
        for m in d[y]:
            for day in d[y][m]:
                ll = []
                for col in d[y][m][day]:
                    ll.append(d[y][m][day][col])
                l.append(ll)
    df = pd.DataFrame(l, columns=list(df.head()))
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
        times.append(dt.datetime.strptime(str(year) + "-" + str(month + 1), '%Y-%m'))
    return times

def FilterData(df, startDate, endDate):
    dff = df[
        (df["dates"] > startDate)
        & (df["dates"] < endDate)
    ]
    return dff

def TotalSelBirds(df, timeSlider):
    times = TimeSliderToDate(timeSlider)
    dff = FilterData(df, times[0], times[1])
    total = 0
    #print(dff)
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
    head = list(df.head())
    d = {}
    rows = 0
    for index, row in df.iterrows():
        year = row["dates"].year
        month = row["dates"].month
        day = row["dates"].day
        hour = row["dates"].hour
        #print(year, month, day, hour)
        if year not in d:
            d[year] = {}
        if month not in d[year]:
            d[year][month] = {}
        if day not in d[year][month]:
            d[year][month][day] = {}
        if hour not in d[year][month][day]:
            rows = 0
            d[year][month][day][hour] = {}
        d[year][month][day][hour][head[0]] = dt.datetime(year, month, day, hour)
        for col in head[1:]:
            rows += 1
            if col not in d[year][month][day][hour]:
                d[year][month][day][hour][col] = 0
            d[year][month][day][hour][col] += row[col]
        """ keys = d[year][month][day][hour].keys()
        for k in keys[1:]:
            k *= 1/rows """
    l = []
    for y in d:
        for m in d[y]:
            for day in d[y][m]:
                for h in d[y][m][day]:
                    ll = []
                    for col in d[y][m][day][h]:
                        ll.append(d[y][m][day][h][col])
                    l.append(ll)
    print(l)
    df = pd.DataFrame(l, columns=list(df.head()))
    print(df)
    return(df)
                    

