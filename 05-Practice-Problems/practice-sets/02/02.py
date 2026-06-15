while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if b == 0:
        print("Cannot divide by zero!")
    else:
        print("Remainder =", a % b)

    choice = input("Do you want to continue? (y/n): ")

    if choice.lower() != 'y':
        print("Goodbye!")
        break
