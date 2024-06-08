# Bank Account Management System

This project provides a basic implementation of a bank account management system with support for different account types and financial operations. It demonstrates how to create accounts, handle transactions, and manage funds through Python classes.

## Files

- [`bank_accounts.py`](#bank_accountspy): Contains the core classes defining various types of bank accounts and their operations.
- [`main.py`](#mainpy): Demonstrates the usage of the classes in `bank_accounts.py` through practical examples.

---

## `bank_accounts.py`

This module implements the following classes:

### `BalanceException`

A custom exception class used to handle cases where a transaction is attempted with insufficient funds.

### `BankAccount`

Represents a standard bank account with basic operations.

#### Attributes

- `balance`: The current balance of the account.
- `name`: The name of the account holder.

#### Methods

- `__init__(self, initialAmount, accountName)`: Initializes a new account with the specified balance and name.
- `getBalance(self)`: Prints the current balance of the account.
- `deposit(self, amount)`: Deposits the specified amount into the account and prints the new balance.
- `viableTransaction(self, amount)`: Checks if the account has sufficient funds for the transaction.
- `withdraw(self, amount)`: Withdraws the specified amount if funds are sufficient; otherwise raises a `BalanceException`.
- `transfer(self, amount, account)`: Transfers the specified amount to another account if funds are sufficient.

### `InterestRewardsAccount`

A subclass of `BankAccount` that provides a 5% interest reward on deposits.

#### Methods

- `deposit(self, amount)`: Adds a 5% interest to the deposited amount and prints the new balance.

### `SavingAccount`

A subclass of `InterestRewardsAccount` that charges a fee for withdrawals.

#### Attributes

- `fee`: A fixed fee for withdrawals.

#### Methods

- `__init__(self, initialAmount, accountName)`: Initializes a savings account with the specified balance, name, and withdrawal fee.
- `withdraw(self, amount)`: Applies a withdrawal fee in addition to the withdrawn amount and prints the new balance.

---

## `main.py`

This script demonstrates the functionality of the classes in `bank_accounts.py`:

1. **Creating Standard Bank Accounts**

    ```python
    Samy = BankAccount(1000, "Samy")
    Mohamed = BankAccount(3000, "Mohamed")
    ```

2. **Checking Balances**

    ```python
    Samy.getBalance()
    Mohamed.getBalance()
    ```

3. **Depositing Money**

    ```python
    Samy.deposit(200)
    ```

4. **Withdrawing Money**

    ```python
    Mohamed.withdraw(1000)
    ```

5. **Attempting a Large Transfer**

    ```python
    Samy.transfer(30000, Mohamed)  # Expected to fail due to insufficient funds
    ```

6. **Creating an Interest Rewards Account**

    ```python
    Ahmed = InterestRewardsAccount(1000, "Ahmed")
    Ahmed.getBalance()
    Ahmed.deposit(200)
    Ahmed.transfer(200, Samy)
    ```

7. **Creating a Savings Account**

    ```python
    Amr = SavingAccount(1000, "Amr")
    Amr.getBalance()
    Amr.deposit(200)
    Amr.transfer(200, Samy)  # Transfer includes a withdrawal fee
    ```

---

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/bank-account-management.git
    cd bank-account-management
    ```

2. **Run the example script:**

    ```bash
    python main.py
    ```

This will execute the operations defined in `main.py` and print the account activities and balances.

---

## Example Output

```text
Account created for Samy with Balance $1000.00
Account created for Mohamed with Balance $3000.00

Account Samy balance is $1000.00
Account Mohamed balance is $3000.00

Deposit Completed. 
You deposited $200.00 in  Samy account
Account Samy balance is $1200.00

Withdrawal Completed. 
You withdrew $1000.00 from Mohamed account
Account Mohamed balance is $2000.00

Withdraw interrupted. ❌ 
Sorry, account 'Samy' only has a balance of $1200.00

Account created for Ahmed with Balance $1000.00

Account Ahmed balance is $1000.00

Deposit Completed. 
Account Ahmed balance is $1210.00

******************

Begining Transfer.. 🚀
Withdrawal Completed. 
You withdrew $200.00 from Ahmed account
Account Ahmed balance is $1010.00

Deposit Completed. 
You deposited $200.00 in  Samy account

Transfer Completed! ✅

******************

Account created for Amr with Balance $1000.00

Account Amr balance is $1000.00

Deposit Completed. 
Account Amr balance is $1210.00

******************

Begining Transfer.. 🚀
Withdrawal Completed. 
Account Amr balance is $1005.00
Deposit Completed. 
You deposited $200.00 in  Samy account

Transfer Completed! ✅

******************
