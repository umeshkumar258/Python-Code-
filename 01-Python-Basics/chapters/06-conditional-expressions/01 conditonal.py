age = int(input("Enter your age: "))

if age <= 0:
    print("You entered an invalid age.")

elif age < 18:
    print("You are a minor.")

elif age == 18:
    print("You just reached the age of consent.")

else:
    print("You are above the age of consent.")
