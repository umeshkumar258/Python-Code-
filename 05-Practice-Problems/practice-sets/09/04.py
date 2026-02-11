import os

def replace_in_file(filepath: str, old_word: str, new_word: str) -> None:
    """Replace all occurrences of a word in a file with a new word."""
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    count = content.count(old_word)

    if count == 0:
        print(f"'{old_word}' was not found in '{filepath}'. No changes made.")
        return

    updated_content = content.replace(old_word, new_word)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"✅ Replaced {count} occurrence(s) of '{old_word}' with '{new_word}' in '{filepath}'.")


if __name__ == "__main__":
    replace_in_file("new.txt", "donkey", "umesh")
