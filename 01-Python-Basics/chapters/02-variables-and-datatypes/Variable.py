"""
Author: Umesh Kumar J B
Description: Demonstrates basic arithmetic operations and data types.
"""


def display_value_and_type(value):
    """Print value and its type in a clean format."""
    print(f"Value: {value!r:<10} | Type: {type(value).__name__}")


def main() -> None:
    # Integer variables
    num1: int = 5
    num2: int = 3

    # Perform operations
    sum_result: int = num1 + num2
    product_result: int = num1 * num2

    # Print results
    print("\n--- Arithmetic Operations ---\n")
    print(f"Sum of {num1} and {num2} is: {sum_result}")
    print(f"Product of {num1} and {num2} is: {product_result}")

    # String variable
    name: str = "Umesh"

    print("\n--- Data Types ---\n")
    display_value_and_type(name)
    display_value_and_type(num1)


if __name__ == "__main__":
    main()
