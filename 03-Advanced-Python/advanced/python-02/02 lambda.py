def square_function(n):
    return n * n

square_lambda = lambda n: n * n

try:
    num = int(input("Enter a number: "))

    print(f"Square using normal function: {square_function(num)}")
    print(f"Square using lambda function: {square_lambda(num)}")
    print(f"Type of input: {type(num)}")

except ValueError:
    print("Please enter a valid integer.")
