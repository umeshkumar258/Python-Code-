import os

# Directory path to list
directory_path = "/"

# Check if path exists and is a directory
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    print(f"Contents of '{directory_path}':\n")
    
    contents = os.listdir(directory_path)

    if not contents:
        print("Directory is empty.")
    else:
        for item in contents:
            print(item)
else:
    print(f"Directory '{directory_path}' does not exist or is not a directory.")
