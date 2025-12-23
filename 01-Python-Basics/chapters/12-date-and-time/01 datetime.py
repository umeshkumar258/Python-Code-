import datetime

# ------------------------------
# 1. Create a specific date
# ------------------------------
custom_date = datetime.date(2024, 2, 12)
print("Custom Date        :", custom_date)
print("Day of the week    :", custom_date.strftime("%A"))

print("-" * 40)

# ------------------------------
# 2. Get today's date
# ------------------------------
today = datetime.date.today()   # only date
print("Today's Date       :", today)
print("Day of the week    :", today.strftime("%A"))

print("-" * 40)

# ------------------------------
# 3. Get current date and time
# ------------------------------
current_datetime = datetime.datetime.now()   # date + time

formatted_now = current_datetime.strftime(
    "%H:%M:%S , %d-%m-%Y"
)

print("Current Date & Time:", formatted_now)

print("-" * 40)

# ------------------------------
# 4. Target date and time
# ------------------------------
target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)

print("Target Date & Time :", target_datetime)
print("Target Day         :", target_datetime.strftime("%A"))

print("-" * 40)

# ------------------------------
# 5. Compare dates
# ------------------------------
if target_datetime < current_datetime:
    print("❌ Target date has already passed.")
else:
    print("✅ Target date is in the future.")

# ------------------------------
# 6. Time difference
# ------------------------------
time_difference = target_datetime - current_datetime

days = time_difference.days
seconds = time_difference.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60

print("-" * 40)
print("⏳ Time Remaining:")
print("Days   :", days)
print("Hours  :", hours)
print("Minutes:", minutes)
