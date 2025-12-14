"""
Text files example
Binary files example
Email: umeshkumarjn143@gmail.com
"""

# ---------------------------------------
# OPEN & READ A FILE
# ---------------------------------------

# open() is a built-in function used to open files
# "file.txt" → file name
# "r" → read mode (default)

try:
    with open("file.txt", "r") as f:   # with automatically closes the file
        data = f.read()
        print("File content:\n")
        print(data)

except FileNotFoundError:
    print("❌ File not found. Please check the file name.")

# ---------------------------------------
# WRITE TO A FILE
# ---------------------------------------
with open("file.txt", "w") as f:
    f.write("Hello, this is written using Python file handling.\n")

# ---------------------------------------
# APPEND TO A FILE
# ---------------------------------------
with open("file.txt", "a") as f:
    f.write("This line is appended at the end.\n")

print("\nFile operations completed successfully.")

