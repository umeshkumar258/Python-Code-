# Creating a dictionary
marks = {"umesh": "73", "babu": "87", "harry": "88"}

# Display dictionary items, keys and values
print("Items:", marks.items())    # (key, value) pairs
print("Keys:", marks.keys())      # All keys
print("Values:", marks.values())  # All values

# Length of dictionary
print("Number of students:", len(marks))

# Access value using get()
print("Umesh's marks (before update):", marks.get("umesh"))

# Updating values / adding new key-value pairs
marks.update({"umesh": 89})   # updates existing key
marks.update({"vinay": 99})   # adds new key

# Removing a key-value pair
marks.pop("umesh")            # removes umesh

print("Updated dictionary:", marks)

# Safe access using get()
print("Unknown key:", marks.get("umesh4"))  # prints None

# Unsafe access (commented because it causes error)
# print(marks["umesh4"])
