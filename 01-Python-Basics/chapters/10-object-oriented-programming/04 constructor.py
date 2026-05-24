class Employee:

    # Class attributes
    default_language = "Python"
    default_salary = 1200000

    # Constructor
    def __init__(self, name, salary=default_salary, language=default_language):
        self.name = name
        self.salary = salary
        self.language = language

    # Instance method
    def get_info(self):
        print(f"Name     : {self.name}")
        print(f"Language : {self.language}")
        print(f"Salary   : {self.salary}")

    # Static method
    @staticmethod
    def greet():
        print("Good Morning")


# Object creation
umesh = Employee("Umesh", 130000, "JavaScript")


# Method calls
print("Using Object:")
umesh.get_info()

print("\nStatic Method:")
Employee.greet()
