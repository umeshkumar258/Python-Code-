# ---------------------------------------
# CLASS DEFINITION
# ---------------------------------------
class Employee:
    """Employee class to store basic details"""

    # Class attributes
    default_language = "Python"
    default_salary = 1200000

    def __init__(self, language=None, salary=None):
        """Constructor to initialize instance attributes"""
        self.language = language if language else Employee.default_language
        self.salary = salary if salary else Employee.default_salary

    # Instance method
    def get_info(self):
        """Display employee details"""
        print(f"Language : {self.language}")
        print(f"Salary   : {self.salary}")

    # Static method
    @staticmethod
    def greet():
        """Static greeting method"""
        print("Good morning")


# ---------------------------------------
# OBJECT CREATION
# ---------------------------------------
umesh = Employee(language="Java")

# ---------------------------------------
# METHOD CALLS
# ---------------------------------------
print("Using object:")
umesh.get_info()
umesh.greet()

print("\nUsing class:")
Employee.get_info(umesh)
Employee.greet()
