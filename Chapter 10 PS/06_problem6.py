'''Can you change the self-parameter inside a class to something else (say "anand"). Try 
changing self to "slf" or "anand" and see the effects.'''

from random import randint
class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no : {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no : {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(12399)
t.book("Rampur", "Rishikesh")
t.getStatus()
t.getFare("Rampur", "Rishikesh")