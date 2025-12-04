# 



# def calculate_remaining_amount(total, pg, food, travel):
#     return total - (pg + food + travel)

# total = int(input("Enter the total amount of money"))
# pg = int(input("Enter the amount of money"))
# food = int(input("Enter the amount of money"))
# travel = int(input("Enter the amount of money"))

# amount = calculate_remaining_amount(total, pg, food, travel)
# print(amount)



# list = []

# for i in range(3):
#     num = int(input("Enter a number"))
#     list.append(num)

# for i in range(len(list)):
#     if list[i] > list[i-1]:
#         list[i-1], list[i] = list[i], list[i-1]
#         print(list[i-1],list[i])


# l


# list = []

# for i in range(3):
#     num = int(input("Enter a number"))
#     list.append(num)

# for i in range(len(list)):
#     if list[i] > list[i-1]:
#         list[i-1], list[i] = list[i], list[i-1]
#         print(list[i-1], list[i])

j# we can not use keywords as varibale names

# rules for naming varialles in python

#1. Variable names must start with a letter or an underscore (_).
#2. Variable names cannot start with a number.
#3. Variable names can only contain alphanumeric characters and underscores (A-Z, a-z, 0-9, and _).
#4. Variable names are case-sensitive (e.g., myVar and myvar are different variables).
#5. Variable names cannot be Python keywords or reserved words.


# Input dimensions for the matrices
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))

# Ensure matrix multiplication is possible
if cols1 != rows2:
    print("Matrix multiplication is not possible with these dimensions.")
else:
    # Input the first matrix
    print("Enter the elements of the first matrix:")
    matrix1 = []
    for i in range(rows1):
        row = list(map(int, input().split()))
        matrix1.append(row)

    # Input the second matrix
    print("Enter the elements of the second matrix:")
    matrix2 = []
    for i in range(rows2):
        row = list(map(int, input().split()))
        matrix2.append(row)

    # Initialize the product matrix with zeros
    product = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                product[i][j] += matrix1[i][k] * matrix2[k][j]

    # Print the resulting product matrix
    print("The product of the matrices is:")
    for row in product:
        print(" ".join(map(str, row)))