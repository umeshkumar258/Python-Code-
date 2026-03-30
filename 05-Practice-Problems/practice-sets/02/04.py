def get_integer(prompt):
    """Safely get integer input"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter an integer.\n")


def basic_operations(a, b):
    """Perform addition and remainder"""
    print("\n--- BASIC OPERATIONS ---")
    print(f"Addition ({a} + {b}) = {a + b}")

    if b != 0:
        print(f"Remainder ({a} % {b}) = {a % b}")
    else:
        print("Remainder: Cannot divide by zero")


def comparison(a, b):
    """Compare two numbers"""
    print("\n--- COMPARISON ---")
    print(f"Is {a} < {b}?  : {a < b}")
    print(f"Is {a} > {b}?  : {a > b}")
    print(f"Is {a} == {b}? : {a == b}")


def type_conversion():
    """Demonstrate type conversion"""
    x = 48.39
    y = str(x)

    print("\n--- TYPE CONVERSION ---")
    print(f"Original Value      : {x} ({type(x)})")
    print(f"Converted Value     : {y} ({type(y)})")


def even_odd(a, b):
    """Check if sum is even or odd"""
    print("\n--- EVEN / ODD CHECK ---")
    result = a + b
    print(f"Sum = {result}")

    if result % 2 == 0:
        print("The sum is EVEN")
    else:
        print("The sum is ODD")


def main():
    print("🔢 ALL-IN-ONE PYTHON PROGRAM")

    a = get_integer("Enter the first number: ")
    b = get_integer("Enter the second number: ")

    basic_operations(a, b)
    comparison(a, b)
    type_conversion()
    even_odd(a, b)

    print("\n✅ Program executed successfully!")


# Run program
main()
