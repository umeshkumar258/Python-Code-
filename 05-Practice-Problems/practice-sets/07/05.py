# --------------------------------
# SUM OF N NATURAL NUMBERS
# --------------------------------

# -------- USING WHILE LOOP --------
n = int(input("Enter the number: "))

i = 0
total = 0

while i <= n:
    total += i
    i += 1

print("Sum using while loop:", total)


# -------- USING FOR LOOP --------
n = int(input("\nEnter the number again: "))

total = 0

for i in range(n + 1):   # 0 to n
    total += i

print("Sum using for loop:", total)
