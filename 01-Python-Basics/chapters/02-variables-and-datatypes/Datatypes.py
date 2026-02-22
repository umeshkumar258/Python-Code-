"""
Author: Umesh Kumar J B
Description: Demonstrating basic Python data types
"""

def display_value_and_type(value):
    """Print value and its data type."""
    print(f"Value: {value} | Type: {type(value)}")


def main():
    a = "umesh"      # String
    b = 3            # Integer
    c = 49.48        # Float
    d = True         # Boolean
    e = None         # NoneType

    variables = [a, b, c, d, e]

    for item in variables:
        display_value_and_type(item)


if __name__ == "__main__":
    main()
