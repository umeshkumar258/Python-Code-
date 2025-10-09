# def lar():
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     c = int(input("Enter a number: "))

#     if(a>b and b>c):
#         print(" a is the largest number")

#     elif(b>c and b>a):
#         print(" b is the largest number")

#     else:
#        print("c is the largest number")
   
# lar()



# def lar():
#     numbers = []

#     for i in range(3):
#         num = int(input(f"Enter number {i+1}: "))
#         numbers.append(num)

#     largest = numbers[0]
#     for num in numbers:
#         if num > largest:
#             largest = num

#     print(f"{largest} is the largest number")

# lar()



# def cel():
#     c = int(input("Enter temp in clesius: "))
#     faher = (c * 9/5) + 32

#     print(f"Temp in faherenhit is {faher}")


# cel()

# print("Hello", end="")
# print(" World")


# d



n = int(input("Enter a number: "))
def pat(n):   
    for i in range(n,n-1):
        print("*" * n)

pat(n)