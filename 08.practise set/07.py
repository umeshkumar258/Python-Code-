def rem(list,word):
    for item in list:
        list.remove(word)
        return 1


list = ["umesh","harry","babu","vijay"]

print(rem(list,"harry"))