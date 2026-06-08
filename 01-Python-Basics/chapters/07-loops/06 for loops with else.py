# List
numbers = [3, 66, 37, 77, 32]

print("Current List:", numbers)

# Check number
def check_number():
    num = int(input("Enter a number to check: "))

    if num in numbers:
        print("Number found!")
        print("Index:", numbers.index(num))
    else:
        print("Number not found!")

# Add number
def add_number():
    num = int(input("Enter a number to add: "))
    numbers.append(num)
    print("Updated List:", numbers)

# Menu
while True:
    print("\n1. Check Number")
    print("2. Add Number")
    print("3. Sort List")
    print("4. Display List")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_number()

    elif choice == "2":
        add_number()

    elif choice == "3":
        print("Sorted List:", sorted(numbers))

    elif choice == "4":
        print("List:", numbers)

    elif choice == "5":
        print("Program Ended")
        break

    else:
        print("Invalid Choice!")
