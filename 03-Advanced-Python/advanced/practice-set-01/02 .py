# ---------------------------------------
# ALL IN ONE PROGRAM
# ---------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("List:", numbers)

# ---------------------------------------
# 1️⃣ Using enumerate()
# ---------------------------------------
print("\nUsing enumerate():")
for index, item in enumerate(numbers):
    if index in (2, 4, 6):
        print(item)

# ---------------------------------------
# 2️⃣ Using range()
# ---------------------------------------
print("\nUsing range():")
for i in range(2, len(numbers), 2):
    print(numbers[i])

# ---------------------------------------
# 3️⃣ Using list comprehension
# ---------------------------------------
print("\nUsing list comprehension:")
selected = [numbers[i] for i in (2, 4, 6)]
print(selected)

# ---------------------------------------
# 4️⃣ enumerate() with start = 1
# ---------------------------------------
print("\nUsing enumerate(start=1):")
for index, item in enumerate(numbers, start=1):
    if index in (3, 5, 7):
        print(item)

# ---------------------------------------
# END OF PROGRAM
# ---------------------------------------
print("\n✅ End of program")
