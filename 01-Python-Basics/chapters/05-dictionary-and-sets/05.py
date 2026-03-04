# Creating an empty set
s = set()

# Adding elements
s.add(20)      # Integer added
s.add(20.0)    # Duplicate value (20 == 20.0) → ignored
s.add('20')    # String is different → added

# Display result
print("Set elements:", s)
print("Length of set:", len(s))
