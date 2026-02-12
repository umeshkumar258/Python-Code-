file_name = "log.txt"

# Read the file content
with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

# Check if the word 'python' is present
if "python" in content:
    print("Yes, 'python' is present in the file.")
else:
    print("No, 'python' is not present in the file.")
