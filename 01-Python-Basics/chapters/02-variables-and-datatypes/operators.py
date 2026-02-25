"""
OPERATORS IN PYTHON
"""

# -------------------------------
# 1️⃣ Arithmetic & Assignment Operators
# -------------------------------

num = 3
num += 8      # num = num + 8
num *= 6      # num = num * 6
num /= 29     # division always returns float

print(f"Final value of num: {num}")
print(f"Type of num: {type(num)}\n")


# -------------------------------
# 2️⃣ Comparison Operators
# -------------------------------

is_equal = (1 == 1)
print(f"Is 1 equal to 1? -> {is_equal}")

b = 38
c = 33
print(f"Is {b} greater than or equal to {c}? -> {b >= c}")

print("Comparison operators always return Boolean values.\n")


# -------------------------------
# 3️⃣ Logical Operators
# -------------------------------

print(f"True OR False  -> {True or False}")
print(f"True AND False -> {True and False}")
print(f"NOT False      -> {not False}")
