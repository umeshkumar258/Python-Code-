# Tuple Immutability Demo

def tuple_demo():

    # Create a tuple
    numbers = (10, 20, 30)

    print("Original Tuple:", numbers)

    # Try to change the tuple
    try:
        numbers[0] = 100

    except TypeError:
        print("❌ Tuples cannot be changed!")

    # Tuple is still the same
    print("Final Tuple:", numbers)


# Function call
tuple_demo()
