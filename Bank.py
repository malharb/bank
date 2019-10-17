#Bank
class Account():

    def __init__(self,owner,balance):
        print("ACCOUNT CREATED\n")
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount Balance : {self.balance}"

    def deposit(self,dep):
        self.balance = self.balance + dep
        print("Deposit accepted")
        return self.balance

    def withdraw(self,withd):
        if withd>self.balance:
            return "Funds Unavailable!"
        else:
            self.balance = self.balance - withd
            print("Withdrawal accepted")
            return self.balance


input('Press ENTER to exit')
