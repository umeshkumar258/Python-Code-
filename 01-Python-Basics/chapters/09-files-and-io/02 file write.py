content = "I am Umesh Kumar J B. I study at REVA University. I am in CSIT. Yes, I am good. Back to work."

filename = "newfile.txt"

with open(filename, "w") as file:
    file.write(content)

print("Data written to the file successfully.")
