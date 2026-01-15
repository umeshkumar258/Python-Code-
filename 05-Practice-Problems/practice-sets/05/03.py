# Creating a set with mixed data types
a = {'66', 66}

print("Set a:", a)
print("Type of a:", type(a))
print("Length of a:", len(a))   # Number of unique elements

print("-" * 40)

# Creating an empty set (IMPORTANT)
s = set()   # {} creates an empty dictionary, not a set

print("Empty set s:", s)
print("Type of s:", type(s))

print("-" * 40)

# Adding elements to a set
s.add(10)
s.add(20)
s.add(20)   # Duplicate values are ignored

print("Set s after adding elements:", s)

print("-" * 40)

# Adding multiple elements
s.update([30, 40, 50])
print("Set s after update:", s)

print("-" * 40)

# Removing elements
s.remove(20)        # Removes 20 (error if not found)
s.discard(100)      # No error even if element not present

print("Set s after removal:", s)

print("-" * 40)

# Set operations
b = {30, 40, 60}

print("Set b:", b)
print("Union:", s.union(b))
print("Intersection:", s.intersection(b))
print("Difference (s - b):", s.difference(b))
