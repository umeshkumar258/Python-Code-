# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Addition
print("\nAddition =", a + b)

# Remainder
if b != 0:
    print("Remainder =", a % b)
else:
    print("Cannot divide by zero")

# Comparison
print("\nComparison")
print("a < b :", a < b)
print("a > b :", a > b)
print("a == b:", a == b)

# Type Conversion
x = 48.39
y = str(x)

print("\nType Conversion")
print("Float :", x, type(x))
print("String:", y, type(y))

# Even or Odd
total = a + b

print("\nSum =", total)

if total % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print("\nProgram executed successfully!")
