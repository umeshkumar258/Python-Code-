line_number = 2

with open("log.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

    if len(lines) >= line_number:
        line_text = lines[line_number - 1]

        if "python" in line_text.lower():
            print(f"Yes, 'python' is present. Line no: {line_number}")
        else:
            print("No, 'python' is not present on the given line.")
    else:
        print("The file does not have that many lines.")
