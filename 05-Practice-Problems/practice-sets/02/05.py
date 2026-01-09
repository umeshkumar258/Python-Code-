def calculate_average():
    print("📘 Average Calculator")
    print("-" * 25)

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        total = a + b
        average = total / 2

        print("\n📊 Results")
        print(f"Sum       : {total}")
        print(f"Average   : {average}")

    except ValueError:
        print("\n❌ Error: Please enter valid numbers only.")

# Function call
calculate_average()
