def divisible5(n):
    if(n%3 == 0):
        return True
    return False

a = [1,2,333,45,77,7,6665,6663,55,65,75]


f = list(filter(divisible5,a))
print(f)

