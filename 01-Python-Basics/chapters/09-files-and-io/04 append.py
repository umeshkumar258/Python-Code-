# ---------------------------------------
# FILE HANDLING - ALL IN ONE PROGRAM
# ---------------------------------------

filename = "file.txt"

# ---------------------------------------
# 1. WRITE TO FILE (w mode)
# ---------------------------------------
with open(filename, "w") as file:
    file.write("Hello, this is line 1\n")
    file.write("This is line 2\n")
    file.write("Python file handling example\n")

print("✔ File written successfully\n")

# ---------------------------------------
# 2. APPEND TO FILE (a mode)
# ---------------------------------------
append_text = "\nUmesh is a cute boy"

with open(filename, "a") as file:
    file.write(append_text)

print("✔ Text appended successfully\n")

# ---------------------------------------
# 3. READ ENTIRE FILE
# ---------------------------------------
with open(filename, "r") as file:
    content = file.read()
    print("📄 Full file content:")
    print(content)

# ---------------------------------------
# 4. READ LINE BY LINE USING readline()
# ---------------------------------------
with open(filename, "r") as file:
    print("\n📌 Reading using readline():")
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()

    print(repr(line1), type(line1))
    print(repr(line2), type(line2))
    print(repr(line3), type(line3))

# ---------------------------------------
# 5. READ ALL LINES USING readlines()
# ---------------------------------------
with open(filename, "r") as file:
    all_lines = file.readlines()
    print("\n📌 Reading using readlines():")
    print(all_lines, type(all_lines))

# ---------------------------------------
# 6. READ USING LOOP (BEST METHOD)
# ---------------------------------------
print("\n📌 Reading file using for loop:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())

# ---------------------------------------
# END OF PROGRAM
# ---------------------------------------
print("\n✅ End of file handling program")
