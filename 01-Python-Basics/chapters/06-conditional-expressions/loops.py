number = int(input("Enter the number: "))

print("Even/Odd result:\n")

for i in range(number + 1):
    status = "even" if i % 2 == 0 else "odd"
    print(f"{i:>3} → {status}")
