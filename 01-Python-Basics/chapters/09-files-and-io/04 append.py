# ---------------------------------------
# FILE HANDLING - ALL IN ONE PROGRAM
# ---------------------------------------

filename = "file.txt"

# ---------------------------------------
# 1️⃣ WRITE TO FILE (w mode)
# ---------------------------------------
with open(filename, "w") as f:
    f.write("Hello, this is line 1\n")
    f.write("This is line 2\n")
    f.write("Python file handling example\n")

print("✔ File written successfully\n")

# ---------------------------------------
# 2️⃣ APPEND TO FILE (a mode)
# ---------------------------------------
append_text = "\nUmesh is a cute boy"
with open(filename, "a") as f:
    f.write(append_text)

print("✔ Text appended successfully\n")

# ---------------------------------------
# 3️⃣ READ ENTIRE FILE (read)
# ---------------------------------------
with open(filename, "r") as f:
    data = f.read()
    print("📄 Full file content:")
    print(data)

# ---------------------------------------
# 4️⃣ READ LINE BY LINE (readline)
# ---------------------------------------
with open(filename, "r") as f:
    print("\n📌 Reading using readline():")
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()

    print(line1, type(line1))
    print(line2, type(line2))
    print(line3, type(line3))

# ---------------------------------------
# 5️⃣ READ ALL LINES (readlines)
# ---------------------------------------
with open(filename, "r") as f:
    lines = f.readlines()
    print("\n📌 Reading using readlines():")
    print(lines, type(lines))

# ---------------------------------------
# 6️⃣ READ USING LOOP (BEST METHOD)
# ---------------------------------------
print("\n📌 Reading file using for loop:")
with open(filename, "r") as f:
    for line in f:
        print(line.strip())

# ---------------------------------------
# END OF PROGRAM
# ---------------------------------------
print("\n✅ End of file handling program")
