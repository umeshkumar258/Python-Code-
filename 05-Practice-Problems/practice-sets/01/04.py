import os


def list_directory(path):

    # Check if directory exists
    if not os.path.exists(path):
        print("❌ Directory not found")
        return

    print(f"\n📂 Contents of: {path}\n")

    files = os.listdir(path)

    # Check if empty
    if len(files) == 0:
        print("⚠ Directory is empty")
        return

    # Display contents
    for item in files:

        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            print(f"📄 File   : {item} | {size} bytes")

        elif os.path.isdir(full_path):
            print(f"📁 Folder : {item}")


# Main Program
path = "F:/Reva Python"

list_directory(path)
