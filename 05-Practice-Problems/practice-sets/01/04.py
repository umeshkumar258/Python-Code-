import os

# Directory path
directory_path = "F:/Reva Python"

# Check if directory exists
if os.path.exists(directory_path):
    print(f"Contents of '{directory_path}':\n")

    contents = os.listdir(directory_path)

    # If directory is empty
    if not contents:
        print("The directory is empty.")
    else:
        for item in contents:
            print(item)
else:
    print("Directory does not exist ❌")
