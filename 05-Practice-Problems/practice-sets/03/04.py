# -------- REMOVE DOUBLE SPACE PROGRAM --------

def remove_extra_spaces():
    print("📘 String Space Cleaner")
    print("-" * 30)

    name = "i am fan  of appu sir"

    print("Original String:")
    print(name)

    # Replacing double space with single space
    cleaned_name = name.replace("  ", " ")

    print("\nCleaned String:")
    print(cleaned_name)

    # Extra check
    if "  " in cleaned_name:
        print("❌ Still contains double spaces.")
    else:
        print("✔ Double spaces removed successfully.")

# Function call
remove_extra_spaces()
