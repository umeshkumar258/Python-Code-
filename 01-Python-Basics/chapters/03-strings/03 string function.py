name = "harry"

print("Length:", len(name))                # number of characters
print("Capitalize:", name.capitalize())    # first letter capital
print("Ends with 'ry':", name.endswith("ry"))
print("Starts with 'h':", name.startswith("h"))
print("Count of 'h':", name.count("h"))
print("Index of 'r':", name.find("r"))     # find returns index
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Replace name:", name.replace("harry", "umesh"))

print("Original:", name, "| Type:", type(name))
print("Index of 'h':", name.find("h"))
