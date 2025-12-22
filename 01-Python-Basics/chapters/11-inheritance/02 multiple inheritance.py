# ---------------------------------------
# BASE CLASS 1
# ---------------------------------------
class Employee:
    company = "IYC"
    name = "Umesh"
    salary = 8999999

    def show(self):
        print(f"Employee Name : {self.name}")
        print(f"Salary        : {self.salary}")


# ---------------------------------------
# BASE CLASS 2
# ---------------------------------------
class Coder:
    language = "Python"

    def print_languages(self):
        print(f"Known Language: {self.language}")


# ---------------------------------------
# DERIVED CLASS (MULTIPLE INHERITANCE)
# ---------------------------------------
class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def show_company(self):
        print(f"Company       : {self.company}")


# ---------------------------------------
# OBJECT CREATION
# ---------------------------------------
a = Employee()
b = Programmer()

# ---------------------------------------
# METHOD CALLS
# ---------------------------------------
print("Using Programmer object:\n")
b.show()              # From Employee
b.print_languages()   # From Coder
b.show_company()      # From Programmer
