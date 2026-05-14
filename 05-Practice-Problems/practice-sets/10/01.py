class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"PIN: {self.pin}")
        print(f"Company: {Programmer.company}")
        print()


# Objects
p1 = Programmer("Umesh", 5000000, 583125)
p2 = Programmer("Rohan", 5000000, 583125)

# Display details
p1.show_details()
p2.show_details()
