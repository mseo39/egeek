from datetime import datetime
import calendar

days=[]
c= calendar.TextCalendar(calendar.SUNDAY)

for i in c.itermonthdays(datetime.today().year,datetime.today().month):
    if i==0:
        days.append([" ","disable"])
    else:
        days.append([i," "])
print(days)
