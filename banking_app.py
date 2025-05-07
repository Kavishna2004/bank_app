accounts = {} 
users = [] 
transaction_history = [] 

print("---WELCOME TO MINI BANKING---")
#-------------------------------create customer-----------------------------------------
def create_customer():
    try:
        customer_id = input("Enter the customer ID: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        nic = input("Enter the NIC number: ")
        account_number = input("Enter the account number: ")

        with open("account.txt", "a") as file:
            file.write(f'{customer_id}\t{username}\t{password}\t{nic}\t{account_number}\t{balance}\n')
    except ValueError:
        print("You must enter a number only!")

# ---------------------------------- Account Creation -----------------------------------
def create_account():
    try:
        customer_id = input("Enter the customer ID: ")
        username = input("Enter your username: ")
        password = input("Enter the password: ")
        nic = input("Enter the NIC number: ")
        account_number = input("Enter the account number: ")
        balance = 0 

        accounts[account_number] = {
            "customer_id": customer_id,
            "username": username,
            "password": password,
            "NIC": nic,
            "balance": balance
        }

        with open("account.txt", "a") as file:
            file.write(f'{customer_id}\t{username}\t{password}\t{nic}\t{account_number}\t{balance}\n')

        print("Account created successfully!")
    
    except Exception as e:
        print("Error: ", e)

# ---------------------------------- Deposit Option -----------------------------------
def deposit(account_number):
    try:
        if account_number in accounts:
            deposit_amount = int(input("Enter your deposit amount: $"))
            if deposit_amount > 0:
                accounts[account_number]["balance"] += deposit_amount
                print(f"Deposit successful! New Balance: ${accounts[account_number]['balance']:.2f}")

                with open("transactions.txt", "a") as file:
                    file.write(f"{account_number}\tDeposit\t${deposit_amount}\t{accounts[account_number]['balance']}\n")
            else:
                print("Invalid amount! Deposit must be greater than 0.")
        else:
            print("Account not found!")
    
    except ValueError:
        print("You must enter a valid number!")

# --------------------------------- Withdraw Option -----------------------------------
def withdraw(account_number):
    try:
        if account_number in accounts:
            withdrawal_amount = int(input("Enter your withdrawal amount: $"))
            if withdrawal_amount > 0 and accounts[account_number]["balance"] >= withdrawal_amount:
                accounts[account_number]["balance"] -= withdrawal_amount
                print(f"Withdrawal successful! New Balance: ${accounts[account_number]['balance']:.2f}")

                with open("transactions.txt", "a") as file:
                    file.write(f"{account_number}\tWithdrawal\t${withdrawal_amount}\t{accounts[account_number]['balance']}\n")
            else:
                print("Insufficient balance or invalid amount!")
        else:
            print("Account not found!")
    
    except ValueError:
        print("You must enter a valid number!")

# ------------------------------- Check Balance -----------------------------------
def show_balance(account_number):
    if account_number in accounts:
        print(f"Your current account balance is: ${accounts[account_number]['balance']}")
    else:
        print("Account not found!")

# ------------------------------- Transaction History ------------------------------
def all_the_transaction_history():
    try:
        with open("transactions.txt", "r") as file:
            transactions = file.readlines()

        if transactions:
            print("\nTransaction History:")
            for transaction in transactions:
                data = transaction.split('\t')
                account_number = data[0]
                transaction_type = data[1]
                amount = data[2]
                balance = data[3].strip()
                print(f"Account Number: {account_number}, Type: {transaction_type}, Amount: {amount}, New Balance: {balance}")
        
        else:
            print("No transactions available.")
    
    except FileNotFoundError:
        print("Transaction history file not found!")

# ------------------------------- Admin Login and Menu -----------------------------
def admin_login():
    admin_user_ID = int(input("Enter your user ID: "))
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user["id"] == admin_user_ID and user["username"] == username and user["password"] == password:
            print("Login Successful!")
            admin_menu(username)
            return

    print("Login Failed. Please try again.")

# ------------------------------- Admin Menu ---------------------------------------
def admin_menu(username):
    while True:
        print("-----WELCOME TO MINI BANKING----")
        print("1. Create customer")
        print("2. Create Account")
        print("3. View Transaction History")
        print("4. Exit")
        
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            create_account()
        elif choice == "3":
            all_the_transaction_history()
        elif choice == "4":
            print("Thank you for your service. Goodbye!")
            break
        else:
            print("Invalid Input. Try again!")

# ------------------------------- Customer Login and Menu --------------------------
def customer_login():
    account_number = input("Enter your account number: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if account_number in accounts and accounts[account_number]["username"] == username and accounts[account_number]["password"] == password:
        print(f"Login Successful. Welcome Customer {username}")
        customer_menu(account_number)
    else:
        print("Login Failed. Please check your credentials.")

# ------------------------------- Customer Menu -----------------------------------
def customer_menu(account_number):
    while True:
        print("-----WELCOME TO MINI BANKING----")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            deposit(account_number)
        elif choice == "2":
            withdraw(account_number)
        elif choice == "3":
            show_balance(account_number)
        elif choice == "4":
            all_the_transaction_history()
        elif choice == "5":
            print("Thank you for your service. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# ------------------------------- Main Menu ---------------------------------------
while True:
    role = input("Enter the Role (admin or customer): ").lower()
    if role == "admin":
        admin_login()
    elif role == "customer":
        customer_login()
    else:
        print("Login Unsuccessful. Try Again!")
