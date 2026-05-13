from pathlib import Path


def replace_in_file(filepath, old_word, new_word):
    """Replace words in a file."""

    path = Path(filepath)

    if not path.exists():
        print(f"❌ File '{filepath}' not found.")
        return

    try:
        content = path.read_text(encoding="utf-8")

        count = content.count(old_word)

        if count == 0:
            print(f"'{old_word}' not found.")
            return

        updated_content = content.replace(old_word, new_word)

        path.write_text(updated_content, encoding="utf-8")

        print(f"✅ Replaced {count} occurrence(s).")

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    replace_in_file("new.txt", "donkey", "umesh")
