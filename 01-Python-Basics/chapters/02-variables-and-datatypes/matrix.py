"""
Author: Umesh Kumar J B
Description: Program to check whether a year is a leap year.
"""


def is_leap_year(year: int) -> bool:
    """
    Return True if the given year is a leap year, else False.
    """
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def get_valid_year() -> int:
    """Take valid year input from the user."""
    while True:
        try:
            return int(input("Enter a year: "))
        except ValueError:
            print("Invalid input! Please enter a numeric year.\n")


def main() -> None:
    year = get_valid_year()

    result = "a leap year" if is_leap_year(year) else "not a leap year"
    print(f"{year} is {result}.")


if __name__ == "__main__":
    main()
