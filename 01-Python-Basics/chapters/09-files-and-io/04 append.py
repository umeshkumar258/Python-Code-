# -----------------------------------
# FILE HANDLING - ALL IN ONE
# -----------------------------------

filename = "file.txt"

# 1. WRITE TO FILE
with open(filename, "w") as file:
    file.write("Hello, this is line 1\n")
    file.write("This is line 2\n")
    file.write("Python file handling example\n")

print("✔ File written successfully\n")


# 2. APPEND TO FILE
with open(filename, "a") as file:
    file.write("\nUmesh is a good student.")

print("✔ Text appended successfully\n")


# 3. READ FULL FILE
with open(filename, "r") as file:
    print("📄 Full File Content:\n")
    print(file.read())


# 4. READ USING readline()
with open(filename, "r") as file:
    print("\n📌 Using readline()\n")

    print(repr(file.readline()))
    print(repr(file.readline()))
    print(repr(file.readline()))


# 5. READ USING readlines()
with open(filename, "r") as file:
    lines = file.readlines()

    print("\n📌 Using readlines()\n")
    print(lines)


# 6. READ USING LOOP
print("\n📌 Using for loop\n")

with open(filename, "r") as file:
    for line in file:
        print(line.strip())


print("\n✅ End of program")
