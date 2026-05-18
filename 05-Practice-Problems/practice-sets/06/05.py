# Tuple of names
names = ("umesh", "appu", "babu", "harry")

# User input
name = input("Enter a name: ").lower()

# Checking name
if name in names:
    print("Name found")
else:
    print("Name not found")
