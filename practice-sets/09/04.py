word = "donkey"

with open("new.txt","r") as f:
    content = f.read()

contentnew = content.replace(word,"umesh")

with open("new.txt","w") as f:
    f.write(contentnew)

