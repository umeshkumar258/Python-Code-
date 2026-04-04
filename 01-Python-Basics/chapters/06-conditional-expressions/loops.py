def even_odd_upto_n():
    try:
        number = int(input("Enter a positive number: ").strip())

        if number < 0:
            print("❗ Please enter a non-negative number.")
            return

        print("\n📊 Even / Odd Result:\n")

        for i in range(number + 1):
            status = "Even" if i % 2 == 0 else "Odd"
            print(f"{i:>3} → {status}")

    except ValueError:
        print("❗ Invalid input. Please enter a valid integer.")

# Run the function
if __name__ == "__main__":
    even_odd_upto_n()
