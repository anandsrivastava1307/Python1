class BankAccount:
    def __init__(self,name,acc_no,balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance
        self.history = []

    @property
    def balance(self):
        return self.__balance

    def display(self):
        print("======Account Details======")
        print("Name: " ,self.name)
        print("Account Number: ",self.acc_no)
        print("Balance: ",self.__balance)

    def deposit(self,amount):
        if amount > 0:
            print(f"{amount} deposited successfully")
            self.__balance += amount
            self.history.append(f"Deposit: {amount}")
        else:
            print("Invalid Amount")

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid Amount")
        elif self.__balance < amount:
            print("Insufficient Balance")
        else:
            print(f"{amount} withdrawn successfully")
            self.__balance -= amount
            self.history.append(f"Withdrawn: {amount}")

    def transfer(self,reciever,amount):
        if amount<=0:
            print("Invalid Amount")
        elif self.__balance < amount:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            reciever.deposit(amount)
            self.history.append(f"Transferred: {amount} to {reciever.name}")
            reciever.history.append(f"Received: {amount} to {self.name}")
            print(f"{amount} Transfer Successfully")

    def show_history(self):
        print("========Transaction History===========")
        if not self.history:
            print("No Transactions")
        else:
            for item in self.history:
                print(item)

        


a1 = BankAccount("Aditi", 1805, 10000)
a2 = BankAccount("Anand", 1005, 50000)
#a1.withdraw(200)
#a1.deposit(100)
#a1.withdraw(500)
#a1.withdraw(50000)
#print(a1.balance)
a1.transfer(a2,200)
a2.transfer(a1,500)
a1.display()
a2.display()
a1.show_history()
a2.show_history()
#a2.deposit(500)
#a2.display()




        