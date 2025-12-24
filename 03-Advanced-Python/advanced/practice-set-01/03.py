# ---------------------------------------
# MULTIPLICATION TABLE - ALL IN ONE
# ---------------------------------------

# Take input
n = int(input("Enter the number: "))

# ---------------------------------------
# 1️⃣ Using list comprehension
# ---------------------------------------
table = [n * i for i in range(1, 11)]
print("\nTable using list comprehension:")
print(table)

# ---------------------------------------
# 2️⃣ Display table line by line
# ---------------------------------------
print("\nFormatted table:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# ---------------------------------------
# 3️⃣ Using for loop to store table
# ---------------------------------------
table_loop = []
for i in range(1, 11):
    table_loop.append(n * i)

print("\nTable using for loop:")
print(table_loop)

# ---------------------------------------
# END OF PROGRAM
# ---------------------------------------
print("\n✅ End of program")
