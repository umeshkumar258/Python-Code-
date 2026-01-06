text = "umesh twinkle twinkle little star"

print("Original text:", text)
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())
print("After replace:", text.replace("umesh", "hello"))
print("Contains 'twinkle':", "twinkle" in text)
print("Split words:", text.split())

print("\nWords one by one:")
for word in text.split():
    print(word)

print("\n✨ End of Program ✨")
