"""
Author: Umesh Kumar J B
Description:
Demonstrates user input handling,
type conversion, and basic operations.
"""

def add_two_numbers():
    """Take two integers and print their sum safely."""
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"Sum = {a + b}\n")
    except ValueError:
        print("Invalid input! Please enter valid integers.\n")


def concatenate_strings():
    """Take two strings and concatenate them."""
    c = input("Enter first value: ")
    d = input("Enter second value: ")
    print(f"Concatenated result = {c + d}\n")


def float_input():
    """Take a float input and display its type."""
    try:
        x = float(input("Enter a float number: "))
        print(f"Value: {x} | Type: {type(x)}\n")
    except ValueError:
        print("Invalid float input!\n")


def integer_input():
    """Take an integer input and display it."""
    try:
        y = int(input("Enter an integer: "))
        print(f"You entered: {y}\n")
    except ValueError:
        print("Invalid integer input!\n")


def main():
    print("Welcome Umesh! Let's practice input handling.\n")
    
    add_two_numbers()
    concatenate_strings()
    float_input()
    integer_input()

    print("Keep learning and building 🚀")


if __name__ == "__main__":
    main()
