try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Invalid age")
    elif age < 18:
        print("You are too young to attend the event")
    elif age <= 20:
        print("You can enter the event")
    else:
        print("You need a ticket to enter")

except ValueError:
    print("Please enter a valid number")
