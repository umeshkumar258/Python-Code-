# ---------------------------------------
# DIVISION WITH TRY-EXCEPT
# ---------------------------------------

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    result = a / b
    print(f"The division is: {result}")

except ZeroDivisionError:
    print("❌ Cannot divide by zero (infinite).")

except ValueError:
    print("❌ Please enter valid integers only.")

else:
    print("✅ Division successful.")

finally:
    print("Thanks")
