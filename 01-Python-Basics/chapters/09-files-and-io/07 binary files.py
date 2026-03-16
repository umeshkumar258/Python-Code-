# ---------------------------------------
# ALL-IN-ONE FILE HANDLING PROGRAM
# ---------------------------------------

def read_binary_file(file_path):
    """Read a binary file and display its size."""
    try:
        with open(file_path, "rb") as file:
            data = file.read()
            print(f"✅ Binary file '{file_path}' read successfully.")
            print(f"📦 Binary data size: {len(data)} bytes")
    except FileNotFoundError:
        print(f"❌ Binary file '{file_path}' not found.")
    except Exception as error:
        print(f"⚠️ Error while reading binary file: {error}")


def read_text_file(file_path):
    """Read a text file and display its content."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            print(f"\n✅ Text file '{file_path}' read successfully.")
            print("📄 Text file content:")
            print(content)
    except FileNotFoundError:
        print(f"❌ Text file '{file_path}' does not exist.")
    except Exception as error:
        print(f"⚠️ Error while reading text file: {error}")


# ---------------------------------------
# MAIN PROGRAM
# ---------------------------------------
binary_file_path = "appu.jpg"
text_file_path = "nfile.txt"

read_binary_file(binary_file_path)
read_text_file(text_file_path)

print("\n✅ Program finished successfully.")
