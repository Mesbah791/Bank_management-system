class Bank:
    def __init__(self,name):
        self.name = name
        self.accounts = {}
        self.total_available_balance = 0
        self.loan_given = 0
        self.is_loan_available = True
        self.is_bankrupt = False
    
    def createAccount(self, name, email, account_type, address):
        account_number = f'{name}{email}'
        self.accounts[account_number] = {
            "name" : name,
            "email": email,
            "address": address,
            "account_type": account_type,
            "balance": 0,
            "loan_taken": 0,
            "transaction_history": []




        }
        print(f"Account created , Account number =  {account_number}")
        
        
    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted ")
        else:
            print("Account does not exist")
            
    def view_accounts(self):
        for account_number, details in self.accounts.items():
            print(f"Account Number: {account_number}, Name: {details['name']}, Email: {details['email']}, Address: {details['address']}, Account Type: {details['account_type']}")


class User:
    def __init__(self, bank, name, email, address):
        self.bank = bank
        self.name = name
        self.email = email
        self.address = address
    
    def createAccount(self, name, email, address, account_type):
        self.bank.createAccount(name, email, address, account_type)
    
    def deposit(self, account_number, amount):
        if self.bank.accounts[account_number]:   
            self.bank.accounts[account_number]['balance'] += amount
            self.bank.total_available_balance += amount
            print("Money diposited!!")
            self.bank.accounts[account_number]["transaction_history"].append(f"Deposited: {amount}")
        else:
            print("Account does not exist")

    def withdraw(self, account_number, amount):
        if self.bank.is_bankrupt == False:
            if self.bank.accounts[account_number]:
                if self.bank.accounts[account_number]['balance'] >= amount :
                    self.bank.accounts[account_number]['balance'] -= amount
                    self.bank.total_available_balance -= amount
                    print(f"Here is your money: {amount}")
                    self.bank.accounts[account_number]['transaction_history'].append(f"Withdrawn: {amount}")
                else:
                    print("Withdrawal amount exceeded")
            else:
                print("Account does not exist")
        else:
            print("The bank is bankrupt")
    

    def check_available_balance(self, account_number):
        if self.bank.accounts[account_number]:
            print(f'Balance: {self.bank.accounts[account_number]['balance']}')
        else:
            print("Account does not exist")
    
    def check_transaction_history(self, account_number):
        if self.bank.accounts[account_number]:
            print(":::::::Your transaction History:::::")
            for transaction in self.bank.accounts[account_number]["transaction_history"]:
                print(transaction)
        else:
            print("Account does not exist")
    
    def take_loan(self, account_number, amount):
        if self.bank.accounts[account_number]:
            if self.bank.is_loan_available == True:
                if self.bank.accounts[account_number]['loan_taken'] < 2:
                    self.bank.accounts[account_number]['loan_taken'] += 1
                    self.bank.accounts[account_number]['balance'] -= amount
                    self.bank.total_available_balance -= amount
                    self.bank.loan_given += amount
                    print("Loan taken successfully")
                    self.bank.accounts[account_number]['transaction_history'].append(f"Loan taken: {amount}")
            else:
                print("Loan facility is not available :(")
        else:
            print("Account does not exist")
    
    def transfer_money(self, sender_account_number, receiver_account_number, amount):
        if self.bank.accounts[sender_account_number] and self.bank.accounts[receiver_account_number]:
            if self.bank.accounts[sender_account_number]['balance'] >= amount:
                self.bank.accounts[sender_account_number]['balance'] -= amount
                self.bank.total_available_balance -= amount
                self.bank.accounts[receiver_account_number]['balance'] += amount
                self.bank.total_available_balance += amount
                self.bank.accounts[sender_account_number]['transaction_history'].append(f"Transferred: {amount}")
                self.bank.accounts[receiver_account_number]['transaction_history'].append(f"Received: {amount}")
                print(f"Successfully Transferred to {receiver_account_number}")
            else:
                print("Balance is not sufficient")
        else:
            print("Account does not exist")




