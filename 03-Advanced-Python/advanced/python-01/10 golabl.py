a = 77   # Global variable

def fun():
    global a   # Refers to the global variable 'a'
    a = 3      # Modifies the global variable
    print(a)   # Prints updated value of 'a'

fun()          # Function call
print(a)       # Prints global 'a'
