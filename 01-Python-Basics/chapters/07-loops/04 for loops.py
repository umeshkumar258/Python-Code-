# ----------------------------------------
# 1. Basic range loop (0 to 7)
# ----------------------------------------
for i in range(8):
    print(i)

# ----------------------------------------
# 2. Range with start, stop, step
# Prints multiples of 10 from 0 to 100
# ----------------------------------------
for i in range(0, 101, 10):
    print(i)

# ----------------------------------------
# 3. Counting backwards using negative step
# ----------------------------------------
for i in range(10, 0, -1):
    print(i)

# ----------------------------------------
# 4. Range starting from any number
# ----------------------------------------
for i in range(5, 15):
    print(i)

# ----------------------------------------
# 5. Printing even and odd numbers
# ----------------------------------------
# Even numbers
for i in range(0, 21, 2):
    print("Even:", i)

# Odd numbers
for i in range(1, 21, 2):
    print("Odd:", i)

# ----------------------------------------
# 6. Loop through list items
# ----------------------------------------
names = ["umesh", "harry", "alex"]
for name in names:
    print("Name:", name)

# ----------------------------------------
# 7. Loop using enumerate() → index + value
# ----------------------------------------
items = ["a", "b", "c"]
for index, value in enumerate(items):
    print("Index:", index, "Value:", value)

# ----------------------------------------
# 8. Loop with continue (skip even numbers)
# ----------------------------------------
for i in range(1, 20):
    if i % 2 == 0:
        continue
    print("Odd only:", i)

# ----------------------------------------
# 9. Loop with break (stop at 10)
# ----------------------------------------
for i in range(1, 20):
    if i == 10:
        break
    print("Break example:", i)

# ----------------------------------------
# 10. Nested loops (loop inside loop)
# ----------------------------------------
for i in range(3):
    for j in range(2):
        print("i =", i, ", j =", j)

# ----------------------------------------
# 11. Create a list using range
# ----------------------------------------
numbers = list(range(1, 11))
print("List created from range:", numbers)

# ----------------------------------------
# 12. Sum of numbers using a loop
# ----------------------------------------
total = 0
for i in range(1, 11):
    total += i

print("Sum =", total)
