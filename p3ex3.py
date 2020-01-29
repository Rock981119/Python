#-*-coding:utf-8-*-
from datetime import datetime,timedelta

today = datetime.now()
print(f"Today is: {today}")
oneday_pass = timedelta(1)
yesterday = today - oneday_pass
print(f"Yesterday was: {yesterday}")

oneweek_pass = timedelta(weeks=1)
last_week = today - oneweek_pass
try:
    print("Last week is: " + last_week)
except TypeError as error1:
    print(f"类型错误 {error1}")
else:
    print("1")
finally:
    print("现在我们把错误的值赋予成字符串")
    print(f"Last week is: {last_week}")
   