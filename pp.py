# class Account:
#     def __init__(self, account_number, account_holder, initial_balance=0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = initial_balance

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Deposit amount must be positive!")
#         else:
#             self.balance += amount
#             print(f"Deposited {amount}. New balance is {self.balance}")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdrawal amount must be positive!")
#         elif amount > self.balance:
#             print("Insufficient funds!")
#         else:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance is {self.balance}")

#     def check_balance(self):
#         print(f"Account balance: {self.balance}")


# class BankingSystem:
#     def __init__(self):
#         self.accounts = {}

#     def create_account(self, account_number, account_holder, initial_balance=0):
#         if account_number in self.accounts:
#             print("Account number already exists!")
#         else:
#             self.accounts[account_number] = Account(account_number, account_holder, initial_balance)
#             print(f"Account created for {account_holder} with account number {account_number}")

#     def get_account(self, account_number):
#         account = self.accounts.get(account_number)
#         if not account:
#             print("Account not found!")
#         return account


# def main():
#     system = BankingSystem()

#     while True:
#         print("\nWelcome to the Banking System")
#         print("1. Create an Account")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Check Balance")
#         print("5. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             acc_num = input("Enter account number: ")
#             acc_holder = input("Enter account holder's name: ")
#             initial_balance = float(input("Enter initial balance (optional, default is 0): ") or 0)
#             system.create_account(acc_num, acc_holder, initial_balance)

#         elif choice == "2":
#             acc_num = input("Enter account number: ")
#             account = system.get_account(acc_num)
#             if account:
#                 amount = float(input("Enter amount to deposit: "))
#                 account.deposit(amount)

#         elif choice == "3":
#             acc_num = input("Enter account number: ")
#             account = system.get_account(acc_num)
#             if account:
#                 amount = float(input("Enter amount to withdraw: "))
#                 account.withdraw(amount)

#         elif choice == "4":
#             acc_num = input("Enter account number: ")
#             account = system.get_account(acc_num)
#             if account:
#                 account.check_balance()

#         elif choice == "5":
#             print("Thank you for using the Banking System!")
#             break

#         else:
#             print("Invalid choice! Please try again.")
#===============================================================

# if __name__ == "__main__":
#     main()
    

balance = 100000
def deposit():
    global balance
    try:
        deposit_amount = int(input("Enter your deposit amount: $"))
        if deposit_amount > 0:
           balance += deposit_amount
           print(f"Deposit successful! New Balance: $ {balance:.2f}")
        else:
            print("Invalid amount! Deposit must be greater than 0.")

    except ValueError:
        print("You must enter a number only!")

def withdraw_amount():
    global balance 
    try:
        withdrawal_amount = int(input("Enter your withdrawal amount: $"))
        if withdrawal_amount > 0 and balance >= withdrawal_amount:
            balance -= withdrawal_amount  
            print(f"Withdrawal successful! New Balance: ${balance:.2f}")
        else:
            print("Insufficient balance or invalid amount!")
    except ValueError:
            print("You must enter a number only!")--

def show_balance():
    name = input("Enter your username: ")
    password = int(input("Enter your password: "))
    
    if name == username and password == pwd:
        print(f"Your current account balance is: $ {balance}")
    else:
        print("Trt Again!")

deposit()
withdraw_amount()
show_balance()

=====================================
balance = 100000

def deposit():
    global balance
    try:
        deposit_amount = int(input("Enter your deposit amount: $"))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"Deposit successful! New Balance: $ {balance:.2f}")
        else:
            print("Invalid amount! Deposit must be greater than 0.")
    except ValueError:
        print("You must enter a number only!")

def withdraw_amount():
    global balance
    try:
        withdrawal_amount = int(input("Enter your withdrawal amount: $"))
        if withdrawal_amount > 0 and balance >= withdrawal_amount:
            balance -= withdrawal_amount  
            print(f"Withdrawal successful! New Balance: ${balance:.2f}")
        else:
            print("Insufficient balance or invalid amount!")
    except ValueError:
        print("You must enter a number only!")

def show_balance(username, password):
    stored_username = "user123"  
    stored_password = 4567  

    if username == stored_username and password == stored_password:
        print(f"Your current account balance is: $ {balance}")
    else:
        print("Try Again!")

def main():
    while True:
        print("\nBanking System Menu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        try:
            choice = int(input("Select an option: "))
            
            if choice == 1:
                deposit()
            elif choice == 2:
                withdraw_amount()
            elif choice == 3:
                user = input("Enter username: ")
                pwd = int(input("Enter password: "))
                show_balance(user, pwd)
            elif choice == 4:
                print("Thank you for using our banking system!")
                break
            else:
                print("Invalid choice! Please select a valid option.")
        
        except ValueError:
            print("You must enter a number only!")

# Run the program
main()

def create_account():
    try:
        customer_id = input("Enter the customer ID: ")
        user = input("Enter your username: ")
        
        # Handling password input securely
        pwd = input("Enter the password: ")
        hashed_pwd = hashlib.sha256(pwd.encode()).hexdigest()  # Hashing the password
        
        NIC = input("Enter the NIC number: ")
        account = input("Enter the account number: ")
        
        # Ensure balance is numeric=================
        ==============================================

        def main():
    admin = AdminMenu()

    while True:
        print("\n1. Admin Menu")
        print("2. Customer Menu")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            admin.admin_menu()
        elif choice == "2":
            # Customer menu (previously defined)
            print("Customer menu code here...")
        else:
            print("Invalid choice. Try again.")

        continue_choice = input("Do you want to continue? (y/n): ")
        if continue_choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()



    def create_account(self):
        name = input("Enter account holder name: ")
        if name not in self.accounts:
            new_account = Account(name)
            self.accounts[name] = new_account
            print(f"Account created for {name}.")
        else:
            print(f"Account for {name} already exists.")

    def delete_account(self):
        name = input("Enter account holder name to delete: ")
        if name in self.accounts:
            del self.accounts[name]
            print(f"Account for {name} has been deleted.")
        else:
            print(f"No account found for {name}.")

    def display_all_accounts(self):
        if self.accounts:
            print("\nList of all accounts:")
            for account_holder, account in self.accounts.items():
                print(f"Account holder: {account_holder}, Balance: {account.balance}")
        else:
            print("No accounts available.")

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    transaction_date TEXT,
    description TEXT,
    type TEXT,
    amount REAL,
    balance REAL,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);
