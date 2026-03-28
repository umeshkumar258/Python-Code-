# Take input from user
names = input("Enter names separated by space: ").split()

# Join list elements using "::"
joined_names = "::".join(names)

# Output
print(f"Original list: {names}")
print(f"Joined string: {joined_names}")
print(f"Type of names: {type(names)}")
