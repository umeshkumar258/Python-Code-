# ---------------------------------------
# BASE CLASS
# ---------------------------------------
class Employee:
    a = 1


# ---------------------------------------
# CHILD CLASS (inherits Employee)
# ---------------------------------------
class Programmer(Employee):
    b = 2


# ---------------------------------------
# GRANDCHILD CLASS (inherits Programmer)
# ---------------------------------------
class Manager(Programmer):
    c = 3


# ---------------------------------------
# OBJECT OF Employee
# ---------------------------------------
o1 = Employee()
print("Employee object:")
print("a =", o1.a)
# print(o1.b)  # ❌ Error: Employee has no attribute 'b'
print()


# ---------------------------------------
# OBJECT OF Programmer
# ---------------------------------------
o2 = Programmer()
print("Programmer object:")
print("a =", o2.a)   # inherited from Employee
print("b =", o2.b)   # from Programmer
print()


# ---------------------------------------
# OBJECT OF Manager
# ---------------------------------------
o3 = Manager()
print("Manager object:")
print("a =", o3.a)   # inherited from Employee
print("b =", o3.b)   # inherited from Programmer
print("c =", o3.c)   # from Manager
