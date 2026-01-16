# Dictionary to store name-language pairs
d = {}

# Number of entries the user wants to add
n = int(input("How many entries do you want to add? "))

for i in range(n):
    name = input(f"\nEnter name {i+1}: ").strip()
    language = input(f"Enter {name}'s favorite language: ").strip()

    # Check if name already exists
    if name in d:
        print("⚠️ Name already exists. Updating the language.")

    d[name] = language

# Display final dictionary
print("\n📘 Final Dictionary:")
for name, language in d.items():
    print(f"{name} → {language}")
