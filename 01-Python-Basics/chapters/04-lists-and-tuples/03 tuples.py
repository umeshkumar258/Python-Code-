# Tuple Example

numbers = (4, 484, 2, 384, 2)

print("Tuple:", numbers)
print("Type:", type(numbers))
print("Length:", len(numbers))

# Accessing elements
print("\nFirst element:", numbers[0])
print("Last element:", numbers[-1])
print("Slice [1:4]:", numbers[1:4])

# Count and Index
print("\nCount of 2:", numbers.count(2))
print("Index of 2:", numbers.index(2))

# Repetition
print("\nRepeated tuple:", numbers * 3)

# Concatenation
new_tuple = numbers + (100, 200)
print("After concatenation:", new_tuple)

# Packing and Unpacking
a, b, c, d, e = numbers
print("\nUnpacked values:", a, b, c, d, e)

# Immutability
# numbers[0] = 10   # Error
print("\nTuples are immutable (cannot be modified)")
