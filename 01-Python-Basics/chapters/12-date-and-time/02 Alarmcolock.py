import time
import datetime


def set_alarm(alarm_time):
    try:
        alarm = datetime.datetime.strptime(alarm_time, "%H:%M:%S").time()
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS")
        return

    print("Alarm set for:", alarm)
    print("Waiting for alarm...")

    while True:
        current = datetime.datetime.now()

        print("Current Time:", current.strftime("%H:%M:%S"))

        if current.time() >= alarm:
            print("Alarm ringing! Wake up!")
            break

        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
