"""
Greeting Program
Author: Umesh
Description: Greets multiple users with input validation
"""


# ---------------------------------------
# Function to get valid name
# ---------------------------------------
def get_name(index: int) -> str:
    """Takes user input and ensures it is not empty"""
    while True:
        name = input(f"Enter name {index}: ").strip()
        if name:
            return name
        print("❌ Name cannot be empty. Please try again.")


# ---------------------------------------
# Function to greet user
# ---------------------------------------
def good_day(name: str) -> None:
    """Greets the user"""
    print(f"Good morning, {name}! 😊")


# ---------------------------------------
# Main Program
# ---------------------------------------
def main() -> None:
    """Main execution function"""
    print("🔹 Greeting Program\n")

    for i in range(1, 4):
        name = get_name(i)
        good_day(name)

    print("\n✅ All greetings completed!")


# Run the program
if __name__ == "__main__":
    main()
