def read_binary(file):
    try:
        with open(file, "rb") as f:
            data = f.read()
            print("Binary file read successfully")
            print("Size:", len(data), "bytes")
    except FileNotFoundError:
        print("Binary file not found")


def read_text(file):
    try:
        with open(file, "r") as f:
            print("\nText File Content:")
            print(f.read())
    except FileNotFoundError:
        print("Text file not found")


read_binary("appu.jpg")
read_text("nfile.txt")

print("\nProgram Finished")
