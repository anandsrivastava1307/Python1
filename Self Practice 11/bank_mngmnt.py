class BankAccount:
    def __init__(self,name,acc_no,balance):
        self.name = name 
        self.acc_no = acc_no
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self,balance):
        self.__balance = balance

    def Deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Your deposit amount is : {amount}")
            print("Successfully deposit")
        else:
            print("Amount must be greater than 0")

    def Withdraw(self,withdraw):
        if 0 <withdraw<=self.__balance:
            self.__balance -= withdraw
            print(f"Your withdraw amount is : {withdraw}")
            print("Successfully Withdraw")
        else:
            print("Insufficient balance")

    def Check_balance(self):
        print(f"Current Balance : {self.__balance}")

class Saving_account(BankAccount):
    def __init__(self, name, acc_no, balance):
        super().__init__(name, acc_no, balance)
        self.interest_rate = 4

    def add_interest(self):
        interest = (self.__balance)*(self.interest_rate)/100
        self.__balance += interest
        print(f"Interest Added: {interest}")
        print(f"New Balance: {self.__balance}")


b1 = BankAccount("Anand", 1234, 15000000)
b2 = Saving_account("Anand", 1234, 15000000)
b2.add_interest()

while True:
    print("\n===== Bank Management System =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        amount = int(input("Enter your amount: "))
        b1.Deposit(amount)
        

    elif choice == "2":
        withdraw = int(input("Enter withdraw amount: "))
        b1.Withdraw(withdraw)
        

    elif choice == "3":
        b1.Check_balance()
        

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")

# b1.check_balance()


