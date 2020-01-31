from random import randrange, randint
from datetime import timedelta
import csv

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)
#print(probs)

from datetime import datetime

d1 = datetime.strptime('2020/1/1 01:30:00', '%Y/%m/%d %H:%M:%S')
d2 = datetime.strptime('2021/1/1 01:30:00', '%Y/%m/%d %H:%M:%S')

dates = []

for i in range(100000):
    date = [random_date(d1,d2).strftime('%Y/%m/%d %H:%M:%S')]
    date.append(randint(0,10))
    dates.append(date)
    """else:
        print(str(i) + ' false')"""

print(dates)

dates.sort()

with open("data/data.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(dates)
#print(dates)
print(len(dates))