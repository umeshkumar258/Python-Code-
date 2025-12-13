# ---------------------------------------
# Function Definition
# ---------------------------------------
def avg():
    """Takes 3 numbers from the user and returns their average"""
    numbers = [int(input("Enter a number: ")) for _ in range(3)]
    return sum(numbers) / len(numbers)


# ---------------------------------------
# Function Call (Multiple Times)
# ---------------------------------------
for i in range(3):
    result = avg()
    print(f"Average {i + 1}: {result}")

print("\nEnd of the program")


# ---------------------------------------
# Built-in sum() example
# ---------------------------------------
# sum() is a built-in function that returns
# the sum of elements in a list or tuple

a = 39
b = 390
c = 300

avgn = (a + b + c) / 3
print("\nAverage using variables:", avgn)

