''' 
1 for snake 
-1 for water
0 for gun
'''

import random

# Mapping choices to numbers
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

# Computer makes a random choice
computer = random.choice([-1, 0, 1])

# Get user input
youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

# Validate input
if youstr not in youDict:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")
else:
    you = youDict[youstr]

    # Display choices
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    # Determine the outcome
    if computer == you:
        print("It's a draw!")
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("You win!")
    else:
        print("You lose!")
