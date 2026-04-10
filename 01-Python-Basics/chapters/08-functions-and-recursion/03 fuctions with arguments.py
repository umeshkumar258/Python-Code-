"""
Function Demonstration Program
Author: Umesh
Description: Shows functions with parameters, return values, and exception handling
"""


# ---------------------------------------
# 1. Function with parameters (no return)
# ---------------------------------------
def greet_user(name: str, ending: str) -> None:
    """Greets the user"""
    print(f"Good Day {name}")
    print(ending)


# ---------------------------------------
# 2. Function with return value
# ---------------------------------------
def greet_with_status(name: str, ending: str, extra: str = "") -> str:
    """Greets the user and returns status"""
    print(f"Good Day {name} {extra}")
    print(ending)
    return "Done"


# ---------------------------------------
# 3. Function to add two numbers
# ---------------------------------------
def add_numbers(num1: float, num2: float) -> float:
    """Returns the sum of two numbers"""
    return num1 + num2


# ---------------------------------------
# 4. Helper function for safe input
# ---------------------------------------
def get_number(prompt: str) -> float:
    """Safely gets a number from the user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


# ---------------------------------------
# 5. Main Program
# ---------------------------------------
def main() -> None:
    """Main execution function"""

    print("🔹 Greeting Examples\n")

    greet_user("Umesh", "Thanks")
    greet_user("Harry", "Thank you")

    status = greet_with_status("Umesh", "Thanks", "🔥")
    print(f"Function returned: {status}\n")

    print("🔹 Addition Program\n")

    for i in range(3):
        print(f"--- Calculation {i + 1} ---")

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        result = add_numbers(num1, num2)
        print(f"✅ Result: {result}\n")


# Run the program
if __name__ == "__main__":
    main()
