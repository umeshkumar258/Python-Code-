# List Operations

a = [3, 5, 7, 88, 46]

print("Original List:", a)

# Sort
a.sort()
print("After sort():", a)

# Append
a.append(88)
print("After append(88):", a)

# Insert
a.insert(3, 99)
print("After insert(3, 99):", a)

# Pop
removed = a.pop(2)
print("Removed element:", removed)
print("After pop(2):", a)

# Index
print("Index of 88:", a.index(88))

# Count
print("Count of 88:", a.count(88))

# Reverse
a.reverse()
print("After reverse():", a)
