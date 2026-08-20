import datetime


def display_date_info():
    custom_date = datetime.date(2024, 2, 12)

    print("Custom Date:", custom_date)
    print("Day:", custom_date.strftime("%A"))

    print("-" * 40)

    today = datetime.date.today()

    print("Today's Date:", today)
    print("Day:", today.strftime("%A"))

    print("-" * 40)


def display_current_datetime():
    now = datetime.datetime.now()

    print("Current Date and Time:",
          now.strftime("%H:%M:%S, %d-%m-%Y"))

    print("-" * 40)

    return now


def analyze_target(now):
    target = datetime.datetime(2030, 1, 2, 12, 30, 1)

    print("Target Date and Time:", target)
    print("Target Day:", target.strftime("%A"))

    print("-" * 40)

    if target < now:
        print("Target date has already passed.")
    else:
        print("Target date is in the future.")

    difference = target - now

    days = difference.days
    hours = difference.seconds // 3600
    minutes = (difference.seconds % 3600) // 60

    print("-" * 40)
    print("Time Remaining:")
    print("Days:", days)
    print("Hours:", hours)
    print("Minutes:", minutes)


# Main program
if __name__ == "__main__":
    display_date_info()

    current_time = display_current_datetime()

    analyze_target(current_time)
