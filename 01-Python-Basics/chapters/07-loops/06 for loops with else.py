# ---------------------------------------
# LIST
# ---------------------------------------
numbers = [3, 66, 37, 77, 32]

print("List items:")
for num in numbers:
    print(num)


# ---------------------------------------
# FUNCTION → Check number in list
# ---------------------------------------
def check_number(lst):
    try:
        user_num = int(input("\nEnter a number to check in the list: "))

        if user_num in lst:
            print("✔ It is in the list!")
            print(f"Found at index: {lst.index(user_num)}")
        else:
            print("✘ It is NOT in the list!")

        print(f"Occurrence count: {lst.count(user_num)}")

    except ValueError:
        print("Please enter a valid number!")


# ---------------------------------------
# FUNCTION → Add number to list
# ---------------------------------------
def add_number(lst):
    try:
        new_val = int(input("\nEnter a number to add to the list: "))
        lst.append(new_val)
        print("Updated list:", lst)

    except ValueError:
        print("Invalid input! Please enter a number.")


# ---------------------------------------
# RUN PROGRAM
# ---------------------------------------
check_number(numbers)

print("\nSorted list:", sorted(numbers))

add_number(numbers)
