line_number = 2

with open("log.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Check line exists
if line_number <= len(lines):

    # Get the line
    line = lines[line_number - 1]

    # Check word
    if "python" in line.lower():
        print(f"'python' found in line {line_number}")
    else:
        print(f"'python' not found in line {line_number}")

else:
    print("Line does not exist.")
