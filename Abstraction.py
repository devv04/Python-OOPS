from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance
    
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, transaction_fee=1.0):
        super().__init__(account_holder, balance)
        self.transaction_fee = transaction_fee

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        total_amount = amount + self.transaction_fee
        if total_amount > self.balance:
            print("Insufficient funds for this withdrawal including transaction fee.")
        else:
            self.balance -= total_amount
            print(f"Withdrew {amount} with a fee of {self.transaction_fee}. New balance is {self.balance}.")

a1=CheckingAccount("Alice", 1000)
a1.deposit(500)
a1.withdraw(200)
a1.withdraw(1500)