# Tuple declaration
a = (4, 484, 2, 384, 2)

# Set declaration (but later overwritten so not needed)
b = {8}

print("Type of a:", type(a), "| Value:", a)
print("Length of tuple a:", len(a))

# Count occurrences of value in tuple
print("Count of 2 in tuple a:", a.count(2))

# Tuple repetition
b = a * 3
print("Tuple repeated 3 times:", b)

# Finding first index of value
print("Index of first occurrence of 2:", a.index(2))

# NOTE:
# Tuples are immutable - values cannot be changed or modified.
