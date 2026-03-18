import datetime


def display_date_info():
    # ------------------------------
    # 1. Custom date
    # ------------------------------
    custom_date = datetime.date(2024, 2, 12)
    print("📅 Custom Date        :", custom_date)
    print("📌 Day of the week    :", custom_date.strftime("%A"))

    print("-" * 40)

    # ------------------------------
    # 2. Today's date
    # ------------------------------
    today = datetime.date.today()
    print("📅 Today's Date       :", today)
    print("📌 Day of the week    :", today.strftime("%A"))

    print("-" * 40)


def display_current_datetime():
    # ------------------------------
    # 3. Current date and time
    # ------------------------------
    now = datetime.datetime.now()
    formatted = now.strftime("%H:%M:%S , %d-%m-%Y")

    print("⏰ Current Date & Time:", formatted)
    print("-" * 40)

    return now


def analyze_target(now):
    # ------------------------------
    # 4. Target date
    # ------------------------------
    target = datetime.datetime(2030, 1, 2, 12, 30, 1)

    print("🎯 Target Date & Time :", target)
    print("📌 Target Day         :", target.strftime("%A"))

    print("-" * 40)

    # ------------------------------
    # 5. Comparison
    # ------------------------------
    if target < now:
        print("❌ Target date has already passed.")
    else:
        print("✅ Target date is in the future.")

    # ------------------------------
    # 6. Time difference
    # ------------------------------
    diff = target - now

    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60

    print("-" * 40)
    print("⏳ Time Remaining:")
    print(f"Days   : {days}")
    print(f"Hours  : {hours}")
    print(f"Minutes: {minutes}")


# ------------------------------
# MAIN PROGRAM
# ------------------------------
if __name__ == "__main__":
    display_date_info()
    current_time = display_current_datetime()
    analyze_target(current_time)
