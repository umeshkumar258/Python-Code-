# ---------------------------------------
# CLASS DEFINITION
# ---------------------------------------
class Employee:
    # Class attributes (shared by all objects)
    language = "Python"
    salary = 1200000

    def __init__(self, name=None, language=None):
        # Instance attributes
        self.name = name
        if language is not None:
            self.language = language   # overrides class attribute for this object


# ---------------------------------------
# OBJECT 1
# ---------------------------------------
umesh = Employee(language="Java")

print("Umesh Details:")
print("Language:", umesh.language)   # Java (instance attribute)
print("Salary  :", umesh.salary)     # 1200000 (class attribute)
print()


# ---------------------------------------
# OBJECT 2
# ---------------------------------------
babu = Employee(name="Babu")

print("Babu Details:")
print("Name    :", babu.name)        # instance attribute
print("Language:", babu.language)    # Python (class attribute)
print("Salary  :", babu.salary)      # class attribute
print()


# ---------------------------------------
# CLASS ATTRIBUTE ACCESS
# ---------------------------------------
print("Class Attribute Access:")
print("Employee.language:", Employee.language)
print("Employee.salary  :", Employee.salary)
