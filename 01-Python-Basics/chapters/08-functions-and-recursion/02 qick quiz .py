# ---------------------------------------
# Function Definition
# ---------------------------------------
def good_day(name):
    """Greets the user"""
    print(f"Good morning, {name}! 😊")


# ---------------------------------------
# Main Program
# ---------------------------------------
def main():
    for i in range(3):
        name = input(f"Enter name {i+1}: ")
        good_day(name)


# Run the program
if __name__ == "__main__":
    main()
