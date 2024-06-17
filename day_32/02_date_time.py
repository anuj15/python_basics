import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
print(year, month, day, day_of_week, now)
