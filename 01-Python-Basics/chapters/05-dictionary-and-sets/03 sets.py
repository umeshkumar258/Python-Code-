# -------------------------------
# Creating a Set
# -------------------------------

numbers_set = {37, 393, 283, 29, 66}

print("Set elements:", numbers_set)
print("Type of numbers_set:", type(numbers_set))


# -------------------------------
# Different Python Data Types
# -------------------------------

set_example = {8}        # Set
tuple_example = ()       # Tuple
dict_example = {}        # Dictionary (not a set)
list_example = []        # List
string_example = ""      # String

print("\nData Types:")
print("Type of set_example:", type(set_example))
print("Type of tuple_example:", type(tuple_example))
print("Type of dict_example:", type(dict_example))
print("Type of list_example:", type(list_example))
print("Type of string_example:", type(string_example))


# -------------------------------
# Demonstrating Set Properties
# -------------------------------

# 1️⃣ Sets are unordered
unordered_set = {10, 5, 20, 1}
print("\nUnordered set:", unordered_set)

# 2️⃣ Sets remove duplicate values automatically
duplicate_set = {1, 2, 2, 3, 4, 4, 5}
print("Set with duplicates removed:", duplicate_set)

# 3️⃣ Adding elements to a set
duplicate_set.add(6)
print("After adding 6:", duplicate_set)

# 4️⃣ Removing elements from a set
duplicate_set.remove(3)
print("After removing 3:", duplicate_set)
