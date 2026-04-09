# ---------------------------------------
# ALL IN ONE PROGRAM (Optimized)
# ---------------------------------------

numbers = list(range(1, 10))   # Cleaner way to create list
target_indices = {2, 4, 6}     # Use set → faster lookup

print("📋 List:", numbers)


# ---------------------------------------
# 1️⃣ Using enumerate()
# ---------------------------------------
print("\n🔹 Using enumerate():")
for index, item in enumerate(numbers):
    if index in target_indices:
        print(item)


# ---------------------------------------
# 2️⃣ Using slicing (better than range)
# ---------------------------------------
print("\n🔹 Using slicing:")
print(*numbers[2::2])   # start=2, step=2


# ---------------------------------------
# 3️⃣ Using list comprehension
# ---------------------------------------
print("\n🔹 Using list comprehension:")
selected = [numbers[i] for i in sorted(target_indices) if i < len(numbers)]
print(selected)
