import datetime

date = datetime.date(2024,2,12)
print(date)


today = datetime.date.today()    # this only for date
print(today)

now = datetime.datetime.now()  # this only for time

now = now.strftime("%H : %M: %S ,  %d :%m : %y")

target_datetime = datetime.datetime(2030,1,2, 12,30,1)
current_datetime = datetime.datetime.now()


if target_datetime < current_datetime:
    print("Target date has passed")

else:
    print("Target is not passed")
