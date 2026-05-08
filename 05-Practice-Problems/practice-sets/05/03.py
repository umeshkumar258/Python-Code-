# -------- SET OPERATIONS PROGRAM --------

# Mixed data type set
a = {"66", 66}

print("Set a:", a)
print("Length:", len(a))

print("-" * 30)

# Empty set
numbers = set()

print("Empty set:", numbers)
print("Type:", type(numbers))

print("-" * 30)

# Adding elements
numbers.add(10)
numbers.add(20)
numbers.add(20)   # Duplicate ignored

print("After add():", numbers)

print("-" * 30)

# Adding multiple values
numbers.update([30, 40, 50])

print("After update():", numbers)

print("-" * 30)

# Removing elements
numbers.remove(20)
numbers.discard(100)   # No error if value not found

print("After removal:", numbers)

print("-" * 30)

# Another set
b = {30, 40, 60}

print("Set b:", b)

# Set operations
print("Union:", numbers | b)
print("Intersection:", numbers & b)
print("Difference:", numbers - b)
