# Set properties:
# 1. Sets are unordered 
# 2. Sets are unindexed 
# 3. You cannot change items directly
# 4. Sets do not allow duplicates

set1 = {37, 393, 283, 29, 66}
set2 = {35, 72, 283, 9, 66}

set1.add(76)  # Add an element

# Display results
print("Is set1 a subset of set2?", set1.issubset(set2))
print("Intersection:", set1.intersection(set2))
print("Is set1 a superset of set2?", set1.issuperset(set2))
print("Union:", set1.union(set2))

# Remove element (do NOT print remove())
set1.remove(37)

print("Length of set1:", len(set1))
print("Updated set1:", set1)

# Example: superset check
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 6}
print("Is s2 a superset of s1?", s2.issuperset(s1))
