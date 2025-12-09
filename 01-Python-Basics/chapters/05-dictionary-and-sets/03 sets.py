# Defining a set (avoid naming variable as set)
my_set = {37, 393, 283, 29, 66}
print("my_set:", my_set)
print("Type of my_set:", type(my_set))


# Other data types
a = {8}          # This is a set
b = ()           # This is a tuple
c = {}           # This is a dictionary, NOT a set
d = []           # This is a list
e = ""           # This is a string

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))
print("Type of d:", type(d))
print("Type of e:", type(e))


# Set Properties:
# 1. Sets are unordered => element order doesn’t matter
# 2. Sets are unindexed => cannot access elements using index
# 3. Sets are immutable (you can add/remove elements, but existing elements cannot change)
# 4. Sets cannot contain duplicate values
