def analyze_text(text):
    print("✨ TEXT ANALYSIS ✨\n")

    print(f"Original text : {text}")
    print(f"Length        : {len(text)}")
    print(f"Uppercase     : {text.upper()}")
    print(f"Lowercase     : {text.lower()}")
    print(f"Title case    : {text.title()}")
    print(f"After replace : {text.replace('umesh', 'hello')}")
    print(f"Contains 'twinkle': {'Yes' if 'twinkle' in text else 'No'}")

    # Store split result (avoid repeating)
    words = text.split()

    print(f"Split words   : {words}")

    print("\nWords one by one:")
    for word in words:
        print(f"- {word}")

    print("\n✨ End of Program ✨")


# Main
text = "umesh twinkle twinkle little star"
analyze_text(text)
