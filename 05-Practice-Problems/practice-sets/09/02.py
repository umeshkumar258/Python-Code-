import random

HISCORE_FILE = "hiscore.txt"
MIN_SCORE = 1
MAX_SCORE = 59


def get_hiscore() -> int:
    """Read the high score from file, return 0 if file is missing or empty."""
    try:
        with open(HISCORE_FILE, "r") as f:
            content = f.read().strip()
            return int(content) if content else 0
    except (FileNotFoundError, ValueError):
        return 0


def save_hiscore(score: int) -> None:
    """Save the new high score to file."""
    with open(HISCORE_FILE, "w") as f:
        f.write(str(score))


def game() -> int:
    """Play a round and return the player's score."""
    print("You are playing the game...")

    score = random.randint(MIN_SCORE, MAX_SCORE)
    hiscore = get_hiscore()

    print(f"Your score : {score}")
    print(f"High score : {hiscore}")

    if score > hiscore:
        save_hiscore(score)
        print(f"🎉 New high score! {score} beats the old record of {hiscore}.")
    else:
        print(f"You need {hiscore - score + 1} more points to beat the high score.")

    return score


if __name__ == "__main__":
    game()
