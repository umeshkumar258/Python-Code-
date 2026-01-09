def number_operations():
    print("📘 Number Operations Program")
    print("-" * 30)

    try:
        a = int(input("Enter a number: "))

        print("\n📊 Results")
        print(f"Square using ** operator : {a ** 2}")
        print(f"Square using * operator  : {a * a}")

        # Extra operations
        print(f"Cube of the number       : {a ** 3}")
        print(f"Is the number even?      : {'Yes' if a % 2 == 0 else 'No'}")

    except ValueError:
        print("\n❌ Error: Please enter a valid integer.")

# Function call
number_operations()
