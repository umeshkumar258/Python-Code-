def analyze_text(text):
    print("\n✨ TEXT ANALYSIS ✨\n")

    # Basic operations
    print("Original Text :", text)
    print("Length        :", len(text))
    print("Uppercase     :", text.upper())
    print("Lowercase     :", text.lower())
    print("Title Case    :", text.title())

    # Replace word
    new_text = text.replace("umesh", "hello")
    print("After Replace :", new_text)

    # Check word
    if "twinkle" in text:
        print("Contains 'twinkle' : Yes")
    else:
        print("Contains 'twinkle' : No")

    # Split words
    words = text.split()

    print("\nWords in Text:")
    for word in words:
        print(word)

    print("\n✨ End of Program ✨")


# Main Program
text = "umesh twinkle twinkle little star"
analyze_text(text)
