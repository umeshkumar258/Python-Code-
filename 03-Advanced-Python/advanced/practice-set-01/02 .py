# ---------------------------------------
# ALL IN ONE PROGRAM (Improved)
# ---------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_indices = (2, 4, 6)

print("📋 List:", numbers)


# ---------------------------------------
# 1️⃣ Using enumerate()
# ---------------------------------------
print("\n🔹 Using enumerate():")
for index, item in enumerate(numbers):
    if index in target_indices:
        print(item)


# ---------------------------------------
# 2️⃣ Using range()
# ---------------------------------------
print("\n🔹 Using range():")
for i in range(2, len(numbers), 2):
    print(numbers[i])


# ---------------------------------------
# 3️⃣ Using list comprehension
# ---------------------------------------
print("\n🔹 Using list comprehension:")
selected = [numbers[i] for i in target_indices]
print(selected)



