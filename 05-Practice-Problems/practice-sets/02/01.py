# Addition of two numbers and check Even/Odd

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b

print("Sum =", sum)

if sum % 2 == 0:
    print("The sum is EVEN")
else:
    print("The sum is ODD")
