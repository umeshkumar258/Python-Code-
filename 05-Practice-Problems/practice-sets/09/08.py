source_file = "this.txt"
copy_file = "this_copy.txt"

# Copy file content
with open(source_file, "r", encoding="utf-8") as source:
    content = source.read()

with open(copy_file, "w", encoding="utf-8") as copy:
    copy.write(content)

print("File copied successfully.")
