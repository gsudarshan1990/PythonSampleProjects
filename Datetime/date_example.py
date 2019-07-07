import datetime

today=datetime.date.today()

print(today)


print(today.year)
print(today.month)
print(today.day)


user_date=datetime.date(2019,7,8)
print(user_date)

print(datetime.date.min)
print(datetime.date.max)


d1=datetime.date(2019,6,1)
d2=d1.replace(year=1990)
print(d1-d2)
