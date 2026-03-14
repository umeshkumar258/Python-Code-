# ---------------------------------------
# FACTORIAL PROGRAM (IMPROVED VERSION)
# ---------------------------------------

def factorial_recursive(n):
    """Return factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_for(n):
    """Return factorial using a for loop."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_while(n):
    """Return factorial using a while loop."""
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


# ---------------------------------------
# MAIN PROGRAM
# ---------------------------------------

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("\nFactorial Results")
    print("-------------------")
    print(f"Using Recursion : {factorial_recursive(number)}")
    print(f"Using For Loop  : {factorial_for(number)}")
    print(f"Using While Loop: {factorial_while(number)}")

print("\nEnd of the program")
