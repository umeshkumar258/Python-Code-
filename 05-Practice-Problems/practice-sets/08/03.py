# Default print -> moves to next line
print("a")
print("b")

# end="" -> stays on same line
print("c", end="")
print("d")

# end=" " -> adds space instead of new line
print("e", end=" ")
print("f")

# sep -> separates multiple values
print("g", "h", "i", sep="-")

# Using both sep and end together
print("j", "k", sep="*", end=" ")
print("l")

print("\nThanks")
