import os

path = "/"

if os.path.isdir(path):
    print("Contents of directory:\n")

    for item in os.listdir(path):
        print(item)
else:
    print("Invalid directory")
