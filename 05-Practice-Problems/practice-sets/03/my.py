# -------- STRING PRACTICE PROGRAM --------

def string_practice():
    print("📘 STRING PRACTICE PROGRAM")
    print("=" * 35)

    # 1️⃣ Letter template replacement
    letter_template = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
    final_letter = letter_template.replace("Name", "Umesh").replace("Date", "12")

    print("\n📄 Generated Letter")
    print(final_letter)

    # 2️⃣ Finding double space
    a = "umesh  kumar"
    double_space_index = a.find("  ")

    print("🔍 Double space index:", double_space_index)

    # 3️⃣ Removing double space
    cleaned_name = a.replace("  ", " ")
    print("✂ Cleaned String:", cleaned_name)

    # 4️⃣ Escape sequence example
    letter = "Dear Harry\nthis python course is nice.\nThanks!"
    print("\n📧 Formatted Letter")
    print(letter)

# Function call
string_practice()
