from datetime import datetime,timedelta
# print today's date
today = datetime.now()
oneday_delta = timedelta(days=1)
print(f"Today is {today}")

# print yesterday's date
yesterday = today - oneday_delta
print(f"Yesterday was: {yesterday}")
# ask a user to enter a date
user_day = input("请输入一个你期望的日期，格式：DD/MM/YYYY:")
user_day_datetime_format = datetime.strptime(user_day,"%d/%m/%Y")
#print(f"你输入的日期为 {user_day_datetime_format}")
print(f"你输入的日期为: {user_day_datetime_format.year}年{user_day_datetime_format.month}月{user_day_datetime_format.day}日")
# print the date one week from the date entered
one_week_delta = timedelta(weeks=1)
#one_week_pass_user_day = user_day_datetime_format - one_week_delta
print(f"上周同一时间为：{user_day_datetime_format - one_week_delta}")
days_user_delta = int(input("输入你希望往前回溯的天数："))
days_user_delta_datetime_format = timedelta(days=days_user_delta)

print(f"从你输入的日期回溯{days_user_delta}天，日期为{user_day_datetime_format - days_user_delta_datetime_format}")