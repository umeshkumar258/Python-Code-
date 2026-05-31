n = int(input("Enter the number of rows: "))

for row in range(1, n + 1):
    print(" " * (n - row) + "*" * (2 * row - 1))
