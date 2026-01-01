from typing import List, Tuple, Dict

# -------------------------------
# LIST
# -------------------------------
numbers: List[int] = [1, 2, 4, 5, 7]

# List operations
numbers.append(10)          # Add element
numbers.remove(4)           # Remove element
total = sum(numbers)        # Sum of elements

print("List:", numbers)
print("Sum of list:", total)


# -------------------------------
# TUPLE
# -------------------------------
person: Tuple[str, int] = ("Umesh", 18)

name, age = person          # Tuple unpacking

print("\nTuple:", person)
print("Name:", name)
print("Age:", age)


# -------------------------------
# DICTIONARY
# -------------------------------
scores: Dict[str, int] = {
    "Umesh": 99,
    "Ravi": 85
}

# Dictionary operations
scores["Anil"] = 90         # Add new key-value pair
scores["Ravi"] = 88         # Update value

print("\nDictionary:", scores)

# Loop through dictionary
for student, marks in scores.items():
    print(student, "scored", marks)


# -------------------------------
# TYPE CHECKING (Optional but useful)
# -------------------------------
print("\nType of numbers:", type(numbers))
print("Type of person:", type(person))
print("Type of scores:", type(scores))
