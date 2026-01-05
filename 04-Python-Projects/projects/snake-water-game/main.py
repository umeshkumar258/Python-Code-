"""
Rules:
Snake (s)  -> 1
Water (w)  -> -1
Gun (g)    -> 0
"""

import random

# Computer choice
computer = random.choice([-1, 0, 1])

# Dictionaries
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# User input
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Input validation
if youstr not in youDict:
    print("❌ Invalid choice! Please choose s, w, or g.")
else:
    you = youDict[youstr]

    print(f"\nYou chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")

    # Game logic
    if computer == you:
        print("🤝 It's a Draw!")

    elif (computer == -1 and you == 1) or \
         (computer == 1 and you == 0) or \
         (computer == 0 and you == -1):
        print("🎉 You Win!")

    else:
        print("😢 You Lose!")
