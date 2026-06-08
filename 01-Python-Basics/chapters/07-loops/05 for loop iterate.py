# Function to print section title
def section(title):
    print("\n" + "-" * 10, title, "-" * 10)


# 1. List Iteration
section("List Iteration")

numbers = [4, 64, 62, 66, 2, 77]

for num in numbers:
    print(num)

print("\nWith Index:")
for i, num in enumerate(numbers):
    print(i, "->", num)


# 2. Tuple Iteration
section("Tuple Iteration")

my_tuple = (4, 63, 66, 366, 33)

for item in my_tuple:
    print(item)


# 3. Set Iteration
section("Set Iteration")

my_set = {4, 666, 2, 66, 663, 3}

for item in my_set:
    print(item)


# 4. String Iteration
section("String Iteration")

name = "umesh"

for ch in name:
    print(ch)


# 5. Dictionary Iteration
section("Dictionary Iteration")

info = {"umesh": 737, "babu": 389}

for key, value in info.items():
    print(key, ":", value)


# 6. Range Examples
section("Range Examples")

print(list(range(1, 11)))
print(list(range(0, 51, 5)))


# 7. Break Example
section("Break")

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# 8. Continue Example
section("Continue")

for i in range(1, 10):
    if i == 5:
        continue
    print(i)


# 9. Nested Loop
section("Nested Loop")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()


# 10. List Comprehension
section("List Comprehension")

squares = [x * x for x in range(1, 10)]
evens = [x for x in range(1, 21) if x % 2 == 0]

print("Squares:", squares)
print("Evens:", evens)
