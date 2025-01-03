class Bank:
    def __init__(self,accno,name,typpe,balance):
        self.accno=accno
        self.name=name
        self.type=typpe
        self.balance=balance
    def deposit(self):
        amount=int(input("Enter the amount to deposit :"))
        self.balance+=amount
        print("Deposit succesfull")
        print("Your current status is :")
        print("Account no : {self.accno}")
        print("Account holder name : {self.name}")
        print("Account type : {self.typpe}")
        print("Current balane : Rs {self.balance}")
    def withdraw(self):
        amount1=int(input("Enter the amount to be withdrawn :"))
        if amount>self.balance:
            print("Not enough balance")
        else:
            self.balance-=amount1
