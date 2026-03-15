import os
import time

file_path = "myfile.txt"

# ---------------------------------------
# FILE INFORMATION PROGRAM
# ---------------------------------------

if os.path.exists(file_path):
    print("✔ File exists")

    file_size = os.path.getsize(file_path)
    last_modified = os.path.getmtime(file_path)
    created_on = os.path.getctime(file_path)
    absolute_path = os.path.abspath(file_path)

    print(f"File size       : {file_size} bytes")
    print(f"Last modified   : {time.ctime(last_modified)}")
    print(f"Created on      : {time.ctime(created_on)}")
    print(f"Absolute path   : {absolute_path}")
    print(f"Is file         : {os.path.isfile(file_path)}")
    print(f"Is directory    : {os.path.isdir(file_path)}")

else:
    print("❌ File does not exist")
