n = int(input("Enter the number: "))

for i in range(n):
    
    # First and last row
    if i == 0 or i == n - 1:
        print("*" * n)
    
    # Middle rows
    else:
        print("*" + " " * (n - 2) + "*")
