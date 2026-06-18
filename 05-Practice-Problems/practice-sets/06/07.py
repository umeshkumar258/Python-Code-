text = "umesh is good boy and he is learning python"

name = input("Enter a word: ").lower()

if name in text.lower():
    print("Found")
else:
    print("Not Found")
