"""
Average Calculation Program
Author: Umesh
Description: Demonstrates functions with user input and parameters
"""


# ---------------------------------------
# Function to calculate average (user input)
# ---------------------------------------
def average_of_numbers(count: int = 3) -> float:
    """Takes 'count' numbers from the user and returns their average"""

    numbers = []

    for i in range(count):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("❌ Please enter a valid number.")

    return sum(numbers) / len(numbers)


# ---------------------------------------
# Function using parameters
# ---------------------------------------
def average_using_variables(*args: float) -> float:
    """Returns the average of given numbers"""
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


# ---------------------------------------
# Main Program
# ---------------------------------------
def main() -> None:
    print("🔹 Average using user input:\n")

    for i in range(3):
        result = average_of_numbers()
        print(f"Average {i + 1}: {result:.2f}\n")

    print("🔹 Average using variables:\n")

    a, b, c = 39, 390, 300
    avg = average_using_variables(a, b, c)

    print(f"Numbers: {a}, {b}, {c}")
    print(f"Average: {avg:.2f}")

    print("\n✅ End of the program")


# Run program
if __name__ == "__main__":
    main()
