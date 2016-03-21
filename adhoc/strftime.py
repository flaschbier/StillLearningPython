from datetime import datetime, timedelta
a = datetime.now() # <== 2016-03-09 11:06:04.824047
print a
print a.strftime("%U")
# >>> 10

#go back to previous Sunday
b = a - timedelta(days = 3)

print b.strftime("%U")
# >>> 10
print b.weekday()
# >>> 6
