# String methods example

name = "harry"

print(f"Length: {len(name)}")                       # Number of characters
print(f"Capitalize: {name.capitalize()}")           # First letter capital
print(f"Ends with 'ry': {name.endswith('ry')}")
print(f"Starts with 'h': {name.startswith('h')}")
print(f"Count of 'r': {name.count('r')}")           # Count occurrences
print(f"First index of 'r': {name.find('r')}")      # Returns index or -1
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")
print(f"Replace name: {name.replace('harry', 'umesh')}")

print(f"Original string: {name} | Type: {type(name)}")
print(f"Index of 'h': {name.find('h')}")
