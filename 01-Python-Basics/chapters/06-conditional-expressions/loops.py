try:
    number = int(input("Enter the number: "))

    if number < 0:
        print("❗ Please enter a positive number.")
    else:
        print("\nEven / Odd Result:\n")

        for i in range(number + 1):
            status = "Even" if i % 2 == 0 else "Odd"
            print(f"{i:>3} → {status}")

except ValueError:
    print("❗ Invalid input. Please enter a valid integer.")
