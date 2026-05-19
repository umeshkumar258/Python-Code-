# Parent Class
class Employee:

    def __init__(self):
        self.a = 1

    def show(self):
        print("a =", self.a)


# Child Class
class Programmer(Employee):

    def __init__(self):
        super().__init__()
        self.b = 2

    def show(self):
        super().show()
        print("b =", self.b)


# Grandchild Class
class Manager(Programmer):

    def __init__(self):
        super().__init__()
        self.c = 3

    def show(self):
        super().show()
        print("c =", self.c)


# Object
m = Manager()

# Output
m.show()
