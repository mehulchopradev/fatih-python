from datetime import date, datetime, timedelta

today = date.today()
print(today)
print(type(today))

print(today.year)
print(today.day)
print(today.month)

past = date(year=1986, month=11, day=25)
print(past)
print(type(past))

future = past.replace(year=today.year)
datestr = future.strftime('%d/%m/%Y')
print(datestr)

print(type(future))

print(today.weekday())

dt = datetime.now()
print(dt)
print(type(dt))

t = dt.time()
print(t)
print(type(t)) # time object

dtpast = datetime(1986, 11, 25, 10, 45)
print(dtpast)

print(dtpast.strftime('%d/%m, %H:%M'))


# one week from now
oneweekdelta = timedelta(weeks=1)
oneweekdate = today + oneweekdelta
print(oneweekdate)
print(type(oneweekdate))


# 30 days (time) for now
thirtydaydelta = timedelta(days=30)
thirtydaydate = dt + thirtydaydelta
print(thirtydaydate)
print(type(thirtydaydate))