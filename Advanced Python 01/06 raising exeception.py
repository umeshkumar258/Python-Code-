a = int(input("enter the numeber:"))

b = int(input("eneter the numeber:"))

if(b == 0):
    raise ZeroDivisionError("heyyyy not good")

else:
   print(f"The division a/b is: {a/b}")


# by using raise it will crash the progamming
