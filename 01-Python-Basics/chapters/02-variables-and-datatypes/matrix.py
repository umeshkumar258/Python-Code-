def is_leap_year(year):
    """
    Returns True if the given year is a leap year,
    otherwise returns False.
    """
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


# Take user input
try:
    year = int(input("Enter a year: "))

    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

except ValueError:
    print("Please enter a valid numeric year.")
