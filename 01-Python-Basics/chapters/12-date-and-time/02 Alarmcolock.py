import time
import datetime


def set_alarm(alarm_time_str):
    try:
        # Convert string to time object
        alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M:%S").time()
    except ValueError:
        print("❌ Invalid format! Use HH:MM:SS")
        return

    print(f"\n⏰ Alarm set for {alarm_time}")
    print("Waiting for alarm...\n")

    while True:
        now = datetime.datetime.now()
        current_time = now.time()

        print("Current Time:", now.strftime("%H:%M:%S"))

        # Better condition (not exact match)
        if current_time >= alarm_time:
            print("\n🔔 WAKE UP! Alarm ringing 🔔")
            break

        time.sleep(1)


# Main program
if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
