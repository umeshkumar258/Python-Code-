# Normal function to find square
def square_function(n):
    return n * n


# Lambda function to find square
square_lambda = lambda n: n * n


# Testing both methods
num = 7

print("Square using normal function :", square_function(num))
print("Square using lambda function :", square_lambda(num))
