# ---------------------------------------
# FACTORIAL PROGRAM (ALL IN ONE)
# ---------------------------------------

# 1️⃣ Factorial using Recursion
def factorial_recursive(n):
    """Returns factorial using recursion"""
    if n == 0 or n == 1:        # Base case
        return 1
    return n * factorial_recursive(n - 1)


# 2️⃣ Factorial using For Loop
def factorial_for(n):
    """Returns factorial using for loop"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 3️⃣ Factorial using While Loop
def factorial_while(n):
    """Returns factorial using while loop"""
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result


# ---------------------------------------
# MAIN PROGRAM
# ---------------------------------------
number = int(input("Enter a number: "))

if number < 0:
    print("❌ Factorial is not defined for negative numbers.")
else:
    print("\n✅ Factorial Results")
    print("---------------------")
    print("Using Recursion :", factorial_recursive(number))
    print("Using For Loop  :", factorial_for(number))
    print("Using While Loop:", factorial_while(number))


print("\nEnd of the program")
