# ---------------------------------------
# CLASS DEFINITION
# ---------------------------------------
class Employee:
    # Class attributes (shared by all objects)
    language = "Python"
    salary = 1200000

    def __init__(self, name):
        # Object (instance) attribute
        self.name = name

    def display(self):
        print(f"Name     : {self.name}")
        print(f"Language : {self.language}")
        print(f"Salary   : {self.salary}")
        print("-" * 30)


# ---------------------------------------
# OBJECT CREATION
# ---------------------------------------
umesh = Employee("Umesh")
babu = Employee("Babu")

# ---------------------------------------
# DISPLAY DETAILS
# ---------------------------------------
umesh.display()
babu.display()

# ---------------------------------------
# MODIFY OBJECT ATTRIBUTE
# ---------------------------------------
umesh.salary = 1500000   # Only for Umesh

print("After modifying Umesh salary:\n")
umesh.display()
babu.display()
