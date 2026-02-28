# 1️⃣ Multiline string with escape characters
a = "Umesh is a good boy but\nhe has fear of \tfuture."
print("Sentence with escape characters:")
print(a)

# 2️⃣ Using quotes inside string (better way)
b = 'Harry is best teacher of "programming" language.'
print("\nUsing quotes inside string:")
print(b)

# 3️⃣ Formal letter format
letter = """Dear Harry,

This Python course is nice.
    Thanks!
"""
print("\nLetter format:")
print(letter)

# 4️⃣ Using external library (pyjokes)
try:
    import pyjokes
    joke = pyjokes.get_joke()
    print("Random Joke:")
    print(joke)
except ImportError:
    print("pyjokes module not installed. Install using: pip install pyjokes")

# 5️⃣ String concatenation
name = "Umesh"
new = f"Babu\t{name}"
print("\nConcatenated string:")
print(new)

# 6️⃣ f-string (Professional way)
print(f"\nMy name is {name} and Python is awesome!")
