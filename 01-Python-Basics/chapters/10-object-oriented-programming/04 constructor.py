# ---------------------------------------
# CLASS DEFINITION
# ---------------------------------------
class Employee:
    # Class attributes
    language = "Python"
    salary = 1200000

    # Constructor (dunder method)
    def __init__(self, name, salary, language):
        self.name = name          # instance attribute
        self.salary = salary      # instance attribute
        self.language = language  # instance attribute
        print("I am creating an object")

    # Instance method
    def getInfo(self):
        print(f"Name     : {self.name}")
        print(f"Language : {self.language}")
        print(f"Salary   : {self.salary}")

    # Static method (no self)
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
umesh.getInfo()
umesh.greet()

print("\nUsing class:")
Employee.getInfo(umesh)
Employee.greet()
