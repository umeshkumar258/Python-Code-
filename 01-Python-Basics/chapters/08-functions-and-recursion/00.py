"""
Python Functions Examples
Author: Umesh
Description: Demonstrates different types of functions in Python
"""


# ---------------------------------------
# 1. Function with user input
# ---------------------------------------
def good_day():
    """Greets the user with their name."""
    user = input("Enter your name: ")
    print(f"Good day, {user}! 😊")


# ---------------------------------------
# 2. Simple function (no parameters)
# ---------------------------------------
def show_message():
    """Displays a simple message."""
    print("This is a simple function.")


# ---------------------------------------
# 3. Function with parameters
# ---------------------------------------
def greet(name):
    """Greets a user using their name."""
    print(f"Hello, {name}! Welcome to Python.")


# ---------------------------------------
# 4. Function with return value
# ---------------------------------------
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


# ---------------------------------------
# 5. Default parameter
# ---------------------------------------
def country_name(country="India"):
    """Prints the country name."""
    print(f"I am from {country}.")


# ---------------------------------------
# 6. Function used inside a loop
# ---------------------------------------
def square(num):
    """Returns the square of a number."""
    return num * num


# ---------------------------------------
# 7. Lambda function (short function)
# ---------------------------------------
multiply = lambda x, y: x * y


# ---------------------------------------
# Main Program
# ---------------------------------------
def main():
    good_day()
    show_message()
    greet("Umesh")

    result = add(10, 20)
    print("Sum:", result)

    country_name()
    country_name("USA")

    print("\nSquares from 1 to 5:")
    for i in range(1, 6):
        print(square(i))

    print("\nMultiplication:", multiply(4, 5))


# Run the program
if __name__ == "__main__":
    main()
