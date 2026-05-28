# Content to write into the file
content = """
I am Umesh Kumar J B.
I study at REVA University.
I am in CSIT.
Yes, I am good.
Back to work.
"""

# File name
filename = "newfile.txt"

# Write content into the file
with open(filename, "w") as file:
    file.write(content)

print("✅ Data written to the file successfully.")
