import random

print("🎮 Welcome to Gun–Water–Snake Game")

# Computer choice
computer = random.randint(1, 3)

# Dictionary for choices
choices = {
    1: "Gun",
    2: "Water",
    3: "Snake"
}

try:
    # User input
    user = int(input("Enter your choice (1 = Gun, 2 = Water, 3 = Snake): "))

    if user not in choices:
        print("❌ Invalid input! Please enter 1, 2, or 3.")
    else:
        print(f"\nComputer chose: {choices[computer]}")
        print(f"You chose: {choices[user]}")

        # Game logic
        if computer == user:
            print("🤝 It's a Tie!")
        elif (computer == 1 and user == 3) or \
             (computer == 2 and user == 1) or \
             (computer == 3 and user == 2):
            print("💻 Computer Wins!")
        else:
            print("🎉 You Win!")

except ValueError:
    print("❌ Please enter a valid number")
