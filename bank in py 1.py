class Account:
    def __init__(self):
        self.balance = 0
        print(" The account is created.")

    def deposit(self):
        amount = float(input("Enter the amount you want to deposit: "))
        self.balance = self.balance + amount
        print ("\n Deposit is successful and the updated balance is %f" % self.balance)

    def withdrawal(self):
        amount = float(input("Enter the amount you want to withdrawal: "))
        if (self.balance >= amount):
            self.balance = self.balance - amount
            print("\n withdrawal is successful and the remaining balance is %f" % self.balance)
        else:
            print("Insufficient Balance")


    def balance_enquiry(self):
        print ("\n Recent balance in the account is %f" % self.balance)

acc =Account()
acc.deposit()
acc.withdrawal()
acc.balance_enquiry()

