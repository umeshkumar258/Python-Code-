a = "umesh"

print(a[-4:])   # same as a[1:] → "mesh"
print(a[1:])    # "mesh"

print(a[-5:])   # full string → "umesh"

print(a[-1:])   # last character → "h"

print(a[0:6:2])  # skip slicing → characters at indices 0,2,4 → "ues"

print(a[0:7:6])  # starts at 0, then jumps 6 steps → prints "u"

print(a[-2:])   # last 2 characters → "sh"

print(a[-2:-1]) # from -2 to -1 (excluding -1) → "s"
print(a[1:2])   # from index 1 to 2 (excluding 2) → "m"
