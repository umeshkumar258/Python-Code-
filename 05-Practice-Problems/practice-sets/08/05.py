# def pattern(n):
#     if(n==0):
#         return 1
#     print("*"*n)
#     pattern(n-1)

# pattern(4)


# n = int(input("Enter the number:"))

# for i in range(1,n+1):
#     print(""*(n),end="")
#     print("*"*(n-i+1),end="")
#     print("")


# n = int(input("Enter the number:"))

# for i in range(1,n+1):
#     print(""*(n),end="")
#     print("*"*(i),end="")
#     print("")


rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    print('*' * i)
