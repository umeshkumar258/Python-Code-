# Python Collections with Type Hints - Improved Version

# -------------------------------
# LIST
# -------------------------------
numbers: list[int] = [1, 2, 4, 5, 7]

# List operations
numbers.append(10)

if 4 in numbers:   # Safe removal
    numbers.remove(4)

total: int = sum(numbers)

print(f"📌 List: {numbers}")
print(f"📊 Sum of list: {total}")


# -------------------------------
# TUPLE
# -------------------------------
person: tuple[str, int] = ("Umesh", 18)

name, age = person  # Tuple unpacking

print(f"\n📌 Tuple: {person}")
print(f"👤 Name: {name}")
print(f"🎂 Age: {age}")


# -------------------------------
# DICTIONARY
# -------------------------------
scores: dict[str, int] = {
    "Umesh": 99,
    "Ravi": 85
}

# Dictionary operations
scores["Anil"] = 90
scores["Ravi"] = 88

print(f"\n📌 Dictionary: {scores}")

# Loop through dictionary
for student, marks in scores.items():
    print(f"🏫 {student} scored {marks}")


# -------------------------------
# TYPE CHECKING (Better Way)
# -------------------------------
print(f"\n🔍 numbers is list? {isinstance(numbers, list)}")
print(f"🔍 person is tuple? {isinstance(person, tuple)}")
print(f"🔍 scores is dict? {isinstance(scores, dict)}")

print("\n✅ Thanks for coding")
print("👋 Goodbye!")
