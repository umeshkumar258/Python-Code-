# ---------------------------------------
# 1. LIST ITERATION
# ---------------------------------------
numbers = [4, 64, 62, 66, 2, 77]

print("List items:")
for num in numbers:
    print(num)

# Using enumerate() → gives index + value
print("\nList items with index (enumerate):")
for index, value in enumerate(numbers):
    print(f"Index {index} -> Value {value}")


# ---------------------------------------
# 2. TUPLE ITERATION
# ---------------------------------------
my_tuple = (4, 63, 66, 366, 33)

print("\nTuple items:")
for item in my_tuple:
    print(item)


# ---------------------------------------
# 3. SET ITERATION (unordered)
# ---------------------------------------
my_set = {4, 666, 2, 66, 663, 3}

print("\nSet items (order may change):")
for item in my_set:
    print(item)


# ---------------------------------------
# 4. STRING ITERATION
# ---------------------------------------
name = "umesh"

print("\nCharacters in string:")
for char in name:
    print(char, end="")
print()  # newline


# ---------------------------------------
# 5. DICTIONARY ITERATION
# ---------------------------------------
info = {"umesh": 737, "babu": 389}

print("\nDictionary key-value pairs:")
for key, value in info.items():
    print(f"{key} → {value}")

# Loop only keys
print("\nDictionary keys:")
for key in info.keys():
    print(key)

# Loop only values
print("\nDictionary values:")
for value in info.values():
    print(value)


# ---------------------------------------
# 6. RANGE EXAMPLES
# ---------------------------------------
print("\nRange example (1 to 10):")
for i in range(1, 11):
    print(i, end=" ")
print()

print("\nRange with steps:")
for i in range(0, 51, 5):
    print(i, end=" ")
print()


# ---------------------------------------
# 7. BREAK & CONTINUE EXAMPLES
# ---------------------------------------
print("\nBreak example:")
for i in range(1, 10):
    if i == 5:
        break
    print(i)


print("\nContinue example:")
for i in range(1, 10):
    if i == 5:
        continue
    print(i)


# ---------------------------------------
# 8. NESTED LOOPS
# ---------------------------------------
print("\nNested loop example:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()


# ---------------------------------------
# 9. LIST COMPREHENSION (ADVANCED)
# ---------------------------------------
print("\nList comprehension example:")
squares = [x * x for x in range(1, 10)]
print("Squares:", squares)

evens = [x for x in range(1, 20) if x % 2 == 0]
print("Even numbers:", evens)
