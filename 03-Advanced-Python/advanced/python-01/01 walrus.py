# Python Walrus Operator (:=) - All in One Example
# Requires Python 3.8+

# -------------------------------
# 1. Length checking
# -------------------------------
numbers = [1, 2, 3, 4, 5]

if (n := len(numbers)) > 3:
    print(f"List is too long ({n} elements), expected ≤ 3")


# -------------------------------
# 2. Input validation
# -------------------------------
if (name := input("\nEnter your name: ").strip()):
    print(f"Hello, {name}")
else:
    print("Name cannot be empty")


# -------------------------------
# 3. While loop usage
# -------------------------------
print("\nEnter numbers (0 to stop):")
while (num := int(input("Enter number: "))) != 0:
    print(f"You entered: {num}")


# -------------------------------
# 4. File-like example (simulation)
# -------------------------------
data = "Hello Python"

if (content := data):
    print("\nData found:", content)


# -------------------------------
# 5. Maximum using walrus + reduce
# -------------------------------
from functools import reduce

values = [10, 45, 23, 99, 67]

maximum = reduce(lambda x, y: x if x > y else y, values)

print("\nMaximum value:", maximum)


# -------------------------------
# 6. Without walrus (comparison)
# -------------------------------
length = len(values)
if length > 3:
    print(f"Values list has {length} elements")
