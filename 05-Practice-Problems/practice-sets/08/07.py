def remove_word(names, word):
    if word in names:
        names.remove(word)
    return names


names = ["umesh", "harry", "babu", "vijay"]

print(remove_word(names, "harry"))
