# A list can contain different data types (strings, numbers, etc.)
name = ["umesh", "orange", 6, 83, "harry", 999]

print("Original List:", name)
print("Type of variable 'name':", type(name))

# Indexing example
print("First element:", name[0])

# Lists are mutable (values can be changed)
name[0] = "appu"
print("Updated first element:", name[0])   # Shows mutability

# Access last element
print("Last element:", name[-1])

# List slicing
print("From index 0 to end:", name[0:])
print("Full list slice:", name[:])

# Append new value
name.append("umeshkumar")
print("List after appending:", name)

# Slice example (index 1 and 2)
print("Slice [1:3] ->", name[1:3])

# Another list example
friends = ["john", "doe", "alice", "bob"]

print("Friend slice [1:3] ->", friends[1:3])

# Modify element in list
name[3] = "umesh"
print("Updated name list:", name)

# Printing final friends list
print("Friends list:", friends)
