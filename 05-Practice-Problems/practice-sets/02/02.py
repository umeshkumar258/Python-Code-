# Program to find remainder of two numbers

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    # Check for division by zero
    if b == 0:
        print("❌ Cannot find remainder when divisor is zero.")
    else:
        remainder = a % b
        print(f"\n{remainder} is the remainder when {a} is divided by {b}")

except ValueError:
    print("❌ Please enter valid integer numbers only.")
