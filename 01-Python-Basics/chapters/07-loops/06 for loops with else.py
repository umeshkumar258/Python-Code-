# ---------------------------------------
# LIST
# ---------------------------------------
numbers = [3, 66, 37, 77, 32]

print("List items:")
for num in numbers:
    print(num)

# ---------------------------------------
# USER INPUT CHECK
# ---------------------------------------
try:
    user_num = int(input("\nEnter a number to check in the list: "))

    if user_num in numbers:
        print("✔ It is there in the list!")
    else:
        print("✘ It is NOT in the list!")

except ValueError:
    print("Please enter a valid number!")

# ---------------------------------------
# EXTRA FEATURE 1 → Count how many times it appears
# ---------------------------------------
print(f"Occurrence count: {numbers.count(user_num)}")

# ---------------------------------------
# EXTRA FEATURE 2 → Show index if it exists
# ---------------------------------------
if user_num in numbers:
    print(f"Found at index: {numbers.index(user_num)}")

# ---------------------------------------
# EXTRA FEATURE 3 → Sorting the list
# ---------------------------------------
print("\nSorted list:", sorted(numbers))

# ---------------------------------------
# EXTRA FEATURE 4 → Add a new number to list
# ---------------------------------------
new_val = int(input("\nEnter a number to add to the list: "))
numbers.append(new_val)
print("Updated list:", numbers)
