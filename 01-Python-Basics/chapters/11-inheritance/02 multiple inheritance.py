class Employee:
    company = "IYc"
    name = "umesh"
    salary = 8999999
    def show(self):
        print(f"The name of the Emplyee is {self.name} and the salary is {self.salary}")

class coder:
    language = "python"
    def printlanguges (self):
        print(f"out of all the language here is your language :{self.language}")


class programmer(Employee,coder):
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The company is {self.company}")

a = Employee()
b = programmer()

b.show()
b.printlanguges()
b.showlanguage()