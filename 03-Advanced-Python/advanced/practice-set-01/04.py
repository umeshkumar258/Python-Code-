def divide_numbers():
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        result = a / b

    except ValueError:
        print("❌ Please enter valid integers only.")
    except ZeroDivisionError:
        print("❌ Cannot divide by zero (infinite).")
    else:
        print(f"✅ Division successful. Result = {result:.2f}")
    finally:
        print("🔚 Program finished.")


# Run the function
divide_numbers()
