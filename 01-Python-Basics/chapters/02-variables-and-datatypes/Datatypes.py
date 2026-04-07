"""
Author: Umesh Kumar J B
Description: Demonstrates basic Python data types in a clean and structured way.
"""

from typing import Any


def display_value_and_type(value: Any) -> None:
    """Print the value along with its data type."""
    print(f"Value: {value!r:<10} | Type: {type(value).__name__}")


def main() -> None:
    """Main function to demonstrate different data types."""
    
    # Define variables of different data types
    string_val: str = "umesh"
    int_val: int = 3
    float_val: float = 49.48
    bool_val: bool = True
    none_val: None = None

    # Store values in a tuple (immutable collection)
    variables = (string_val, int_val, float_val, bool_val, none_val)

    print("\n--- Python Data Types Demonstration ---\n")

    for item in variables:
        display_value_and_type(item)


if __name__ == "__main__":
    main()
