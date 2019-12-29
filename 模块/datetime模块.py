import datetime
import time
import calendar

a = datetime.datetime.now()
print(a)

# 日期转星期函数
trans_weekday = lambda datastring:calendar.day_name[datetime.datetime.strptime(datastring, '%Y/%m/%d').weekday()]
str = '2019/12/22'
b = trans_weekday(str)

print(b)