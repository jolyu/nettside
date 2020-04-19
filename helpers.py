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
    if timeDiff > dt.timedelta(weeks=52):
        return DataToMonths(df), "month"
    elif timeDiff > dt.timedelta(weeks=12):
        return DataToWeeks(df), "week"
    elif timeDiff > dt.timedelta(days=4):
        return DataToDays(df), "day"
    else:
        return DataToHours(df), "hour"

def GetFirstLastIndex(df):
    return [df.first_valid_index(), df.last_valid_index()]

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
    dates = [pd.to_datetime(d) for d in dates]
    # try:
    #     dates = [dt.datetime.strptime(d, '%Y-%m-%d %H:%M:%S.%f') for d in dates]
    # except:
    #     try:
    #         dates = [dt.datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in dates]
    #     except:
    #         dates = [dt.datetime.strptime(d, '%Y-%m-%d') for d in dates]
        
    return dates
        

                    

