# Create empty dictionary
d = {}

# Ask number of entries
n = int(input("How many entries? "))

# Take input from user
for i in range(n):
    print(f"\nEntry {i+1}")

    name = input("Enter name: ").strip()
    language = input("Enter favorite language: ").strip()

    d[name] = language

# Display dictionary
print("\nFinal Dictionary")

for name, language in d.items():
    print(f"{name} : {language}")
