import time
import datetime


def set_alarm(alarm_time_str):
    try:
        # Convert input string to time object
        alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M:%S").time()
    except ValueError:
        print("❌ Invalid time format! Please use HH:MM:SS")
        return

    print(f"\n⏰ Alarm set for {alarm_time}")
    print("Waiting...\n")

    while True:
        now = datetime.datetime.now()
        current_time = now.time()

        # Check if current time >= alarm time
        if current_time >= alarm_time:
            print("\n🔔 Wake up! Alarm ringing 🔔")
            break

        # Print every 5 seconds instead of every second
        print("Current time:", now.strftime("%H:%M:%S"))
        time.sleep(5)


# ---------------------------------------
# MAIN PROGRAM
# ---------------------------------------
if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
