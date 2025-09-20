import os
# Attempt to list the contents of the specified directory
directory_path = "/"

if os.path.exists(directory_path) and os.path.isdir(directory_path):
	contents = os.listdir(directory_path)
	print(contents)
else:
	print(f"Directory '{directory_path}' does not exist.")



# This is also extenla module

