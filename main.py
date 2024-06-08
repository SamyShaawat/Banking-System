from bank_accounts import *

Samy = BankAccount(1000, "Samy")
Mohamed = BankAccount(3000, "Mohamed")


Samy.getBalance()
Mohamed.getBalance()

Samy.deposit(200)

Mohamed.withdraw(1000)


Samy.transfer(30000, Mohamed)

Ahmed = InterestRewardsAccount(1000, "Ahmed")
Ahmed.getBalance()

Ahmed.deposit(200)

Ahmed.transfer(200, Samy)

Amr = SavingAccount(1000, "Amr")
Amr.getBalance()

Amr.deposit(200)

Amr.transfer(200, Samy)
