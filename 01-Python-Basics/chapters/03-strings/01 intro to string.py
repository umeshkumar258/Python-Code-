# All of these represent strings
a = "umesh"
b = 'umesh'
c = '''umesh'''

# String slicing
name_short = a[:3]   # Same as a[0:3]
print("Short name:", name_short)

full_name = a[:]     # Same as a[0:]
print("Full name:", full_name)

new = b[:]           # Prints full string
print("Copied string:", new, "| Type:", type(new))

# Strings are immutable in Python (cannot be changed in place)
hot = a[:]
print("Hot:", hot, "| Type:", type(hot))

# String concatenation
best = a + b
print("Concatenated name:", best)
