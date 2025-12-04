class Demo:
    a = 4


o = Demo()
print(o.a)  # prints the class attribute becausse instance attriute 
#                         is not present

o.a = 0       # Instance attribute is set

print(o.a)   # prints the instance attributes because instance attribute is present
print(Demo.a)  # prints the class attribute