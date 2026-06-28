class BankAccount:
    def __init__(self,name,acc_no,balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance
        self.history = []

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,value):
        if value >= 0:
            self.__balance = value
        else:
            raise ValueError("Balance cannot be negative")
        
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            self.history.append(f"Deposit Amount : {amount}")
            print(f"{amount} is deposited")
        else:
            raise ValueError("Deposit amount must be positive")
        
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            print(f"Your Withdrawn Amount: {amount}")
        elif amount <= 0:
            raise ValueError("Invalid Amount")
        elif amount > self.__balance:
            raise ValueError("Insufficient Balance")
        self.__balance -= amount
        self.history.append(f"Withdrawn Amount : {amount}")
        print(f"{amount} withdrawn successfully")

    def show_balance(self):
        print("Current Balance: ", self.__balance)

    def show_history(self):
        for i in self.history:
            print(i)

    def __str__(self):
        return(
            f"Name: {self.name}\n"
            f"Account No: {self.acc_no}\n"
            f"Balance: {self.__balance}")
    
    '''def __add__(self,other):
        total = self.__balance + other.__balance
        return f"Total Balance: {total}" '''
    
    def save(self):
        with open("accounts.txt", "a")as f:
            f.write(f"{self.name},{self.acc_no},{self.__balance} \n")

    

a1 = BankAccount("Anand",1805,1000000)
a2 = BankAccount("Aditi",1005, 1000000)

a1.withdraw(1000)
a2.withdraw(1)

print(a1)
print(a2)

a1.show_history()
a2.show_history()

#a1.save()
#a2.save()
    




        