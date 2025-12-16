# ---------------------------------------
# ALL IN ONE FILE HANDLING PROGRAM
# ---------------------------------------

# 1️⃣ READ A BINARY FILE (Image, Audio, etc.)
try:
    with open("appu.jpg", "rb") as file:
        binary_data = file.read()
        print("Binary file read successfully")
        print("Binary data size:", len(binary_data), "bytes")

except FileNotFoundError:
    print("❌ Binary file not found")


# ---------------------------------------
# 2️⃣ READ A TEXT FILE WITH ERROR HANDLING
# ---------------------------------------
try:
    with open("nfile.txt", "r") as file:
        content = file.read()
        print("\nText file content:")
        print(content)

except FileNotFoundError:
    print("❌ The text file does not exist")


# ---------------------------------------
# END OF PROGRAM
# ---------------------------------------
print("\n✅ Program finished successfully")
