# i tried this one


# n = int(input("ENter the numebr:"))

# for i in range(1,n+1):
#     print(""*(n-1),end="")          # this contain to make the space 
#     print("*"*(n-i+1),end="")
#     print("")


# n = int(input("ENter the numebr:"))

# for i in range(1,n+1):
#     print(""*(n+1),end="")    
#     print("*"*(i),end="")
#     print("")



# n = int(input("ENter the numebr:"))

# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-2),end="")
#     print("")                      # this line is mantory 


n = int(input("ENter the numebr:"))

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n ,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end = "")
        print("*",end = "")
    print("")
 





