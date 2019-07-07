import datetime

today=datetime.date.today()
print(today.year)
print(today.month)
print(today.day)


print(datetime.date.min)
print(datetime.date.max)


d1=datetime.date(2019,8,15)
d2=d1.replace(year=1947)
print(d1-d2)
