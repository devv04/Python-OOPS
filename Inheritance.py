class Account:
    def __init__(self, name,balance):
        print("Account __init__ called")
        self.name =name
        self.__balance=balance

    def deposit(self,amount):
        self.amount=amount
        print(f"Money in Account before deposit is:{self.__balance}")
        self.__balance+=amount
        print(f"Money in Account after deposit is:{self.__balance}")

    def withdraw(self,amount):
        self.amount=amount
        print(f"Money in Account before withdrawal is: {self.__balance}")
        if amount>self.__balance:
            print(f"Insufficient balance")
        else:
            self.__balance-=amount
            print(f"Money in Account after withdrawal is: {self.__balance}")
    
    def get_balance(self):
            return self.__balance
        
   


class SavingsAccount(Account):
    print("SavingsAccount __init__ called")
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def add_interest(self):
        interest = self.get_balance() * 0.05
        self.deposit(interest)


    
d1=SavingsAccount("Dev",5000)

d1.add_interest()
print(f"Available balance after adding interest is: {d1.get_balance()}")