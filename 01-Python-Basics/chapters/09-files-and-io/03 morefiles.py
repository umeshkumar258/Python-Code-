# -----------------------------------
# FILE HANDLING PROGRAM
# -----------------------------------

filename = "file.txt"


# WRITE TO FILE
def write_file():
    with open(filename, "w") as file:
        file.write("Hello, this is line 1\n")
        file.write("This is line 2\n")
        file.write("Python file handling\n")

    print("✔ File written successfully\n")


# APPEND TO FILE
def append_file():
    with open(filename, "a") as file:
        file.write("This line is appended\n")

    print("✔ Data appended successfully\n")


# READ FULL FILE
def read_file():
    with open(filename, "r") as file:
        print("📄 Full File Content:\n")
        print(file.read())


# READ USING READLINE
def read_line():
    with open(filename, "r") as file:
        print("📌 Using readline()\n")

        print(file.readline().strip())
        print(file.readline().strip())
        print(file.readline().strip())


# READ USING READLINES
def read_lines():
    with open(filename, "r") as file:
        lines = file.readlines()

        print("\n📌 Using readlines()")
        print(lines)


# READ USING LOOP
def read_loop():
    with open(filename, "r") as file:
        print("\n📌 Using for loop")

        for line in file:
            print(line.strip())


# MAIN FUNCTION
def main():
    try:
        write_file()
        append_file()

        read_file()
        read_line()
        read_lines()
        read_loop()

        print("\n✅ Program completed successfully")

    except FileNotFoundError:
        print("❌ File not found")

    except Exception as e:
        print("❌ Error:", e)


# RUN PROGRAM
if __name__ == "__main__":
    main()
