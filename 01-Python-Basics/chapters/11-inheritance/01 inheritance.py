# ---------------------------------------
# PARENT CLASS
# ---------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"


# ---------------------------------------
# CHILD CLASS (Inheritance)
# ---------------------------------------
class Dog(Animal):

    def speak(self):
        return "Woof!"


# ---------------------------------------
# OBJECT CREATION
# ---------------------------------------
my_dog = Dog("Buddy")

# ---------------------------------------
# OUTPUT
# ---------------------------------------
print("Name :", my_dog.name)      # Inherited attribute
print("Sound:", my_dog.speak())   # Overridden method
