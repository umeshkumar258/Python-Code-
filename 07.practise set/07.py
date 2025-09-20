 # it is very important


"""  *
    ***
   *****
"""


# n = int(input("enter the number:"))

# for i in range(1, n+1):
#     print(" "*(n-i),end ="")
#     print("*"*(2*i-1),end="")
#     print("")


# n = int(input("enter the number:"))

# for i in range (1,n+1):
#     print("")
#     print("*"*(2*i-1),end="")
#     print(" "* (n-i),end="")


n = int(input("Enter the number:"))


for i in range(1,n+1):
    print(""*(n-i),end="")
    print("*"*(i),end="")
    print("")