age = int(input("Enter the age: "))

if age >= 18:
    if age == 20:
        print("You can enter the event.")
    else:
        print("You need a ticket to enter.")
else:
    print("You are too young to attend the event.")
