# ── 1. Escape Characters ───────────────────────────────────────
sentence = "Umesh is a good boy but\nhe has fear of \tfuture."
print("Escape characters:")
print(sentence)
# \n → newline   \t → tab   \\ → literal backslash   \' \" → quotes

# ── 2. Quotes Inside a String ─────────────────────────────────
quote = 'Harry is the best teacher of "programming".'
print("\nQuotes inside a string:")
print(quote)
# Outer single quotes let inner double quotes sit freely — no escaping needed

# ── 3. Multiline String (Triple Quotes) ───────────────────────
letter = """\
Dear Harry,

This Python course is great.

    Thanks!
"""
print("Formal letter:")
print(letter)
# The backslash after the opening \"\"\" suppresses the leading blank line

# ── 4. f-strings (Recommended since Python 3.6) ───────────────
name = "Umesh"
greeting = f"My name is {name} and Python is awesome!"
print(greeting)

# Expressions work directly inside braces:
print(f"Name length  : {len(name)}")
print(f"Uppercased   : {name.upper()}")
print(f"Inline math  : {7 * 6}")

# ── 5. String Concatenation vs f-strings ──────────────────────
# ❌ Less readable
combined_old = "Babu\t" + name

# ✅ Preferred
combined_new = f"Babu\t{name}"

print(f"\nConcatenated : {combined_old!r}")   # !r shows \t as literal — useful for debugging
print(f"f-string     : {combined_new!r}")

# ── 6. External Library — pyjokes ─────────────────────────────
try:
    import pyjokes
    print(f"\nRandom joke  : {pyjokes.get_joke()}")
except ImportError:
    print("\n[pyjokes not installed] → pip install pyjokes")
