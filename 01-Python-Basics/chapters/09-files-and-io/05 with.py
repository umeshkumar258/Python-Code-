# ---------------------------------------
# FILE READING - ALL IN ONE
# ---------------------------------------

filename = "file.txt"

# ---------------------------------------
# 1️⃣ READ ENTIRE FILE
# ---------------------------------------
with open(filename, "r") as f:
    print("📄 Full file content:")
    print(f.read())

# ---------------------------------------
# 2️⃣ READ FIRST N CHARACTERS
# ---------------------------------------
with open(filename, "r") as f:
    content = f.read(10)
    print("\n📌 First 10 characters:")
    print(content)

# ---------------------------------------
# 3️⃣ FILE POINTER MOVEMENT
# ---------------------------------------
with open(filename, "r") as f:
    print("\n📌 File pointer example:")
    print("First 5 chars :", f.read(5))
    print("Next 5 chars  :", f.read(5))
    print("Remaining    :", f.read())

# ---------------------------------------
# 4️⃣ READ LINE BY LINE (readline)
# ---------------------------------------
with open(filename, "r") as f:
    print("\n📌 Reading using readline():")
    print(f.readline(), end="")
    print(f.readline(), end="")

# ---------------------------------------
# 5️⃣ READ ALL LINES (readlines)
# ---------------------------------------
with open(filename, "r") as f:
    print("\n📌 Reading using readlines():")
    lines = f.readlines()
    print(lines, type(lines))

# ---------------------------------------
# 6️⃣ BEST METHOD: READ USING LOOP
# ---------------------------------------
print("\n📌 Reading file using for loop:")
with open(filename, "r") as f:
    for line in f:
        print(line.strip())

# ---------------------------------------
# END OF PROGRAM
# ---------------------------------------
print("\n✅ End of file reading program")
