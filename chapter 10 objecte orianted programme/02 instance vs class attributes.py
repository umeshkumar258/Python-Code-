class Employee:
    language = "py"    # this is a class attribute
    salary = 1200000


umesh = Employee()
umesh.language = "java"        # This is an instance attribute
print( umesh.language,umesh.salary)


babu = Employee()
babu.name = "babu"
print(babu.name,babu.salary,babu.language)


# here name is object attribute and salary and language are class
# attributes as theyy directly belong to the class