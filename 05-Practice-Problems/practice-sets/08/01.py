n = [int(input("Enter the numbers: ")) for i in range(3)]

a = max(n)

print(f"The largest number is {a}")


# Function to find the greatest of three numbers
def greatest(a, b, c):
    return max(a, b, c)

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Finding and displaying the greatest number
result = greatest(num1, num2, num3)
print(f"The greatest number is: {result}")
