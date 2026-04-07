"""
Author: Umesh Kumar J B
Description:
Demonstrates user input handling,
type conversion, and basic operations (clean & reusable version).
"""

from typing import Callable


def get_valid_input(prompt: str, convert_func: Callable):
    """
    Reusable function to safely take input and convert it.
    """
    while True:
        try:
            return convert_func(input(prompt))
        except ValueError:
            print("Invalid input! Please try again.\n")


def add_two_numbers() -> None:
    """Take two integers and print their sum."""
    a = get_valid_input("Enter first number: ", int)
    b = get_valid_input("Enter second number: ", int)
    print(f"Sum = {a + b}\n")


def concatenate_strings() -> None:
    """Take two strings and concatenate them."""
    c = input("Enter first value: ")
    d = input("Enter second value: ")
    print(f"Concatenated result = {c + d}\n")


def float_input() -> None:
    """Take a float input and display its type."""
    x = get_valid_input("Enter a float number: ", float)
    print(f"Value: {x} | Type: {type(x).__name__}\n")


def integer_input() -> None:
    """Take an integer input and display it."""
    y = get_valid_input("Enter an integer: ", int)
    print(f"You entered: {y}\n")


def main() -> None:
    """Main function."""
    print("Welcome Umesh! Let's practice input handling.\n")

    add_two_numbers()
    concatenate_strings()
    float_input()
    integer_input()

    print("Keep learning and building 🚀")


if __name__ == "__main__":
    main()
