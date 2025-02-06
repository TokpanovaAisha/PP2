# Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
# Withdrawals may not exceed the available balance. 
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance 

    def deposit(self, cash):
        self.balance += cash
        print(f"You added {cash} to your balance!")
        print(f"On your balance:", self.balance)

    def withdraw(self, cash):
        if self.balance < cash:
            print("You do not have enough cash!")
            print(f"On your balance:", self.balance)
        else:
            self.balance -= cash
            print(f"You withdrawed {cash} from your balance!")
            print(f"On your balance:", self.balance)


a = Account("Aisha", 5000)
a.deposit(2000)
a.deposit(1000)
a.withdraw(3000)
a.withdraw(10000)