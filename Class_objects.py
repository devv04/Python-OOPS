class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        print(f"Available balance before deposit: {self.balance}")
        self.balance += amount
        print(f"Available balance after deposit: {self.balance}")

    def withdraw(self, amount):
        print(f"Available balance before withdraw: {self.balance}")
        if amount > self.balance:
            print("Withdrawal failed: Insufficient balance")
        else:
            self.balance -= amount
            print(f"Available balance after withdraw: {self.balance}")

    def display(self):
        print(
            f"Account Holder: {self.account_holder} | "
            f"Current Balance: {self.balance}"
        )


# Objects
A1 = BankAccount("DEV", 5000)
A2 = BankAccount("RAM", 10000)

# Operations
A1.deposit(2000)
A1.withdraw(1000)
A1.withdraw(10000)
A1.display()
A2.deposit(5000)
A2.withdraw(3000)   
A2.display()