number = int(input("Enter the number: "))  # Get input from the user

# Loop through numbers from 0 to the input number
for i in range(number):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
