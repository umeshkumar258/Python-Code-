class Employee:
    language =  "python"
    salary = 1200000

    def __init__(self,name,salary,language):   # dunder mehtod which is called imedatly
        self.salary= salary
        self.language=language
        print("I am creating an object")

    
    def getInfo(self):
        print(f"the language is {self.language},the slary {self.salary}")
    
    @staticmethod
    def greet(self):
        print("good morning")

umesh = Employee("harry",130000,"javascript")
# umesh.language = "java"


# umesh.getInfo()
Employee.getInfo(umesh)