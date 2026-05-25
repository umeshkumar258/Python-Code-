# Remove Double Spaces Program

def remove_extra_spaces():
    text = "i am fan  of appu sir"

    print("Original String:")
    print(text)

    # Remove double spaces
    cleaned_text = text.replace("  ", " ")

    print("\nCleaned String:")
    print(cleaned_text)

    # Check result
    if "  " not in cleaned_text:
        print("Double spaces removed successfully.")
    else:
        print("Still contains double spaces.")


# Function call
remove_extra_spaces()
