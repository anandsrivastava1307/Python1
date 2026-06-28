class BankAccount:
    def __init__(self,name,acc_no,balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
        self.history = []

    def display(self):
        print("Name: " ,self.name)
        print("Account Number: ",self.acc_no)
        print("Balance: ",self.balance)

    def deposit(self,amount):
        if amount > 0:
            print(f"{amount} deposited successfully")
            self.balance += amount
            self.history.append(f"Deposit: {amount}")
        else:
            print("Invalid Amount")

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid Amount")
        elif self.balance < amount:
            print("Insufficient Balance")
        else:
            print(f"{amount} withdrawn successfully")
            self.balance -= amount
            self.history.append(f"Withdrawn: {amount}")

    def show_history(self):
        print("========Transaction History===========")
        for item in self.history:
            print(item)
        


a1 = BankAccount("Aditi", 1805, 10000)
a2 = BankAccount("Anand", 1005, 50000)
a1.withdraw(200)
a1.deposit(100)
a1.withdraw(500)
a1.withdraw(50000)
a1.withdraw(-100)
a1.display()
a1.show_history()
#a2.deposit(500)
#a2.display()




        