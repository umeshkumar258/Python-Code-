class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number * self.number

    def cube(self):
        return self.number * self.number * self.number

    def square_root(self):
        return self.number ** 0.5

    def show(self):
        print("Number:", self.number)
        print("Square:", self.square())
        print("Cube:", self.cube())
        print("Square Root:", self.square_root())


# Object
calc = Calculator(4)

# Call method
calc.show()
