

month = (0,31,59,90,120,151,181,212,243,273,304,334)

y = int(input("year:"))
m = int(input("month:"))
d = int(input("day:"))
num_day = d
if 0 < m <= 12:
    num_day+=month[m-1]

if m>=3 and ((y%4==0 and y%100!=0) or (y%400==0)):
    num_day+=1

print(num_day)