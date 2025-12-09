# Dictionary creation
marks = {
    "umesh": "73",
    "bab": "99",
    "harry": "72"
}

# Display dictionary and its type
print("Dictionary:", marks)
print("Type:", type(marks))

# Key properties of dictionaries:
# 1. Unordered (until Python 3.7: now maintains insertion order but conceptually unordered)
# 2. Mutable
# 3. Indexed by keys
# 4. Duplicate keys are not allowed

# Accessing values using keys
print("Umesh's marks:", marks["umesh"])
print("Length of dictionary:", len(marks))

# Accessing value using get() method (safer method)
print("Bab's marks:", marks["bab"])
print("Bab's marks (using get):", marks.get("bab"))

# Dictionary with list value
student_data = {
    "numbers": [939, 9303, 99],
    "umesh": "939"
}

print("Student Data:", student_data)
print("Numbers list:", student_data["numbers"])
