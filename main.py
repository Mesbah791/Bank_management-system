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
        print(f"Account created ,Your Account number =  {account_number}")
        
        
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
        
            
            if self.bank.accounts[account_number]['loan_taken'] < 2:
                self.bank.accounts[account_number]['loan_taken'] += 1
                self.bank.accounts[account_number]['balance'] += amount
                self.bank.total_available_balance -= amount
                self.bank.loan_given += amount
                print("Loan taken successfully")
                self.bank.accounts[account_number]['transaction_history'].append(f"Loan taken: {amount}")
           
    
    def transfer_money(self, sender_account_number, receiver_account_number, amount):
      
        if self.bank.accounts[sender_account_number]['balance'] >= amount:
            self.bank.accounts[sender_account_number]['balance'] -= amount
    
            self.bank.accounts[receiver_account_number]['balance'] += amount
 
            self.bank.accounts[sender_account_number]['transaction_history'].append(f"Transferred: {amount}")
            self.bank.accounts[receiver_account_number]['transaction_history'].append(f"Received: {amount}")
            print(f"Successfully Transferred to {receiver_account_number}")
        else:
            print("Balance is not sufficient")
 




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
                account_type = input('Enter account type = ')
                user.createAccount(name, email, address, account_type)
                while True:
                    print(f"What are your looking for??")
                    print("1. Create another for money transfering")
                    print("2. Deposit money")
                    print("3. Withdraw money")
                    print("4. Check balance")
                    print("5. Check transaction history")
                    print("6. Take loan")
                    print("7. Transfer money")
                    print("8. Exit")
                    choice = int(input("Enter Your Choice : "))
                    if choice == 1:
                        name = input("Your name please : ")
                        email = input("Your Email please : ")
                        address = input("Your address please : ")
                        user = User(bank, name, email, address)
                        account_type = input("Your account type please : ")
                        user.createAccount(name, email, address, account_type)

                    elif choice == 2:
                        account_number = input('Your  account number please : ')
                        user_account = user.bank.accounts.get(account_number,None)
                        if user_account  is None:
                            print("Account does not exist ^_^")
                        else:
                            amount = int(input('Enter  the ammount: '))
                            user.deposit(account_number, amount)

                    elif choice == 3:
                        account_number = input('Your  account number please : ')
                        user_account = user.bank.accounts.get(account_number,None)
                        if user_account is None:
                            print("Account does not exist ^_^")
                        else:
                            amount = int(input('Enter the amount: '))
                            user.withdraw(account_number, amount)

                    elif choice == 4:
                        account_number = input('Your  account number please : ')
                        user_account = user.bank.accounts.get(account_number,None)
                        if user_account is None:
                            print("Account does not exist ^_^")
                        else :
                            user.check_available_balance(account_number)

                    elif choice == 5:
                        account_number = input('Your  account number please : ')
                        user_account = user.bank.accounts.get(account_number,None)
                        if user_account is None:
                            print("Account does not exist ^_^")
                        else:
                            user.check_transaction_history(account_number)

                    elif choice == 6:
                        if user.bank.is_loan_available == True:
                            account_number = input('Your  account number please : ')
                            
                            user_account = user.bank.accounts.get(account_number,None)
                            if user_account is None:
                                print("Account does not exist ^_^")
                            else:
                                amount = int(input('Enter the amount : '))
                                user.take_loan(account_number, amount)

                    elif choice == 7:
                        sender_account_number = input('Enter your account number: ')
                        sender_user_account = user.bank.accounts.get(sender_account_number,None)
                        receiver_account_number = input('Enter receiver account number: ')
                        receiver_user_account = user.bank.accounts.get(receiver_account_number,None)
                        
                        
                        if sender_user_account is None or receiver_user_account is None:
                            print("Account does not exist ^_^")
                        else:
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
                account_type = input('Your account type please :  ')
                admin.createAccount(name, email, address, account_type)
                while True:
                    print(f"What you are looking for??")
                    
                    print("1. Delete account")
                    print("2. View accounts")
                    print("3. Check bank total available balance")
                    print("4. Total loan given")
                    print("5. Turn on or off loan")
                    print("6. Exit")
                    choice = int(input("Enter Your Choice : "))
                    

                    if choice == 1:
                        account_number = input('Enter your account number: ')
                        admin_account = admin.bank.accounts.get(account_number,None)
                        if admin_account is None:
                            print("Account does not exist ^_^")
                        else:
                            admin.delete_account(account_number)

                    elif choice == 2:
                        admin.view_accounts()

                    elif choice == 3:
                        admin.check_total_balance()

                    elif choice == 4:
                        admin.loan_given()

                    elif choice == 5:
                        admin.loan_on_of()

                    elif choice == 6:
                        break

                    else:
                        print("Invalid Input")

            elif choice == 3:
                break
            else:
                print("Invalid Input")    
        

Main()