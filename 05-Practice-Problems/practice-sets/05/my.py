# --------------------------------
# ALL IN ONE SET PROGRAM
# --------------------------------

# Creating an empty set
s = set()

# Taking input from the user
for i in range(5):
    num = int(input("Enter the number: "))
    s.add(num)

# Display set
print("\nSet elements:")
print(s)

# --------------------------------
# Adding element
# --------------------------------
s.add(100)
print("\nAfter adding 100:")
print(s)

# --------------------------------
# Removing element
# --------------------------------
s.remove(100)
print("\nAfter removing 100:")
print(s)

# --------------------------------
# Checking membership
# --------------------------------
print("\nIs 10 present in set?", 10 in s)

# --------------------------------
# Length of set
# --------------------------------
print("Total elements:", len(s))

# --------------------------------
# Important notes
# --------------------------------
print("\nImportant Points:")
print("1. Sets do not allow duplicate values")
print("2. Sets are unordered")
print("3. Sets store only immutable elements")
print("4. Empty set is created using set()")
