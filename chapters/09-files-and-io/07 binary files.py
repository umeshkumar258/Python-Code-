with open ("appu.jpg","rb") as file:
    print(file.read())



try:
    with open('nfile.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
