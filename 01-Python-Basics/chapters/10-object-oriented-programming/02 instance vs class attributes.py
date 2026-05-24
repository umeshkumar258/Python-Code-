# ---------------------------------------
# CLASS DEFINITION
# ---------------------------------------
class Employee:
    # Class attributes
    language = "Python"
    salary = 1200000

    def __init__(self, name, language=None):
        self.name = name

        # Use custom language if given
        if language:
            self.language = language


# ---------------------------------------
# OBJECTS
# ---------------------------------------
umesh = Employee("Umesh", "Java")
babu = Employee("Babu")


# ---------------------------------------
# DISPLAY DETAILS
# ---------------------------------------
print("Umesh Details")
print("Name     :", umesh.name)
print("Language :", umesh.language)
print("Salary   :", umesh.salary)

print("\nBabu Details")
print("Name     :", babu.name)
print("Language :", babu.language)
print("Salary   :", babu.salary)


# ---------------------------------------
# CLASS ATTRIBUTES
# ---------------------------------------
print("\nClass Attributes")
print("Language :", Employee.language)
print("Salary   :", Employee.salary)
