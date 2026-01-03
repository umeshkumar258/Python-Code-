# Original list
my_list = [8, 4, 3, 7, 9]

# 1️⃣ Using normal for loop
squared_list_loop = []
for num in my_list:
    squared_list_loop.append(num ** 2)

# 2️⃣ Using list comprehension (Pythonic way)
squared_list_comprehension = [num ** 2 for num in my_list]

# 3️⃣ Using map() and lambda
squared_list_map = list(map(lambda x: x ** 2, my_list))

# Output
print("Original list              :", my_list)
print("Squared list (for loop)    :", squared_list_loop)
print("Squared list (comprehension):", squared_list_comprehension)
print("Squared list (map method)  :", squared_list_map)
