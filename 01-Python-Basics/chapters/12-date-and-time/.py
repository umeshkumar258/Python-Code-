import time
import datetime


def set_alarm(alarm_time):
    print(f"\n⏰ Alarm set for {alarm_time}")
    print("Waiting...\n")

    while True:
        # Get current time in HH:MM:SS format
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current time:", current_time)

        # Check alarm
        if current_time == alarm_time:
            print("\n🔔 Wake up! Alarm ringing 🔔")
            break

        time.sleep(1)  # wait for 1 second


# ---------------------------------------
# MAIN PROGRAM
# ---------------------------------------
if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
