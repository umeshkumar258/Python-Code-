class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n ** 2}")

    def cube(self):
        print(f"The cube is {self.n ** 3}")
    
    def square_root(self):
        print(f"The square root is {self.n ** 0.5}")

    @staticmethod
    def hello():
        print("Hello Umesh")


a = Calculator(4)
a.square()
a.cube()
a.square_root()
a.hello()
