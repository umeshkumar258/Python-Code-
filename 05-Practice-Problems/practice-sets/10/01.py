class Programmer:
    company = "Microsoft"   # Class variable

    def __init__(self, name: str, salary: int, pin: int):
        self.name = name
        self.salary = salary
        self.pin = pin

    def __str__(self):
        return f"Name: {self.name}, PIN: {self.pin}, Salary: {self.salary}, Company: {self.company}"


p = Programmer("Umesh", 5_000_000, 583125)
r = Programmer("Rohan", 5_000_000, 583125)

print(p)
print(r)
