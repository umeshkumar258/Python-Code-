import random

print("🎮 Welcome to the Number Guessing Game")
print("Guess a number between 1 and 20")

# Generate random number
computer = random.randint(1, 20)

guesses = 0

while True:
    try:
        user = int(input("Enter your guess: "))
        guesses += 1

        if user > computer:
            print("⬇️ You guessed a higher number")
        elif user < computer:
            print("⬆️ You guessed a lower number")
        else:
            print("✅ You guessed the correct number!")
            print(f"🎯 Total attempts: {guesses}")
            break

    except ValueError:
        print("❌ Please enter a valid integer")

print("👋 Game Over. Thanks for playing!")
