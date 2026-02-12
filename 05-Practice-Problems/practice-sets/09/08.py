source_file = "this.txt"
destination_file = "this_copy.txt"

# Read content from the source file
with open(source_file, "r", encoding="utf-8") as file:
    content = file.read()

# Write content to the destination file
with open(destination_file, "w", encoding="utf-8") as file:
    file.write(content)

print("File copied successfully.")
