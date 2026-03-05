try:
    age = int(input("Enter your age: "))

    if age < 18:
        print("You are too young to attend the event.")

    elif age == 20:
        print("You can enter the event.")

    elif age > 20:
        print("You need a ticket to enter.")

    else:
        print("You can attend, but rules may apply.")

except ValueError:
    print("❗ Please enter a valid number for age.")
