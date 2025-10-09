from functools import reduce

ist = [3,4,5,6,7]

square = lambda n:n*n

sqlist = map(square ,ist)
print(list(sqlist))


# filter function

def evem(n):
    if(n%2 == 0):
        return True
    return False

onlyeven = filter(evem,ist)
print(list(onlyeven))


# Reduce exmple

def sum(a,b):
    return a+b

print(reduce(sum,ist))