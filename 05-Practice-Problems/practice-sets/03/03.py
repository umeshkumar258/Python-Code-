# String Find Program

def string_find_demo():
    text = "i am fan of appu sir"

    print("Original String:")
    print(text)

    # Find spaces
    double_space = text.find("  ")
    single_space = text.find(" ")

    print("\nResults")
    print("Double space index :", double_space)
    print("Single space index :", single_space)

    # Check double space
    if double_space == -1:
        print("No double space found.")
    else:
        print("Double space found.")


# Function call
string_find_demo()
