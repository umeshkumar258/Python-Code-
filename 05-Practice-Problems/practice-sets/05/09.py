# -------------------------------
# SET EXAMPLE - ALL IN ONE
# -------------------------------

# ❌ This is NOT possible because lists are mutable
# s = {8, 7, 12, "Harry", [1, 2]}

# ✅ Correct code (using tuple instead of list)
s = {8, 7, 12, "Harry", (1, 2)}

print("Set elements:")
print(s)

# -------------------------------
# Adding elements to set
# -------------------------------
s.add(100)
print("\nAfter adding 100:")
print(s)

# -------------------------------
# Removing elements
# -------------------------------
s.remove(7)
print("\nAfter removing 7:")
print(s)

# -------------------------------
# Set properties
# -------------------------------
print("\nSet properties:")
print("Length of set:", len(s))
print("Is 12 in set?", 12 in s)

# -------------------------------
# Important notes
# -------------------------------
print("\nImportant Notes:")
print("• Sets do not allow duplicate values")
print("• Sets are unordered")
print("• Sets store only immutable elements")
