

class Train:

    def __init__(self,trainNo):
        self.trainNo = trainNo
    
    def book (self,trainNo,fro,to):
        print(f"Ticket is booked in train no:{trainNo} 
        {fro} to {to}")
    
    def getstatus(self, trainNo):
        print(f"Trian no:{trainNo} is running on time")

        


t = Train(525266)
t.book("kadabagere ","bengaluru")
