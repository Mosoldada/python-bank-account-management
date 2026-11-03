# Bank Account Management (Python CLI)

A console-based bank account management project built with Python. It demonstrates Python fundamentals such as dictionaries, functions, loops, conditions, and input validation.

> **Educational project only.** This is not a real banking application.

## Features

- Create a new account with a holder name and an initial balance
- Display all accounts
- Search by account number or account holder name
- Deposit money into an account
- Withdraw money with a balance check
- Transfer money between different accounts
- View reports:
  - Details of an account
  - Total number of accounts
  - Total balance across accounts
  - Account(s) with the highest balance

## Requirements

- Python 3
- No external packages required

## Run the program

1. Download `bank_account_management.py`.
2. Open a terminal in the folder containing the file.
3. Run:

   ```bash
   python bank_account_management.py
   ```

   On systems where Python 3 uses the `python3` command, run:

   ```bash
   python3 bank_account_management.py
   ```

4. Enter a number from **1 to 8** to select an action.

## Menu

```text
1. Create Account
2. Show Accounts
3. Search Account
4. Deposit
5. Withdraw
6. Transfer
7. Report
8. Exit
```

The first account number is **1001**. Newly created accounts receive the next number in sequence.

## Notes and limitations

- Account information is stored **in memory**. Closing the program erases all accounts and transactions.
- Balances and transaction amounts use **whole numbers (integers)**; decimals are not supported.
- Account holder names are normalized to lowercase.
- This project has no login system, database, or persistent transaction history.

## Learning goals

This project practices:

- Working with dictionaries and nested data
- Creating reusable functions
- Validating user input
- Handling menu-driven program flow
- Implementing simple business rules

## Project structure

```text
bank-account-management/
├── bank_account_management.py
└── README.md
```
