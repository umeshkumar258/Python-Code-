# ---------------------------------------
# ALL IN ONE STAR PATTERNS
# ---------------------------------------

n = int(input("Enter the number: "))

print("\n1) Right Triangle")
for i in range(1, n + 1):
    print("*" * i)


print("\n2) Inverted Right Triangle")
for i in range(1, n + 1):
    print("*" * (n - i + 1))


print("\n3) Left Aligned Triangle")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)


print("\n4) Center Pyramid")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


print("\n5) Inverted Pyramid")
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


print("\n6) Hollow Square")
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")


print("\n7) Square Pattern")
for i in range(n):
    print("*" * n)
