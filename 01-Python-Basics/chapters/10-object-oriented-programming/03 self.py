# ---------------------------------------
# CLASS DEFINITION
# ---------------------------------------
class Employee:
    # Class attributes
    language = "Python"
    salary = 1200000

    # Instance method
    def getInfo(self):
        print(f"Language : {self.language}")
        print(f"Salary   : {self.salary}")

    # Static method (no self)
    @staticmethod
    def greet():
        print("Good morning")


# ---------------------------------------
# OBJECT CREATION
# ---------------------------------------
umesh = Employee()

# Instance attribute (overrides class attribute for this object)
umesh.language = "Java"

# ---------------------------------------
# METHOD CALLS
# ---------------------------------------
print("Using object:")
umesh.getInfo()
umesh.greet()

print("\nUsing class:")
Employee.getInfo(umesh)
Employee.greet()
