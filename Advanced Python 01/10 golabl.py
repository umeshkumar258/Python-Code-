a = 77

def fun():
    global a
    a = 3

    print(a)

fun()
print(a)