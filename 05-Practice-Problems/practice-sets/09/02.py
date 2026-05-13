import random

HISCORE_FILE = "hiscore.txt"
MIN_SCORE = 1
MAX_SCORE = 59


def get_hiscore():
    """Return high score from file."""
    try:
        with open(HISCORE_FILE, "r") as file:
            return int(file.read().strip())

    except (FileNotFoundError, ValueError):
        return 0


def save_hiscore(score):
    """Save high score to file."""
    with open(HISCORE_FILE, "w") as file:
        file.write(str(score))


def game():
    """Play the game."""

    print("🎮 You are playing the game...\n")

    score = random.randint(MIN_SCORE, MAX_SCORE)
    hiscore = get_hiscore()

    print(f"Your score : {score}")
    print(f"High score : {hiscore}")

    if score > hiscore:
        save_hiscore(score)
        print("\n🎉 New High Score!")
    else:
        print(f"\nYou need {hiscore - score + 1} more points to beat the high score.")

    return score


if __name__ == "__main__":
    game()
