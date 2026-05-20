# Simple All-in-One Python Program

def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid integer.\n")


# Input
a = get_number("Enter first number: ")
b = get_number("Enter second number: ")

# Basic Operations
print("\n--- BASIC OPERATIONS ---")
print("Addition =", a + b)

if b != 0:
    print("Remainder =", a % b)
else:
    print("Cannot divide by zero")

# Comparison
print("\n--- COMPARISON ---")
print(a, "<", b, "=", a < b)
print(a, ">", b, "=", a > b)
print(a, "==", b, "=", a == b)

# Type Conversion
print("\n--- TYPE CONVERSION ---")
x = 48.39
y = str(x)

print("Original:", x, type(x))
print("Converted:", y, type(y))

# Even or Odd
print("\n--- EVEN OR ODD ---")
total = a + b

print("Sum =", total)

if total % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print("\nProgram executed successfully!")
