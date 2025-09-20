try:
    a = int(input("Enter the number:"))

    b = int(input("Enter the number:"))

    print(f"the divison is {a/b}")

except ZeroDivisionError as e:
    print("infinte")
    

print("Thanks")