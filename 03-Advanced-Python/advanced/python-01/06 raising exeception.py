try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))

    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    print(f"The division a/b is: {a / b}")

except ValueError:
    print("Please enter only numbers.")

except ZeroDivisionError as e:
    print("Error:", e)

finally:
    print("Program finished safely.")
