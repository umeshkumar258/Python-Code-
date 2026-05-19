# Parent Class
class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"


# Child Class
class Dog(Animal):

    def speak(self):
        return "Woof!"


# Object Creation
dog1 = Dog("Buddy")

# Output
print("Name :", dog1.name)
print("Sound:", dog1.speak())
