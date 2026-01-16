# Create an empty dictionary
d = {}

# Take input two times using a loop
for i in range(2):
    name = input("Enter the name: ")
    language = input("Enter the language: ")
    d[name] = language   # Direct assignment is better than update()

# Print the dictionary
print(d)
