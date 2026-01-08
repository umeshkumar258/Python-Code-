# Program to add two numbers with validation and extra details

def add_numbers():
    try:
        # Taking input from user
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        # Performing addition
        result = a + b

        # Displaying result
        print("\n--- Result ---")
        print(f"First Number : {a}")
        print(f"Second Number: {b}")
        print(f"Sum          : {result}")

        # Extra feature: check even or odd
        if result % 2 == 0:
            print("The sum is EVEN.")
        else:
            print("The sum is ODD.")

    except ValueError:
        print("❌ Please enter valid integer numbers only.")

# Function call
add_numbers()
