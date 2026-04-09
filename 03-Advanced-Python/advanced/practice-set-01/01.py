from pathlib import Path

def read_files(file_list):
    for file_name in file_list:
        file_path = Path(file_name)

        print(f"\n📄 Reading {file_name}:")

        if not file_path.exists():
            print(f"❌ {file_name} not found")
            continue

        try:
            with file_path.open("r", encoding="utf-8") as file:
                content = file.read().strip()

                if content:
                    print(content)
                else:
                    print("⚠ File is empty")

        except PermissionError:
            print(f"⚠ Permission denied for {file_name}")
        except Exception as error:
            print(f"⚠ Error in {file_name}: {error}")


# File list
files = ["9.txt", "0.txt", "6.txt"]

# Run function
read_files(files)

print("\n🙏 Thanks")
