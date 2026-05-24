# ---------------------------------------
# CLASS DEFINITION
# ---------------------------------------
class Employee:
    # Class attributes
    language = "Python"
    default_salary = 1200000

    # We can pass the default salary directly into the argument
    def __init__(self, name, salary=default_salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name     : {self.name}\n"
              f"Language : {self.language}\n"
              f"Salary   : {self.salary}\n"
              f"{'-' * 30}")


# ---------------------------------------
# OBJECT CREATION & MODIFICATION
# ---------------------------------------
umesh = Employee("Umesh")
babu = Employee("Babu")

print("Before modifying salary:\n")
umesh.display()
babu.display()

# Modifying only Umesh's salary
umesh.salary = 1500000   

print("After modifying Umesh salary:\n")
umesh.display()
babu.display()
