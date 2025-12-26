from functools import reduce

numbers = [2, 3, 66, 4, 34, 55, 99, 65]

def greater(x, y):
    """Return the greater of two numbers"""
    return x if x > y else y

maximum = reduce(greater, numbers)

print("Maximum value:", maximum)
