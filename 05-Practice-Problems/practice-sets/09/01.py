def search_in_file(filepath, keyword):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        if keyword.lower() in content.lower():
            print(f"'{keyword}' found in the file.")
        else:
            print(f"'{keyword}' not found in the file.")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)


search_in_file("your_file.txt", "umesh")
