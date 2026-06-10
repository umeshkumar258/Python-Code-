# File Reading Program

file = open("file.txt", "r")

# Read entire file
print("Full Content:")
print(file.read())

file.close()

# Read first 10 characters
file = open("file.txt", "r")
print("\nFirst 10 Characters:")
print(file.read(10))
file.close()

# Read line by line
file = open("file.txt", "r")
print("\nUsing readline():")
print(file.readline(), end="")
print(file.readline(), end="")
file.close()

# Read all lines
file = open("file.txt", "r")
print("\n\nUsing readlines():")
print(file.readlines())
file.close()

# Best method - for loop
print("\nUsing for loop:")
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())

print("\nEnd of Program")
