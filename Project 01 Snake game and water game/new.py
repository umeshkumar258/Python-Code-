import random

# Dictionary to map numbers to choices
choices = {1: "snake", 2: "water", 3: "gun"}

# Get input from user
user = int(input("Enter a number (1: Snake, 2: Water, 3: Gun): "))
computer = random.randint(1, 3)

# Show choices
print(f"You chose: {choices[user]}")
print(f"Computer chose: {choices[computer]}")

# Game logic
if user == computer:
    print("It's a tie!")
elif (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
    print("You win!")
else:
    print("You lose!")
