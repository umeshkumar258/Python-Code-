def power_of_number():
    print("🔢 Power Calculator (a^a)")
    print("-" * 30)

    try:
        a = int(input("Enter a number: "))

        result = a ** a

        print("\n📊 Result")
        print(f"{a} raised to the power of {a} is: {result}")

        # Extra information
        print(f"Number type : {'Even' if a % 2 == 0 else 'Odd'}")

    except ValueError:
        print("\n❌ Error: Please enter a valid integer.")

# Function call
power_of_number()
