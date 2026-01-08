# ALL IN ONE PYTHON PROGRAM

# 1. Taking integer input
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("\n--- BASIC OPERATIONS ---")

    # 2. Addition
    print(f"Addition ({a} + {b}) = {a + b}")

    # 3. Remainder
    if b != 0:
        print(f"Remainder ({a} % {b}) = {a % b}")
    else:
        print("Remainder: Cannot divide by zero")

    # 4. Comparison
    print("\n--- COMPARISON ---")
    print(f"Is {a} < {b}? :", a < b)
    print(f"Is {a} > {b}? :", a > b)
    print(f"Is {a} == {b}? :", a == b)

    # 5. Type conversion
    x = 48.39
    y = str(x)

    print("\n--- TYPE CONVERSION ---")
    print("Original value:", x)
    print("Converted value:", y)
    print("Type after conversion:", type(y))

    # 6. Even or Odd check
    print("\n--- EVEN / ODD CHECK ---")
    if (a + b) % 2 == 0:
        print("Sum is EVEN")
    else:
        print("Sum is ODD")

except ValueError:
    print("❌ Please enter valid integer numbers only.")
