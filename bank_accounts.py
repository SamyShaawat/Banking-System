class BalanceException(Exception):
    pass

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
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(
                f"\nWithdrawal Completed. \nYou withdrew ${amount:.2f} from {self.name} account"
            )
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted. ❌ {error}')
    
    def transfer(self, amount, account):
        try:
            print('\n******************\n\nBegining Transfer.. 🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Completed! ✅\n\n******************')
        except BalanceException as error:
            print(f'\nTransfer interrupted. ❌ {error}')