class calculator:
    def __init__(self,n):
        self.n = n


    def square(self):
        print(f"the square is {self.n*self.n}")

    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")
    
    def roote(self):
        print(f"the square roote {self.n**1/2}")

a = calculator(4)
a.square()
a.cube()
a.roote()

