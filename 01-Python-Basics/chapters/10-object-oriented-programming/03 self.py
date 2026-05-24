# ---------------------------------------
# CLASS DEFINITION
# ---------------------------------------
class Employee:
    # Class attributes
    default_language = "Python"
    default_salary = 1200000

    def __init__(self, language="Python", salary=1200000):
        self.language = language
        self.salary = salary

    # Instance method
    def get_info(self):
        print(f"Language : {self.language}")
        print(f"Salary   : {self.salary}")

    # Static method
    @staticmethod
    def greet():
        print("Good Morning")


# ---------------------------------------
# OBJECT CREATION
# ---------------------------------------
umesh = Employee("Java")


# ---------------------------------------
# METHOD CALLS
# ---------------------------------------
print("Using Object:")
umesh.get_info()
umesh.greet()

print("\nUsing Class:")
Employee.get_info(umesh)
Employee.greet()
