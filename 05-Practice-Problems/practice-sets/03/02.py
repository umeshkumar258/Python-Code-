# -------- TEMPLATE LETTER PROGRAM --------

def generate_letter():
    print("📨 Letter Generator")
    print("-" * 25)

    name = input("Enter Name: ")
    date = input("Enter Date: ")

    letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

    # Replacing placeholders
    letter = letter.replace("<|Name|>", name)
    letter = letter.replace("<|Date|>", date)

    print("\n📄 Generated Letter")
    print("-" * 25)
    print(letter)

# Function call
generate_letter()
