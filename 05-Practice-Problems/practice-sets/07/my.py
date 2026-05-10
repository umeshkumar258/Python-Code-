n = int(input("Enter the number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

print("List:", numbers)
print("Sum of elements:", sum(numbers))
