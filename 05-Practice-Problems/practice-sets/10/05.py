class Train:
    def __init__(self, train_no, train_name, seats):
        self.train_no = train_no
        self.train_name = train_name
        self.seats = seats

    def book_ticket(self, from_station, to_station):
        if self.seats > 0:
            self.seats -= 1
            print(f"✓ Ticket booked in {self.train_name}")
            print(f"Train No : {self.train_no}")
            print(f"From     : {from_station}")
            print(f"To       : {to_station}")
            print(f"Seats Left: {self.seats}")
        else:
            print("✗ No seats available")

    def get_status(self):
        print(f"{self.train_name} ({self.train_no}) is running on time")

    def get_available_seats(self):
        print(f"Available seats: {self.seats}")

    def __str__(self):
        return f"Train No: {self.train_no}, Train Name: {self.train_name}"


# Creating object
t = Train(525266, "Vande Bharat Express", 5)

print(t)
t.get_status()
t.get_available_seats()

t.book_ticket("Kadabagere", "Bengaluru")
