class BankAccount:
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.name = accountName
        print(f"\nAccount created for {self.name} with Balance ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount {self.name} balance is ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(
            f"\nDeposit Completed. \nYou deposited ${amount:.2f} in  {self.name} account"
        )
        self.getBalance()
