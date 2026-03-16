# ---------------------------------------
# CLASS DEFINITION
# ---------------------------------------
class Employee:
    # Class attributes (shared by all objects)
    language = "Python"
    default_salary = 1200000

    def __init__(self, name, salary=None):
        # Instance attributes
        self.name = name
        self.salary = salary if salary is not None else Employee.default_salary

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
print("Before modifying salary:\n")
umesh.display()
babu.display()

# ---------------------------------------
# MODIFY OBJECT ATTRIBUTE
# ---------------------------------------
umesh.salary = 1500000   # Only changes Umesh's salary

print("After modifying Umesh salary:\n")
umesh.display()
babu.display()
