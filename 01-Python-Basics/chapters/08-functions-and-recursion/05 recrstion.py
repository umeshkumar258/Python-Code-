# factorial (5) = 5*4*3*2*1



def factorial(n):
    if(n==1 or n==0):   # Base case:
        return 1          # return type is int
    return n * factorial(n-1)   #Recursive Case:

n = int(input("Enter the number:"))
print(f"{factorial(n)}")



def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
number = int(input("Enter a number: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {number} is {factorial(number)}")
