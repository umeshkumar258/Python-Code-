with open("poem.txt", "r") as file:
    content = file.read()  # Read the content of the file

print(content)  # Print the content of the file

if "umesh" in content:  # Check if "umesh" is in the content of the file
    print("Hey umesh is there")
else:
    print("Hey umesh is not there")
