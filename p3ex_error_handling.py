from datetime import datetime,timedelta
user_birthday = input("输入你的生日，以格式（DD/MM/YYYY）>")

try:
    user_birthday_datetime_format = datetime.strptime(user_birthday,"%d/%m/%Y")
except ValueError as error1:
    print("错误的日期格式")
    
else:
    print(f"你的生日是：{user_birthday_datetime_format.year}年{user_birthday_datetime_format.month}月{user_birthday_datetime_format.day}日")
