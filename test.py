from datetime import datetime
import calendar

days=[]
c= calendar.TextCalendar(calendar.SUNDAY)
for i in c.itermonthdays(datetime.today().year,datetime.today().month):
    days.append(i)

disable=["" for i in range(len(days))]
for i in range(0,len(days)):
    if days[i] ==0:
        disable[i]="disabled"
print(disable)
