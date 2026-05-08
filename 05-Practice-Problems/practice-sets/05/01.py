# -------- DICTIONARY LOOKUP PROGRAM --------

def dictionary_lookup():

    dictionary = {
        "appu": "umesh",
        "harry": "code",
        "kannada": "love"
    }

    word = input("Enter a word: ").lower()

    # get() avoids using if-else
    meaning = dictionary.get(word)

    if meaning:
        print("Meaning:", meaning)
    else:
        print("Word not found")

# Function call
dictionary_lookup()
