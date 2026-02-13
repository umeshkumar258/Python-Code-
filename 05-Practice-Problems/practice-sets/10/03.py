class Demo:
    a = 4   # Class attribute


o = Demo()

print(o.a)     # Accessing class attribute through object

o.a = 0        # Creating instance attribute

print(o.a)     # Now accessing instance attribute
print(Demo.a)  # Accessing class attribute directly from class
