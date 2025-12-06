# OPERATORS IN PYTHON

# 1. Arithmetic Operators: +, -, *, /, %, **, //

e = 3
e += 8      # e = 3 + 8 = 11
e *= 6      # e = 11 * 6 = 66
e /= 29     # e = 66 / 29 (result is float)

print("Value of e =", e)


# 2. Comparison Operators: ==, >, >=, <, != etc.

a = (1 == 1)
print("Is 1 equal to 1? ->", a)

b = 38
c = 33
print("Is b >= c? ->", b >= c)

# Comparison operators always return boolean values


# 3. Logical Operators: and, or, not

g = True or False
print("True or False =", g)

print("True or False =", True or False)
print("True or True =", True or True)

r = True and False
print("True and False =", r)

y = not False
print("not False =", y)

z = True and False
print("True and False again =", z)
