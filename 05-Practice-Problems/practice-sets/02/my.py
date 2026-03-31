def number_operations():
    print("📘 Number Operations Program")
    print("-" * 30)

    while True:
        try:
            a = int(input("Enter a number: "))

            # Calculations
            square1 = a ** 2
            square2 = a * a
            cube = a ** 3
            is_even = (a % 2 == 0)

            print("\n📊 Results")
            print(f"Square (using **): {square1}")
            print(f"Square (using * ): {square2}")
            print(f"Cube            : {cube}")
            print(f"Even Number?    : {'Yes' if is_even else 'No'}")

            # Extra features
            print(f"Absolute value  : {abs(a)}")

            if a < 0:
                print("⚠️ Note: Negative number entered")

        except ValueError:
            print("\n❌ Error: Please enter a valid integer.")

        # Repeat option
        choice = input("\nDo you want to continue? (y/n): ").lower()
        if choice != 'y':
            print("👋 Program Ended")
            break


# Function call
number_operations()
