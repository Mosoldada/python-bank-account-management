def is_valid(item):
    try:
        int(item)
    except ValueError:
        print("Please enter number values")
        return False
    return True

def validation_int(message):
    while True:
        item = input(message).strip().lower()
        if not item:
            print("Please enter a number")
            continue
        elif not is_valid(item):
            continue
        return int(item)


def show_dict(dictionary):
    if not dictionary:
        print("There is nothing to show")
    for key, value in dictionary.items():
        print(f"{key}: {value}")
        
accounts = {}
account_number = 1001

def add_account(accounts, account_number, name, balance):
    accounts[account_number]['name'] = name
    accounts[account_number]['balance'] = balance

def ask_to_continue():
    while True:
        question = input("Would you like to continue (y/n)? ").strip().lower()
        if question != "y" and question != "n":
            print("Please enter y or n")
            continue
        break
    return question




while True:
    print("*" * 10)
    print("***Welcome to Bank Account Management***")
    print("Please Choose Between Following Actions: ")
    print("1. Create Account\n""2. Show Accounts\n""3. Search Account\n""4. Deposit")
    print("5. Withdraw\n""6. Transfer\n""7. Report\n""8. Exit")
    print("*" * 10)
    choice = validation_int("Please enter your choice: ")

    if choice < 1 or choice > 8:
        print("Please choose between 1 and 8")
        continue

    if choice == 1:
        while True:
            name = input("Please enter your name: ").strip().lower()
            if not name:
                print("Please enter your name")
                continue
            break
        while True:
            balance = validation_int("Please enter your balance: ")
            if balance < 0:
                print("Balance must be greater or equal to 0")
                continue
            break
        accounts[account_number] = {}
        add_account(accounts, account_number, name, balance)
        print("Account created successfully")
        print(f"Account number: {account_number}")
        print(f"Account name: {name}")
        print(f"Account balance: {balance}")
        account_number += 1

    elif choice == 2:
        show_dict(accounts)

    elif choice == 3:
        if not accounts:
            print("There is nothing to search.")
            continue
        print("Choose your search method: ")
        print("1. Search by account number\n""2. Search by account holder name")
        while True:
            search_choice = validation_int("Please enter your search method: ")
            if search_choice < 1 or search_choice > 2:
                print("Please choose between 1 and 2")
                continue
            break
        if search_choice == 1:
            while True:
                search_account_number = validation_int("Please enter your account number: ")
                if search_account_number < 1001:
                    print("Account number must be equal or greater than 1001")
                    continue

                if search_account_number not in accounts:
                    print("Account number not found")
                else:
                    print(f"{search_account_number}: {accounts[search_account_number]}")
                if ask_to_continue() == 'y':
                    continue
                break

        elif search_choice == 2:
            while True:
                search_account_holder_name = input("Please enter your account holder name: ").strip().lower()
                if not search_account_holder_name:
                    print("Please enter your account holder name")
                    continue

                search_found = False
                for key, value in accounts.items():
                    if value['name'] == search_account_holder_name:
                        print(f"{key}: {accounts[key]}")
                        search_found = True

                if not search_found:
                    print("Account holder name not found")
                if ask_to_continue() == 'y':
                    continue
                break
    elif choice == 4:
        if not accounts:
            print("There is no account to deposit.")
            continue
        while True:
            condition = False
            while True:
                deposit_account = validation_int("Please enter your deposit account: ")
                if deposit_account < 1001:
                    print("Account number must be equal or greater than 1001")
                    continue
                if deposit_account not in accounts:
                    print("Account number not found")
                    if ask_to_continue() == 'y':
                        continue
                    else:
                        condition = True

                break
            if condition:
                break

            while True:
                deposit_amount = validation_int("Please enter your deposit amount: ")
                if deposit_amount <= 0:
                    print("Deposit amount must be greater than 0")
                    continue
                accounts[deposit_account]['balance'] += deposit_amount
                print("Deposit amount added successfully")
                print(f"Account number: {deposit_account}")
                print(f"Account name: {accounts[deposit_account]['name']}")
                print(f"Balance: {accounts[deposit_account]['balance']}")

                break
            if ask_to_continue() == 'y':
                continue
            else:
                break
    elif choice == 5:
        if not accounts:
            print("There is no account to withdraw.")
            continue
        while True:
            withdraw_condition = False
            while True:
                withdraw_account = validation_int("Please enter your withdraw account: ")
                if withdraw_account < 1001:
                    print("Account number must be equal or greater than 1001")
                    continue
                if withdraw_account not in accounts:
                    print("Account number not found")
                    if ask_to_continue() == 'y':
                        continue
                    else:
                        withdraw_condition = True
                break
            if withdraw_condition:
                break
            while True:
                withdraw_amount = validation_int("Please enter your withdraw amount: ")
                if withdraw_amount <= 0:
                    print("Withdraw amount must be greater than 0")
                    continue
                new_withdraw_condition = False
                if withdraw_amount > accounts[withdraw_account]['balance']:
                    print("There is not enough money to withdraw")
                    if ask_to_continue() == 'y':
                        continue
                    else:
                        new_withdraw_condition = True
                else:
                    print("Withdraw Successful")
                    accounts[withdraw_account]['balance'] -= withdraw_amount
                    print(f"Account number: {withdraw_account}")
                    print(f"Account name: {accounts[withdraw_account]['name']}")
                    print(f"Balance: {accounts[withdraw_account]['balance']}")
                if new_withdraw_condition:
                    print("Withdraw operation finished")
                break
            print("New withdraw operation")
            if ask_to_continue() == 'y':
                continue
            break
    elif choice == 6:
        if len(accounts) < 2:
            print("There aren't enough accounts to transfer.")
            continue
        while True:
            transfer_condition = False
            while True:
                source_account = validation_int("Please enter your source account number: ")
                if source_account < 1001:
                    print("Account number must be equal or greater than 1001")
                    continue
                if source_account not in accounts:
                    print("Account number not found")
                    if ask_to_continue() == 'y':
                        continue
                    else:
                        transfer_condition = True
                break
            if transfer_condition:
                print("Transfer operation canceled")
                break
            while True:
                destination_account = validation_int("Please enter your destination account number: ")
                if destination_account < 1001:
                    print("Account number must be equal or greater than 1001")
                    continue
                if destination_account not in accounts:
                    print("Account number not found")
                    if ask_to_continue() == 'y':
                        continue
                    else:
                        transfer_condition = True
                if source_account == destination_account:
                    print("Source and destination accounts can not be equal")
                    if ask_to_continue() == 'y':
                        continue
                    else:
                        transfer_condition = True

                break

            if transfer_condition:
                print("Transfer operation canceled")
                break
            while True:
                transfer_amount = validation_int("Please enter your transfer amount: ")
                new_amount_condition = False
                if transfer_amount <= 0:
                    print("Transfer amount must be greater than 0")
                    if ask_to_continue() == 'y':
                        continue
                    else:
                        new_amount_condition = True

                if new_amount_condition:
                    print("Transfer operation canceled")
                    break


                if accounts[source_account]['balance'] < transfer_amount:
                    print("There is not enough money to transfer.")
                    print(f"Account number: {source_account}")
                    print(f"Balance: {accounts[source_account]['balance']}")
                    print(f"Account number: {destination_account}")
                    print(f"Balance: {accounts[destination_account]['balance']}")
                    if ask_to_continue() == 'y':
                        continue
                    else:
                        new_amount_condition = True
                else:
                    print("Transfer Successful")
                    accounts[source_account]['balance'] -= transfer_amount
                    accounts[destination_account]['balance'] += transfer_amount
                    print("Transfer From: ")
                    print(f"Account number: {source_account}")
                    print(f"Transfer amount: {transfer_amount}")
                    print(f"Balance: {accounts[source_account]['balance']}")
                    print("Transfer To: ")
                    print(f"Account number: {destination_account}")
                    print(f"Transfer amount: {transfer_amount}")
                    print(f"Balance: {accounts[destination_account]['balance']}")
                    break
                if new_amount_condition:
                    print("Transfer operation canceled")
                    break
            print("New transfer operation")
            if ask_to_continue() == 'y':
                continue
            break
    elif choice == 7:
        if not accounts:
            print("There is no accounts.")
            continue

        print("Choose the report that you want: ")
        print("1. Check account\n""2. Total accounts\n""3. Total Balance\n""4. Max Balance")
        while True:
            report_choice = validation_int("Please enter your report choice: ")
            if report_choice < 1 or report_choice > 4:
                print("Please enter your report choice between 1 and 4")
                continue
            break
        if report_choice == 1:
            while True:
                report_account = validation_int("Please enter your account number: ")
                if report_account < 1001:
                    print("Account number must be equal or greater than 1001")
                    continue
                if report_account not in accounts:
                    print("Account number not found")
                    if ask_to_continue() == 'y':
                        continue
                else:
                    print(f"Account number: {report_account}")
                    print(f"Name: {accounts[report_account]['name']}")
                    print(f"Balance: {accounts[report_account]['balance']}")
                break

        elif report_choice == 2:
            total_accounts = 0
            for key in accounts:
                total_accounts += 1
            print(f"Total accounts: {total_accounts}")
        elif report_choice == 3:
            total_balance = 0
            for value in accounts.values():
                total_balance += value['balance']
            print(f"Total balance: {total_balance}")
        elif report_choice == 4:
            if len(accounts) == 1:
                for key in accounts:
                    print(f"Account Number: {key}")
                    print(f"Max Balance: {accounts[key]['balance']}")
                    print(f"Name: {accounts[key]['name']}")
            elif len(accounts) > 1:
                max_balance = 0
                max_accounts = {}
                for key, value in accounts.items():
                    if value['balance'] >= max_balance:
                        max_balance = value['balance']
                        max_account_name = value['name']
                        max_account_number = key
                for key in accounts:
                    if key != max_account_number and accounts[key]['balance'] == max_balance:
                        max_accounts[key] = {}
                        max_accounts[key]['balance'] = accounts[key]['balance']
                        max_accounts[key]['name'] = accounts[key]['name']
                if not max_accounts:
                    print(f"Max account number : {max_account_number}")
                    print(f"Account name: {max_account_name}")
                    print(f"Account balance: {max_balance}")
                else:
                    print("Max Accounts: ")
                    for key in max_accounts:
                        print("*" * 5)
                        print(f"Max account number: {key}")
                        print(f"Account name: {max_accounts[key]['name']}")
                        print(f"Account balance: {max_accounts[key]['balance']}")
                    print("*" * 5)
                    print(f"Max account number : {max_account_number}")
                    print(f"Account name: {max_account_name}")
                    print(f"Account balance: {max_balance}")






    elif choice == 8:
        print("Thank you for choosing Bank Account Management")
        break
