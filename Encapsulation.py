class Account:
    def __init__(self, name,balance):
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
    
d1=Account("Dev",5000)
d1.deposit(2000)    
d1.withdraw(1000)
print(f"Available balance is: {d1.get_balance()}")  

d1.withdraw(7000)

d2=Account("Ram",10000)
d2.deposit(5000)    
d2.withdraw(3000)
print(f"Available balance is: {d2.get_balance()}")
d2.withdraw(15000)
    
