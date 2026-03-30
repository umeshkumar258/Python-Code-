def get_integer(prompt):
    """Safely get integer input from user"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter an integer.\n")


def find_remainder(a, b):
    """Return remainder if valid"""
    if b == 0:
        return None
    return a % b


def display_result(a, b, remainder):
    """Display formatted result"""
    print("\n--- Result ---")
    print(f"First Number : {a}")
    print(f"Second Number: {b}")

    if remainder is None:
        print("❌ Cannot find remainder when divisor is zero.")
    else:
        print(f"Remainder    : {remainder}")
        print(f"{remainder} is the remainder when {a} is divided by {b}")


def main():
    """Main control loop"""
    print("🔢 Remainder Program with Validation")

    while True:
        a = get_integer("Enter the first number: ")
        b = get_integer("Enter the second number: ")

        remainder = find_remainder(a, b)
        display_result(a, b, remainder)

        choice = input("\nDo you want to continue? (y/n): ").lower()
        if choice != 'y':
            print("👋 Exiting program. Goodbye!")
            break


# Run program
main()
