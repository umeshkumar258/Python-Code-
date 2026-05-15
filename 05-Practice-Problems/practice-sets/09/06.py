file_name = "log.txt"

# Read file
with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

# Check word
if "python" in content:
    print("Python found.")
else:
    print("Python not found.")
