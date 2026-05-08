# -------- SET INPUT PROGRAM --------

def set_demo():

    numbers = set()

    for i in range(5):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.add(num)

    print("\nUnique numbers:", numbers)

# Function call
set_demo()
