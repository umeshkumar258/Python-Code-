# f = open("file.txt")
# print(f.read())
# f.close()

# the same thing can be written using with statemte like this:


with open("file.txt") as f:
    print(f.read())

# you dont have to explictly close the file


with open('file.txt', 'r') as file:
    content = file.read(10)  # Reads first 5 characters
    print(content)
