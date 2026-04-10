"""
Python Functions Examples
Author: Umesh
Description: Demonstrates different types of functions in Python
"""


# ---------------------------------------
# 1. Function with user input
# ---------------------------------------
def get_user_name() -> str:
    """Takes user input and returns the name."""
    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name
        print("❌ Name cannot be empty. Please try again.")


def good_day(name: str) -> None:
    """Greets the user with their name."""
    print(f"Good day, {name}! 😊")


# ---------------------------------------
# 2. Simple function (no parameters)
# ---------------------------------------
def show_message() -> None:
    """Displays a simple message."""
    print("This is a simple function.")


# ---------------------------------------
# 3. Function with parameters
# ---------------------------------------
def greet(name: str) -> None:
    """Greets a user using their name."""
    print(f"Hello, {name}! Welcome to Python.")


# ---------------------------------------
# 4. Function with return value
# ---------------------------------------
def add(a: int, b: int) -> int:
    """Returns the sum of two numbers."""
    return a + b


# ---------------------------------------
# 5. Default parameter
# ---------------------------------------
def country_name(country: str = "India") -> None:
    """Prints the country name."""
    print(f"I am from {country}.")


# ---------------------------------------
# 6. Function used inside a loop
# ---------------------------------------
def square(num: int) -> int:
    """Returns the square of a number."""
    return num * num


# ---------------------------------------
# 7. Lambda function (short function)
# ---------------------------------------
multiply = lambda x, y: x * y


# ---------------------------------------
# Main Program
# ---------------------------------------
def main() -> None:
    """Main function to execute all examples."""

    # Get user input once
    user_name = get_user_name()

    good_day(user_name)
    show_message()
    greet(user_name)

    result = add(10, 20)
    print(f"Sum: {result}")

    country_name()
    country_name("USA")

    print("\nSquares from 1 to 5:")
    for i in range(1, 6):
        print(f"{i}² = {square(i)}")

    print(f"\nMultiplication: {multiply(4, 5)}")


# Run the program
if __name__ == "__main__":
    main()
