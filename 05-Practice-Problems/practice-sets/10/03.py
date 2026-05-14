class Demo:
    a = 4   # Class attribute


# Create object
obj = Demo()

# Access class attribute
print("Before changing:")
print("Object value:", obj.a)
print("Class value :", Demo.a)

# Create instance attribute
obj.a = 0

print("\nAfter changing object value:")
print("Object value:", obj.a)
print("Class value :", Demo.a)
