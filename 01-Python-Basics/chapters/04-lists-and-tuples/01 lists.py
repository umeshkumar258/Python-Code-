# A list can store different data types
items = ["Umesh", "orange", 6, 83, "Harry", 999]

print("Original List:", items)
print("Type of variable:", type(items))

# Indexing
print("First element:", items[0])

# Lists are mutable
items[0] = "Appu"
print("After updating first element:", items[0])

# Access last element
print("Last element:", items[-1])

# List slicing
print("From index 0 to end:", items[0:])
print("Full list copy:", items[:])

# Append new value
items.append("UmeshKumar")
print("After append:", items)

# Slice example
print("Slice [1:3] ->", items[1:3])

# Another list example
friends = ["John", "Doe", "Alice", "Bob"]

print("Friends slice [1:3] ->", friends[1:3])

# Modify element
items[3] = "Umesh"
print("Updated items list:", items)

print("Final friends list:", friends)
