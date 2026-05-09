# Empty dictionary
d = {}

# Number of entries
n = int(input("How many entries? "))

# Input section
for i in range(n):
    name = input("Enter name: ")
    language = input("Enter favorite language: ")

    d[name] = language   # Add or update

# Output section
print("\nFinal Dictionary:")

for name, language in d.items():
    print(name, ":", language)
