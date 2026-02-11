def search_in_file(filepath: str, keyword: str) -> None:
    """Read a file and check if a keyword exists in its content."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        print(content)

        if keyword.lower() in content.lower():
            print(f"'{keyword}' was found in the file.")
        else:
            print(f"'{keyword}' was not found in the file.")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except IOError as e:
        print(f"Error reading file: {e}")


search_in_file("your_file.txt", "umesh")
