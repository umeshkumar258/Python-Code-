# ---------------------------------------
# FILE HANDLING – ALL IN ONE
# ---------------------------------------

filename = "file.txt"


def write_file(file_name):
    """Write initial content to the file."""
    try:
        with open(file_name, "w") as file:
            file.write("Hello, this is line 1\n")
            file.write("This is line 2\n")
            file.write("Python file handling\n")
        print("✔ File written successfully\n")
    except Exception as e:
        print(f"❌ Error while writing file: {e}\n")


def append_file(file_name):
    """Append new content to the file."""
    try:
        with open(file_name, "a") as file:
            file.write("This line is appended\n")
        print("✔ Data appended successfully\n")
    except Exception as e:
        print(f"❌ Error while appending file: {e}\n")


def read_full_file(file_name):
    """Read and display the full file content."""
    try:
        with open(file_name, "r") as file:
            data = file.read()
            print("📄 Full file content:")
            print(data)
    except FileNotFoundError:
        print("❌ File not found\n")
    except Exception as e:
        print(f"❌ Error while reading file: {e}\n")


def read_using_readline(file_name):
    """Read file line by line using readline()."""
    try:
        with open(file_name, "r") as file:
            print("📌 Reading using readline():")
            line1 = file.readline()
            line2 = file.readline()
            line3 = file.readline()

            print(line1, type(line1))
            print(line2, type(line2))
            print(line3, type(line3))
    except FileNotFoundError:
        print("❌ File not found\n")
    except Exception as e:
        print(f"❌ Error while using readline(): {e}\n")


def read_using_readlines(file_name):
    """Read all lines into a list using readlines()."""
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            print("\n📌 Reading using readlines():")
            print(lines, type(lines))
    except FileNotFoundError:
        print("❌ File not found\n")
    except Exception as e:
        print(f"❌ Error while using readlines(): {e}\n")


def read_using_loop(file_name):
    """Read file line by line using a loop."""
    try:
        print("\n📌 Reading file using for loop:")
        with open(file_name, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("❌ File not found\n")
    except Exception as e:
        print(f"❌ Error while reading with loop: {e}\n")


def main():
    """Main function to run all file handling operations."""
    write_file(filename)
    append_file(filename)
    read_full_file(filename)
    read_using_readline(filename)
    read_using_readlines(filename)
    read_using_loop(filename)

    print("\n✅ End of file handling program")


# Run the program
if __name__ == "__main__":
    main()
