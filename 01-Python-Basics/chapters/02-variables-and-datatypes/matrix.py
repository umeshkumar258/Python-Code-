year = int(input("Enter a year: "))

# Leap year rule:
# ✔ divisible by 400 → leap year
# ✔ divisible by 4 but not by 100 → leap year

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
