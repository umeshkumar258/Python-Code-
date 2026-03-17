# ---------------------------------------
# BASE CLASS 1
# ---------------------------------------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Employee Name : {self.name}")
        print(f"Salary        : {self.salary}")


# ---------------------------------------
# BASE CLASS 2
# ---------------------------------------
class Coder:
    def __init__(self, language):
        self.language = language

    def print_languages(self):
        print(f"Known Language: {self.language}")


# ---------------------------------------
# DERIVED CLASS (MULTIPLE INHERITANCE)
# ---------------------------------------
class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def __init__(self, name, salary, language):
        # Initialize both parent classes
        Employee.__init__(self, name, salary)
        Coder.__init__(self, language)

    def show_company(self):
        print(f"Company       : {self.company}")


# ---------------------------------------
# OBJECT CREATION
# ---------------------------------------
b = Programmer("Umesh", 8999999, "Python")

# ---------------------------------------
# METHOD CALLS
# ---------------------------------------
print("Using Programmer object:\n")
b.show()
b.print_languages()
b.show_company()
