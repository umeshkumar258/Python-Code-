import os

file_path = 'myfile.txt'

# Get file size
print(f"File size: {os.path.getsize(file_path)} bytes")

# Get last modification time
print(f"Last modified: {os.path.getmtime(file_path)}")

# Check if file exists
print(f"File exists: {os.path.exists(file_path)}")
