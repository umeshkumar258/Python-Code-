# Simple Letter Generator

def generate_letter():
    name = input("Enter your name: ")
    date = input("Enter the date: ")

    letter = f"""
Dear {name},

Congratulations! You are selected.

Date: {date}
"""

    print("\nGenerated Letter")
    print("-" * 25)
    print(letter)


# Calling the function
generate_letter()
