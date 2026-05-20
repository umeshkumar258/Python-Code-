def number_operations():

    while True:
        try:
            n = int(input("Enter a number: "))

            print("\n--- RESULTS ---")
            print("Square =", n * n)
            print("Cube   =", n ** 3)

            # Even or Odd
            if n % 2 == 0:
                print("Even Number")
            else:
                print("Odd Number")

            print("Absolute Value =", abs(n))

            if n < 0:
                print("Negative number entered")

        except ValueError:
            print("Invalid input! Enter integers only.")

        choice = input("\nContinue? (y/n): ").lower()

        if choice != "y":
            print("Program Ended")
            break


# Function Call
number_operations()
