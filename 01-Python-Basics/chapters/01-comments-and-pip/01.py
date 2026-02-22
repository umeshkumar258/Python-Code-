"""
Author: Umesh Kumar J B
Description: Basic Python program demonstrating
- Printing messages
- Multi-line comments
- Taking user input
- Type conversion
"""

def main():
    # Welcome Messages
    print("Hello Umesh!")
    print("Hello Umesh, welcome to Python learning!\n")

    # Personal Introduction
    intro = """
    I am Umesh Kumar J B.
    I am pursuing Engineering at REVA University.
    """
    print(intro)

    # Taking user input safely
    try:
        number = int(input("Enter a number: "))
        print(f"You entered: {number} | Type: {type(number)}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

    print("\nUmesh is continuously learning and improving!")

# Standard Python practice
if __name__ == "__main__":
    main()
