# Simple String Operations Program

text = "Umesh twinkle twinkle little star 🌟"

# Original text
print("Original Text:", text)

# Length
print("Length:", len(text))

# Uppercase and lowercase
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Capitalize and title case
print("Capitalized:", text.capitalize())
print("Title Case:", text.title())

# Replace word
new_text = text.replace("Umesh", "Hello")
print("After Replace:", new_text)

# Check word
print("Contains 'twinkle'?", "twinkle" in text)

# Split into words
words = text.split()

print("Words:", words)

# Print words line by line
print("\nWords one by one:")
for word in words:
    print(word)

print("\n✨ End of Program ✨")
