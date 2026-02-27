# String slicing examples (clean & corrected)

name = "umesh"

# Basic slicing
print(name[-4:])     # "mesh"
print(name[1:])      # "mesh"
print(name[-5:])     # "umesh"
print(name[-1:])     # "h"

# Step slicing
print(name[0:6:2])   # "ueh"  (indices 0,2,4)
print(name[0:7:6])   # "u"

# Negative slicing
print(name[-2:])     # "sh"
print(name[-2:-1])   # "s"
print(name[1:2])     # "m"

# Bonus: Reverse string
print(name[::-1])    # "hsemu"
