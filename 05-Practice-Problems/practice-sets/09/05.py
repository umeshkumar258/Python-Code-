# List of words to be censored
blocked_words = ["donkey", "ganda", "app"]

file_name = "new.txt"

# Read the file content
with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

# Replace each blocked word with stars
for word in blocked_words:
    censored = "#" * len(word)
    content = content.replace(word, censored)

# Write the updated content back to the file
with open(file_name, "w", encoding="utf-8") as file:
    file.write(content)

print("Censoring completed successfully.")
