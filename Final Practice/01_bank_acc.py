class BankAccount:

    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance


    @property
    def balance(self):
        return self.__balance


    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            raise ValueError("Balance cannot be negative")


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully")

        else:
            raise ValueError("Deposit amount must be positive")


    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Invalid amount")

        elif amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amount

        print(f"{amount} withdrawn successfully")


    def show_balance(self):
        print("Current Balance:", self.__balance)


    def __str__(self):

        return (
            f"Name: {self.name}\n"
            f"Account No: {self.acc_no}\n"
            f"Balance: {self.__balance}"
        )


    def __add__(self, other):

        total = self.__balance + other.__balance

        return f"Total Balance: {total}"


    def save(self):

        with open("account.txt", "a") as f:

            f.write(
                f"{self.name},{self.acc_no},{self.__balance}\n"
            )


try:

    a1 = BankAccount("Anand", 101, 5000)

    a2 = BankAccount("Rahul", 102, 10000)


    a1.deposit(1000)

    a1.withdraw(2000)


    print()

    print(a1)

    print()

    print(a1 + a2)


    a1.save()
    a2.save()

except Exception as e:

    print("Error:", e)
        
        