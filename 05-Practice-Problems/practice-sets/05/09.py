# -------------------------------
# Simple Set Example
# -------------------------------

# Creating a set
# Use tuple instead of list because sets store only immutable values
s = {8, 7, 12, "Harry", (1, 2)}

print("Original Set:", s)

# Adding an element
s.add(100)
print("\nAfter adding 100:", s)

# Removing an element
s.remove(7)
print("\nAfter removing 7:", s)

# Set properties
print("\nLength of set:", len(s))
print("Is 12 present?", 12 in s)

# Important Notes
print("\nImportant Notes:")
print("- Sets do not allow duplicates")
print("- Sets are unordered")
print("- Sets store immutable elements only")
