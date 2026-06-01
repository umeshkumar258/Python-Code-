try:
    age = int(input("Enter your age: "))

    if age <= 0:
        print("Invalid age")
    elif age < 18:
        print("You are not old enough")
    elif age <= 98:
        print("You are doing good")
    elif age == 99:
        print("Wow! You are 99 years old!")
    else:
        print("You are above 99")

except ValueError:
    print("Please enter a valid age")
