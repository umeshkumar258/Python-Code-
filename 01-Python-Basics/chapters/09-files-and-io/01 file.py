"""
Text file handling example
"""

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

# ---------------------------------------
# OPEN & READ A FILE
# ---------------------------------------
try:
    with open("file.txt", "r") as f:
        data = f.read()
        print("File content:\n")
        print(data)

except FileNotFoundError:
    print("File not found. Please check the file name.")

print("\nFile operations completed successfully.")
