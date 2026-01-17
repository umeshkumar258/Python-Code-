numbers = []

for _ in range(4):
    numbers.append(int(input("Enter the number: ")))

numbers.sort()

print("Sorted list:", numbers)
print("Largest number:", numbers[-1])
