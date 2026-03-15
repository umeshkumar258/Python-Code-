# ---------------------------------------
# FILE READING - ALL IN ONE
# ---------------------------------------

filename = "file.txt"

# ---------------------------------------
# 1. READ ENTIRE FILE
# ---------------------------------------
with open(filename, "r") as file:
    print("📄 Full file content:")
    print(file.read())

# ---------------------------------------
# 2. READ FIRST N CHARACTERS
# ---------------------------------------
with open(filename, "r") as file:
    first_10_chars = file.read(10)
    print("\n📌 First 10 characters:")
    print(first_10_chars)

# ---------------------------------------
# 3. FILE POINTER MOVEMENT
# ---------------------------------------
with open(filename, "r") as file:
    print("\n📌 File pointer example:")
    first_5 = file.read(5)
    next_5 = file.read(5)
    remaining = file.read()

    print("First 5 chars :", first_5)
    print("Next 5 chars  :", next_5)
    print("Remaining     :", remaining)

# ---------------------------------------
# 4. READ LINE BY LINE USING readline()
# ---------------------------------------
with open(filename, "r") as file:
    print("\n📌 Reading using readline():")
    line1 = file.readline()
    line2 = file.readline()

    print(line1, end="")
    print(line2, end="")

# ---------------------------------------
# 5. READ ALL LINES USING readlines()
# ---------------------------------------
with open(filename, "r") as file:
    all_lines = file.readlines()
    print("\n📌 Reading using readlines():")
    print(all_lines, type(all_lines))

# ---------------------------------------
# 6. BEST METHOD: READ USING LOOP
# ---------------------------------------
print("\n📌 Reading file using for loop:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())

# ---------------------------------------
# END OF PROGRAM
# ---------------------------------------
print("\n✅ End of file reading program")
