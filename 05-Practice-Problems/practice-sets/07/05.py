# Sum of N natural numbers

n = int(input("Enter the number: "))

# Using formula (best way)
total = n * (n + 1) // 2
print("Sum using formula:", total)

# Using for loop
total = sum(range(n + 1))
print("Sum using loop:", total)
