# ---------------------------------------
# CLASS DEFINITION
# ---------------------------------------
class Employee:
    """Employee class to store employee details"""

    # Class attributes (defaults)
    default_language = "Python"
    default_salary = 1200000

    # Constructor
    def __init__(self, name, salary=None, language=None):
        self.name = name
        self.salary = salary if salary is not None else Employee.default_salary
        self.language = language if language is not None else Employee.default_language

    # Instance method
    def get_info(self):
        print(f"Name     : {self.name}")
        print(f"Language : {self.language}")
        print(f"Salary   : {self.salary}")

    # Static method
    @staticmethod
    def greet():
        print("Good morning")


# ---------------------------------------
# OBJECT CREATION
# ---------------------------------------
umesh = Employee("Umesh", 130000, "JavaScript")

# ---------------------------------------
# METHOD CALLS
# ---------------------------------------
print("\nUsing object:")
umesh.get_info()
Employee.greet()   # better practice

print("\nUsing class:")
Employee.get_info(umesh)
Employee.greet()
