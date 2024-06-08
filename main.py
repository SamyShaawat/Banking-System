from bank_accounts import *

Samy = BankAccount(1000, "Samy")
Mohamed = BankAccount(3000, "Mohamed")


Samy.getBalance()
Mohamed.getBalance()

Samy.deposit(200)

Mohamed.withdraw(1000)