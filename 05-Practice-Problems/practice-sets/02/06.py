def power_of_number():
    print("🔢 Power Calculator")
    print("-" * 30)

    while True:
        try:
            a = int(input("Enter base number (a): "))
            b = int(input("Enter power (b): "))

            result = a ** b

            print("\n📊 Result")
            print(f"{a}^{b} = {result}")

            # Extra info
            print(f"Base is {'Even' if a % 2 == 0 else 'Odd'}")

            # Warning for large numbers
            if result > 1_000_000:
                print("⚠️ Result is a very large number!")

        except ValueError:
            print("\n❌ Error: Please enter valid integers.")

        # Continue option
        choice = input("\nDo you want to calculate again? (y/n): ").lower()
        if choice != 'y':
            print("👋 Exiting Calculator. Thank you!")
            break


# Function call
power_of_number()
