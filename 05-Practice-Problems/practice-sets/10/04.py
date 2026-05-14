class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print("Square:", self.number ** 2)

    def cube(self):
        print("Cube:", self.number ** 3)

    def square_root(self):
        print("Square Root:", self.number ** 0.5)

    @staticmethod
    def hello():
        print("Hello Umesh")


# Object
calc = Calculator(4)

# Method calls
calc.square()
calc.cube()
calc.square_root()

# Static method call
calc.hello()
