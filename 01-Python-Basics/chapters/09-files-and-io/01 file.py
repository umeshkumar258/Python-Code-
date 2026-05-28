# -----------------------------------
# SIMPLE FILE HANDLING PROGRAM
# -----------------------------------

filename = "file.txt"

# WRITE TO FILE
with open(filename, "w") as file:
    file.write("Hello, this is written using Python.\n")

# APPEND TO FILE
with open(filename, "a") as file:
    file.write("This line is added later.\n")

# READ FROM FILE
try:
    with open(filename, "r") as file:
        print("📄 File Content:\n")
        print(file.read())

except FileNotFoundError:
    print("❌ File not found.")

print("\n✅ File operations completed successfully.")
