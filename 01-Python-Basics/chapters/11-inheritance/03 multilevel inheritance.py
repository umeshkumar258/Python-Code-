# ---------------------------------------
# BASE CLASS
# ---------------------------------------
class Employee:
    def __init__(self):
        self.a = 1

    def show(self):
        print(f"a = {self.a}")


# ---------------------------------------
# CHILD CLASS (inherits Employee)
# ---------------------------------------
class Programmer(Employee):
    def __init__(self):
        super().__init__()   # Call parent constructor
        self.b = 2

    def show(self):
        super().show()
        print(f"b = {self.b}")


# ---------------------------------------
# GRANDCHILD CLASS (inherits Programmer)
# ---------------------------------------
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        self.c = 3

    def show(self):
        super().show()
        print(f"c = {self.c}")


# ---------------------------------------
# OBJECT OF Employee
# ---------------------------------------
print("Employee object:")
o1 = Employee()
o1.show()
print()


# ---------------------------------------
# OBJECT OF Programmer
# ---------------------------------------
print("Programmer object:")
o2 = Programmer()
o2.show()
print()


# ---------------------------------------
# OBJECT OF Manager
# ---------------------------------------
print("Manager object:")
o3 = Manager()
o3.show()
