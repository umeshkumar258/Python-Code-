import os


def list_directory_contents(path):
    if not os.path.exists(path):
        print("❌ Directory does not exist")
        return

    print(f"\n📂 Contents of '{path}':\n")

    contents = os.listdir(path)

    if not contents:
        print("⚠ The directory is empty.")
        return

    for item in contents:
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            print(f"📄 File : {item} ({size} bytes)")
        elif os.path.isdir(full_path):
            print(f"📁 Folder : {item}")


if __name__ == "__main__":
    directory_path = "F:/Reva Python"
    list_directory_contents(directory_path)
