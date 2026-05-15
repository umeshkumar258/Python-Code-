# Words to censor
blocked_words = ["donkey", "ganda", "app"]

file_name = "new.txt"

# Read file
with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

# Censor words
for word in blocked_words:
    content = content.replace(word, "#" * len(word))

# Write updated content
with open(file_name, "w", encoding="utf-8") as file:
    file.write(content)

print("Censoring completed.")
