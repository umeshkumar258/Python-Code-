# Ask the user to enter age
age = int(input("Enter your age: "))

# Check age conditions
if age <= 0:
    print("Invalid age. Age must be greater than 0.")

elif age < 18:
    print("You are a minor.")

elif age == 18:
    print("You have just reached the age of consent.")

else:
    print("You are above the age of consent.")
