





import math

# Input
n = int(input("Enter the number: "))

# Handle edge cases
if n <= 1:
    print("It is not a prime number")
elif n == 2:
    print("It is a prime number")  # 2 is the only even prime number
else:
    # Check divisibility from 2 to sqrt(n)
    for i in range(2, n):
        if n % i == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")
