import time
import datetime


def set_alarm(alarm_time):
    print(f"\n⏰ Alarm set for {alarm_time}")
    print("Waiting for alarm...\n")

    while True:
        # Get current time in HH:MM:SS format
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current Time:", current_time)

        # Check if alarm time matches current time
        if current_time == alarm_time:
            print("\n🔔 WAKE UP! Alarm ringing 🔔")
            break

        time.sleep(1)   # wait for 1 second


# Main program
if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
