import os
import time

file_path = "myfile.txt"

# ---------------------------------------
# 1️⃣ Check if file exists
# ---------------------------------------
if os.path.exists(file_path):
    print("✔ File exists")

    # ---------------------------------------
    # 2️⃣ File size
    # ---------------------------------------
    size = os.path.getsize(file_path)
    print(f"File size: {size} bytes")

    # ---------------------------------------
    # 3️⃣ Last modification time
    # ---------------------------------------
    modified_time = os.path.getmtime(file_path)
    print("Last modified:",
          time.ctime(modified_time))

    # ---------------------------------------
    # 4️⃣ File creation time (OS dependent)
    # ---------------------------------------
    created_time = os.path.getctime(file_path)
    print("Created on:",
          time.ctime(created_time))

    # ---------------------------------------
    # 5️⃣ Absolute path of file
    # ---------------------------------------
    print("Absolute path:",
          os.path.abspath(file_path))

    # ---------------------------------------
    # 6️⃣ Check file or directory
    # ---------------------------------------
    print("Is file:", os.path.isfile(file_path))
    print("Is directory:", os.path.isdir(file_path))

else:
    print("❌ File does not exist")
