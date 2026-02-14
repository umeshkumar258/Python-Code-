class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def get_status(self):
        print(f"Train no: {self.trainNo} is running on time")


t = Train(525266)

t.book("Kadabagere", "Bengaluru")
t.get_status()