class Admin:
    def __init__(self, bank, name, email, address):
        self.bank = bank
        self.name = name
        self.email = email
        self.address = address


    def createAccount(self, name, email, address, account_type):
        self.bank.createAccount(name, email, address, account_type)

    def delete_account(self, account_number):
        if self.bank.accounts[account_number]:
            self.bank.delete_account(account_number)
        else:
            print("Account does not exist")
    
    def view_accounts(self):
        self.bank.view_accounts()

    
    def loan_given(self):
        print(f'Total loan given by the bank: {self.bank.loan_given}')

    def check_total_balance(self):
        print(f'Total available balance of the bank: {self.bank.total_available_balance}')


    def loan_on_of(self):
        print('1. Turn on loan feature')
        print('2. Turn off loan feature')
        choice = int(input(f'Chose Your Options ?\t'))
        if choice == 1:
            self.bank.is_loan_available = True
            print('Loan feature turned on')
        elif choice == 2:
            self.bank.is_loan_available = False
            print('Loan feature turned off')
        else:
            print('Invalid choice')


class Main:
    bank = Bank('my bank')
    while True:
            print(f'Welcome to {bank.name}!!')
            print("1. User")
            print("2. Admin")
            print("3. Exit")
            choice = int(input("Enter your choice : "))
            if choice == 1:
                name = input("Enter Your Name : ")
                email = input("Enter Your Email : ")
                address = input("Enter Your Address : ")
                user = User(bank, name, email, address)

                while True:
                    print(f"Welcome {name}")
                    print("1. Create account")
                    print("2. Deposit money")
                    print("3. Withdraw money")
                    print("4. Check balance")
                    print("5. Check transaction history")
                    print("6. Take loan")
                    print("7. Transfer money")
                    print("8. Exit")
                    choice = int(input("Enter Your Choice : "))
                    if choice == 1:
                        account_type = input('Enter your account type: ')
                        user.createAccount(name, email, address, account_type)

                    elif choice == 2:
                        account_number = input('Enter your account number: ')
                        amount = int(input('Enter the amount: '))
                        user.deposit(account_number, amount)

                    elif choice == 3:
                        account_number = input('Enter your account number: ')
                        amount = int(input('Enter the amount: '))
                        user.withdraw(account_number, amount)

                    elif choice == 4:
                        account_number = input('Enter your account number: ')
                        user.check_available_balance(account_number)

                    elif choice == 5:
                        account_number = input('Enter your account number: ')
                        user.check_transaction_history(account_number)

                    elif choice == 6:
                        account_number = input('Enter your account number: ')
                        amount = int(input('Enter the amount: '))
                        user.take_loan(account_number, amount)

                    elif choice == 7:
                        sender_account_number = input('Enter your account number: ')
                        receiver_account_number = input('Enter receiver account number: ')
                        amount = int(input('Enter the amount: '))
                        user.transfer_money(sender_account_number, receiver_account_number, amount)

                    elif choice == 8:
                        break
                    
                    else:
                        print("Invalid Input!!")
            elif choice == 2:
                name = input("Enter Your Name : ")
                email = input("Enter Your Email : ")
                address = input("Enter Your Address : ")
                admin = Admin(bank, name, email, address)
                while True:
                    print(f"Welcome {name}")
                    print("1. Create account")
                    print("2. Delete account")
                    print("3. View accounts")
                    print("4. Check bank total available balance")
                    print("5. Total loan given")
                    print("6. Turn on or off loan")
                    print("7. Exit")
                    choice = int(input("Enter Your Choice : "))
                    if choice == 1:
                        account_type = input('Enter your account type: ')
                        admin.createAccount(name, email, address, account_type)

                    elif choice == 2:
                        account_number = input('Enter your account number: ')
                        admin.delete_account(account_number)

                    elif choice == 3:
                        admin.view_accounts()

                    elif choice == 4:
                        admin.check_total_balance()

                    elif choice == 5:
                        admin.loan_given()

                    elif choice == 6:
                        admin.loan_on_of()

                    elif choice == 7:
                        break

                    else:
                        print("Invalid Input")

            elif choice == 3:
                break
            else:
                print("Invalid Input")    
        

Main()