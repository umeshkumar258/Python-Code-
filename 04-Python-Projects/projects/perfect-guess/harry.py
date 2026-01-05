import random

def play_game():
    print("\n🎮 Welcome to the Number Guessing Game")

    # Difficulty levels
    print("\nChoose Difficulty Level")
    print("1. Easy (1–10, 5 attempts)")
    print("2. Medium (1–20, 7 attempts)")
    print("3. Hard (1–50, 10 attempts)")

    level = int(input("Enter your choice (1/2/3): "))

    if level == 1:
        max_num = 10
        max_attempts = 5
    elif level == 2:
        max_num = 20
        max_attempts = 7
    else:
        max_num = 50
        max_attempts = 10

    number = random.randint(1, max_num)
    attempts = 0

    print(f"\n🔢 Guess the number between 1 and {max_num}")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess > number:
                print("⬇️ Lower number please")
            elif guess < number:
                print("⬆️ Higher number please")
            else:
                print(f"\n🎉 Correct! You guessed it in {attempts} attempts")
                return

            print(f"Attempts left: {max_attempts - attempts}")

        except ValueError:
            print("❌ Enter only numbers")

    print(f"\n😢 Game Over! The correct number was {number}")

# Replay option
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("\n👋 Thanks for playing!")
        break
