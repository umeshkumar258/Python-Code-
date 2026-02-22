"""
Author: Umesh Kumar J B
Description:
Demonstrates usage of:
- External third-party modules (pyjokes)
- Python standard library (datetime)
- Date calculations
- Variables and formatted output
"""

from datetime import datetime, timedelta
import pyjokes


def print_joke():
    """Fetch and print a random joke using pyjokes."""
    print("Printing a random joke...\n")
    joke = pyjokes.get_joke()
    print(f"Joke: {joke}\n")


def date_operations():
    """Demonstrate basic datetime operations."""
    now = datetime.now()
    print(f"Current date and time: {now}")

    custom_date = datetime(2024, 12, 7)
    print(f"Custom date: {custom_date}")

    new_date = now + timedelta(days=5)
    print(f"Date after 5 days: {new_date}\n")


def main():
    name = "Umesh"
    print(f"Hello {name}! Welcome to advanced Python learning.\n")

    print_joke()
    date_operations()

    print("Learning never stops 🚀")


if __name__ == "__main__":
    main()
