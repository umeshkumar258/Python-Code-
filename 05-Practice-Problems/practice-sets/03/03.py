# -------- STRING FIND PROGRAM --------

def string_find_demo():
    print("📘 String Find Operation")
    print("-" * 30)

    name = "i am fan  of appu sir"

    print("Original String:")
    print(name)

    # Finding double space
    double_space_index = name.find("  ")

    # Finding single space
    single_space_index = name.find(" ")

    print("\n📊 Results")
    print(f"Index of double space  : {double_space_index}")
    print(f"Index of single space  : {single_space_index}")

    # Extra explanation
    if double_space_index != -1:
        print("✔ Double space found in the string.")
    else:
        print("❌ No double space found.")

# Function call
string_find_demo()
