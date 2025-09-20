from functools import reduce

a = [2,3,66,4,34,55,99,65]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,a))

# I Love this one