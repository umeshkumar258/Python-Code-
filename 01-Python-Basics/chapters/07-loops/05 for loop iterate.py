# ---------------------------------------
# FUNCTION TO PRINT SECTION TITLE
# ---------------------------------------
def section(title):
    print(f"\n{'-'*10} {title} {'-'*10}")


# ---------------------------------------
# 1. LIST ITERATION
# ---------------------------------------
numbers = [4, 64, 62, 66, 2, 77]

section("List Iteration")

print("List items:")
for num in numbers:
    print(num)

print("\nList items with index:")
for index, value in enumerate(numbers):
    print(f"Index {index} -> Value {value}")


# ---------------------------------------
# 2. TUPLE ITERATION
# ---------------------------------------
my_tuple = (4, 63, 66, 366, 33)

section("Tuple Iteration")

for item in my_tuple:
    print(item)


# ---------------------------------------
# 3. SET ITERATION
# ---------------------------------------
my_set = {4, 666, 2, 66, 663, 3}

section("Set Iteration (unordered)")

for item in my_set:
    print(item)


# ---------------------------------------
# 4. STRING ITERATION
# ---------------------------------------
name = "umesh"

section("String Iteration")

print("Characters:", " ".join(name))


# ---------------------------------------
# 5. DICTIONARY ITERATION
# ---------------------------------------
info = {"umesh": 737, "babu": 389}

section("Dictionary Iteration")

print("Key → Value:")
for key, value in info.items():
    print(f"{key} → {value}")

print("\nKeys:", list(info.keys()))
print("Values:", list(info.values()))


# ---------------------------------------
# 6. RANGE EXAMPLES
# ---------------------------------------
section("Range Examples")

print("1 to 10:", list(range(1, 11)))
print("Step of 5:", list(range(0, 51, 5)))


# ---------------------------------------
# 7. BREAK & CONTINUE
# ---------------------------------------
section("Break Example")

for i in range(1, 10):
    if i == 5:
        break
    print(i)

section("Continue Example")

for i in range(1, 10):
    if i == 5:
        continue
    print(i)


# ---------------------------------------
# 8. NESTED LOOPS
# ---------------------------------------
section("Nested Loop")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()


# ---------------------------------------
# 9. LIST COMPREHENSION
# ---------------------------------------
section("List Comprehension")

squares = [x**2 for x in range(1, 10)]
evens = [x for x in range(1, 20) if x % 2 == 0]

print("Squares:", squares)
print("Even numbers:", evens)
