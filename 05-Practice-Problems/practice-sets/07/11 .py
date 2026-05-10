# Reverse Multiplication Table

n = int(input("Enter the number: "))

for i in range(10, 0, -1):
    result = n * i
    print(f"{n} × {i} = {result}")
