text = "umesh is good boy and he is learning python"

name = input("Enter the name: ").lower()

if name in text.lower():
    print("Yes, it is there")
else:
    print("Not there")
