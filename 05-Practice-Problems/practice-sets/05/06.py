# Create empty dictionary
d = {}

print("Enter 5 name and language pairs")
print("-" * 35)

# Taking input
for i in range(5):
    name = input("Enter name: ")
    language = input("Enter language: ")

    d[name] = language   # Adds or updates value
    print()

# Display dictionary
print("-" * 35)
print("Final Dictionary:")

for key, value in d.items():
    print(key, ":", value)

print("\nTotal entries:", len(d))
