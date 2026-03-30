def get_integer(prompt):
    """Function to safely get integer input from user"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter an integer.\n")


def check_even_odd(number):
    """Function to check if number is even or odd"""
    return "EVEN" if number % 2 == 0 else "ODD"


def add_numbers():
    """Main function to add two numbers"""
    print("\n🔢 Addition Program with Validation")

    a = get_integer("Enter the first number: ")
    b = get_integer("Enter the second number: ")

    result = a + b

    print("\n--- Result ---")
    print(f"First Number : {a}")
    print(f"Second Number: {b}")
    print(f"Sum          : {result}")
    print(f"The sum is {check_even_odd(result)}.")


def main():
    """Main control loop"""
    while True:
        add_numbers()

        choice = input("\nDo you want to continue? (y/n): ").lower()
        if choice != 'y':
            print("👋 Exiting program. Goodbye!")
            break


# Run program
main()
