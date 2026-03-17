# ---------------------------------------
# PARENT CLASS
# ---------------------------------------
class Animal:
    """Base class for all animals"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

    def info(self):
        return f"I am an animal named {self.name}"


# ---------------------------------------
# CHILD CLASS (Inheritance)
# ---------------------------------------
class Dog(Animal):
    """Dog class inheriting from Animal"""

    def __init__(self, name, breed=None):
        super().__init__(name)   # call parent constructor
        self.breed = breed

    def speak(self):
        return "Woof!"

    def info(self):
        base_info = super().info()
        return f"{base_info} and I am a Dog"


# ---------------------------------------
# OBJECT CREATION
# ---------------------------------------
my_dog = Dog("Buddy", "Labrador")

# ---------------------------------------
# OUTPUT
# ---------------------------------------
print("Name :", my_dog.name)
print("Sound:", my_dog.speak())
print("Info :", my_dog.info())
