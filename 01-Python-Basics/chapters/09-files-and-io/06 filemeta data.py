import os
import time

file = "myfile.txt"

if os.path.exists(file):
    print("File exists")

    print("Size:", os.path.getsize(file), "bytes")
    print("Modified:", time.ctime(os.path.getmtime(file)))
    print("Created:", time.ctime(os.path.getctime(file)))
    print("Path:", os.path.abspath(file))
else:
    print("File does not exist")
