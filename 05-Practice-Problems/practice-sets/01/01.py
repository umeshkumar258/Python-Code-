# Store the string
text = "Umesh twinkle twinkle little star 🌟"

# Print original text
print("Original Text:")
print(text)

# Length of the string
print("\nLength of text:", len(text))

# Convert to uppercase
print("\nUppercase:")
print(text.upper())

# Convert to lowercase
print("\nLowercase:")
print(text.lower())

# Capitalize first letter
print("\nCapitalized:")
print(text.capitalize())

# Title case
print("\nTitle Case:")
print(text.title())

# Replace a word
print("\nAfter Replacement:")
print(text.replace("Umesh", "Hello"))

# Check if a word exists
word = "twinkle"
print(f"\nDoes the word '{word}' exist?", word in text)

# Split the string into words
print("\nWords in the text:")
print(text.split())

# Print each word on a new line
print("\nWords printed line by line:")
for w in text.split():
    print(w)

# Add a decorative line
print("\n✨ End of Program ✨")
