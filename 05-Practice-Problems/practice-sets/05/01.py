# -------- DICTIONARY LOOKUP PROGRAM --------

def dictionary_lookup():
    words = {
        "appu": "umesh",
        "harry": "code",
        "kannada": "love"
    }

    print("📘 Dictionary Lookup")
    print("-" * 30)

    a = input("Enter the word: ").lower()

    if a in words:
        print(f"✅ Meaning: {words[a]}")
    else:
        print("❌ Word not found in dictionary.")

# Function call
dictionary_lookup()
