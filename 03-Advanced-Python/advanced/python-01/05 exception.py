try:
    a = int(input("Hey,enter a number:"))
    print(a)

except ValueError as v:
    print("heyyyy")
    print(v)
except Exception as e:
    print(e)

print("Thanks")


# by using this it will not crash the progamme 