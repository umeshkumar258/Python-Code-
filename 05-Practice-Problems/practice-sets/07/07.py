# --------------------------------
# STAR PYRAMID PATTERN
# --------------------------------

n = int(input("Enter the number: "))

for i in range(1, n + 1):
    # print spaces
    print(" " * (n - i), end="")

    # print stars
    print("*" * (2 * i - 1))
