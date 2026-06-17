# Simple Age Check Program

try:
    age = int(input("Enter your age: "))

    if age < 18:
        print("Too young to attend.")

    elif age == 20:
        print("You can enter.")

    elif age > 20:
        print("You need a ticket.")

    else:
        print("Rules may apply.")

except ValueError:
    print("Please enter a valid age.")
