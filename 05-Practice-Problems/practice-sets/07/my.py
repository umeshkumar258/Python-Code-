user = int(input("Enter the number of elements: "))

l = []
i = 0

while i < user:
    num = int(input("Enter element: "))
    l.append(num)
    i += 1

total = sum(l)

print("List:", l)
print("Sum of elements:", total)
