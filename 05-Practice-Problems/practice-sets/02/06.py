def power_calculator():

    while True:
        try:
            a = int(input("Enter base number: "))
            b = int(input("Enter power: "))

            result = a ** b

            print(f"\nResult: {a}^{b} = {result}")

            # Even or Odd
            if a % 2 == 0:
                print("Base is Even")
            else:
                print("Base is Odd")

            # Large number check
            if result > 1000000:
                print("Large Number!")

        except ValueError:
            print("Invalid input! Enter integers only.")

        choice = input("\nCalculate again? (y/n): ").lower()

        if choice != "y":
            print("Program Ended")
            break


# Function Call
power_calculator()
