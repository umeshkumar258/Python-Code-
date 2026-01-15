# ---------- DICTIONARY CREATION ----------
d = {}

print("Enter name and language details")
print("-" * 35)

# ---------- INPUT USING LOOP ----------
for i in range(5):
    name = input(f"Enter name {i+1}: ").strip()
    language = input(f"Enter language {i+1}: ").strip()

    # Check for duplicate name
    if name in d:
        print("⚠ Name already exists. Value will be updated.")

    d[name] = language
    print()

# ---------- OUTPUT ----------
print("-" * 35)
print("Final Dictionary:")

for name, language in d.items():
    print(f"{name} : {language}")

print("\nType of d:", type(d))
print("Total entries:", len(d))
