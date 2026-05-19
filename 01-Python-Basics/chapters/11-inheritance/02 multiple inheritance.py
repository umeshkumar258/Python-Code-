# Parent Class 1
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Name   :", self.name)
        print("Salary :", self.salary)


# Parent Class 2
class Coder:

    def __init__(self, language):
        self.language = language

    def show_language(self):
        print("Language :", self.language)


# Child Class
class Programmer(Employee, Coder):

    def __init__(self, name, salary, language):

        Employee.__init__(self, name, salary)
        Coder.__init__(self, language)

    def company(self):
        print("Company : ITC Infotech")


# Object
p1 = Programmer("Umesh", 90000, "Python")

# Output
p1.show()
p1.show_language()
p1.company()
