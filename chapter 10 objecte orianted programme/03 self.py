class Employee:
    language =  "python"
    salary = 1200000


    def getInfo(self):
        print(f"the language is {self.language},the slary {self.salary}")
    
    @staticmethod
    def greet(self):
        print("good morning")

umesh = Employee()
umesh.language = "java"


# umesh.getInfo()
Employee.getInfo(umesh)
Employee.greet(umesh)
