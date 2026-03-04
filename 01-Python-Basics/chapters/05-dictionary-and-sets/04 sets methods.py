# -------------------------------
# Set Properties
# 1. Sets are unordered
# 2. Sets are unindexed
# 3. Items cannot be changed directly
# 4. Sets do not allow duplicate values
# -------------------------------

# Creating two sets
set1 = {37, 393, 283, 29, 66}
set2 = {35, 72, 283, 9, 66}

print("Set1:", set1)
print("Set2:", set2)


# -------------------------------
# Adding an element
# -------------------------------
set1.add(76)
print("\nAfter adding 76 to set1:", set1)


# -------------------------------
# Set Operations
# -------------------------------

# Subset check
print("\nIs set1 a subset of set2?", set1.issubset(set2))

# Superset check
print("Is set1 a superset of set2?", set1.issuperset(set2))

# Intersection (common elements)
print("Intersection of set1 and set2:", set1.intersection(set2))

# Union (all unique elements)
print("Union of set1 and set2:", set1.union(set2))


# -------------------------------
# Removing an element
# -------------------------------
set1.remove(37)
print("\nAfter removing 37 from set1:", set1)


# -------------------------------
# Length of the set
# -------------------------------
print("Length of set1:", len(set1))


# -------------------------------
# Example: Superset check
# -------------------------------
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 6}

print("\nExample sets:")
print("s1:", s1)
print("s2:", s2)
print("Is s2 a superset of s1?", s2.issuperset(s1))
