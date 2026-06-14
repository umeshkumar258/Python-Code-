# List Example

items = ["Umesh", "orange", 6, 83, "Harry", 999]

print("Original List:", items)
print("Type:", type(items))

# Indexing
print("\nFirst element:", items[0])
print("Last element:", items[-1])

# Updating elements
items[0] = "Appu"
print("\nAfter updating first element:", items)

# Slicing
print("\nFull list:", items[:])
print("Slice [1:3]:", items[1:3])

# Append
items.append("UmeshKumar")
print("\nAfter append:", items)

# Modify an element
items[3] = "Umesh"
print("After modifying index 3:", items)

# Another list
friends = ["John", "Doe", "Alice", "Bob"]

print("\nFriends List:", friends)
print("Friends Slice [1:3]:", friends[1:3])
