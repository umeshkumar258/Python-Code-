# ---------------------------------------
# 1. Function with parameters (no return)
# ---------------------------------------
def good_day(name, ending):
    print(f"Good Day {name}")
    print(ending)


good_day("Umesh", "Thanks")
good_day("Harry", "Thank you")


# ---------------------------------------
# 2. Function with return value
# ---------------------------------------
def good_day_with_status(name, ending, extra):
    print(f"Good Day {name} {extra}")
    print(ending)
    return "Done"


status = good_day_with_status("Umesh", "Thanks", "🔥")
print("Function returned:", status)


# ---------------------------------------
# 3. Function to add two numbers
# ---------------------------------------
def add_numbers(num1, num2):
    return num1 + num2


# ---------------------------------------
# 4. Loop with input + exception handling
# ---------------------------------------
for i in range(3):
    try:
        num1 = int(input("\nEnter first number: "))
        num2 = int(input("Enter second number: "))

        result = add_numbers(num1, num2)
        print("The result is:", result)

    except ValueError:
        print("❌ Invalid input. Please enter valid integers.")
