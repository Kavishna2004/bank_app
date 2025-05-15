import datetime

def show_current_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f"Current Date: {current_date}")

3
def create_account():
    customer_id = input("\nEnter the account user id: ")
    acc_number = input("Enter the account number: ")
    holder_name = input("Enter your account holder name: ").strip()  # Remove unwanted spaces

    # ✅ Validate: Only letters and spaces
    if not holder_name.replace(" ", "").isalpha():
        print("Invalid name! Use only letters and spaces.\n")
        return

    # ✅ Convert to Title Case (e.g. brintha balakumar → Brintha Balakumar)
    holder_name = holder_name.title()

    initial_balance = input("Enter the Initial balance : ")

    account_number.append(acc_number)  
    account_details.append({
        "account_number": acc_number,
        "holder_name": holder_name,
        "balance": initial_balance
    })

    with open("accounts.txt", "a") as accounts_file:
        accounts_file.write(f"{customer_id},{acc_number},{holder_name},{initial_balance}\n")

    print("Account created successfully!\n")

4 

def total_customer():
    count = 0
    with open ("customers.txt","r")as customers_file:
        for users in customers_file:
            count += 1
    print("Total users is :", count)
    
total_customer


5
import random
customers = {}

def create_account():
    name = input("Enter your full name: ").strip()

    if re.match("^[A-Za-z\s]+$", name):
        name = name.title()
        account_number = random.randint(1000, 9999)
    
        if 1000 <= account_number <= 9999:
            customer_id = str(len(customers) + 1)
            customers[customer_id] = {'name': name, 'account_number': account_number}
            print(f"Account created successfully! Welcome, {name}. Your account number is {account_number}.")
        else:
            print("Error: Account number generation failed. Please try again.")
    else:
        print("Invalid name. Please use letters and spaces only.")

def main():
    print("Welcome to the Account Creation System!")
    create_account()
    

    print("\nCurrent Customers:")
    for customer_id, details in customers.items():
        print(f"Customer ID: {customer_id}, Name: {details['name']}, Account Number: {details['account_number']}")



6
# def count_transactions(account_number):
#     count = 0
#     try:
#         with open("transaction.txt", "r") as transaction_file:
#             for line in transaction_file:
#                 details = line.strip().split(',')
#                 if account_number == details[1]:
#                     count += 1
#         return count
#     except FileNotFoundError:
#         print("\nTransaction file not found.")
#         return 0
        
#         elif choice == "2":
#             acc_no = input("Enter account number to count transactions: ")
#             total = count_transactions(acc_no)
#             print(f"\nTotal number of transactions for account {acc_no}: {total}")
7
def create_account():
    while True:
        username = input("Enter a username: ")
        if username in users:
            print("Username already taken. Try another.")
        else:
            users.append(username)
            print("Account created successfully!")
            break

create_account()


transactions = {
    1001: [
        "Deposited $500", "Withdrew $200", "Deposited $300"
    ],
    1002: [
        "Deposited $1000", "Withdrew $500"
    ],
    1003: [] 
}

def transaction_type_summary(account_number):
    if account_number in transactions:
        account_transactions = transactions[account_number]
        
        if len(account_transactions) == 0:
            print(f"Account {account_number} has no transactions.")
            return
        
        deposits = 0
        withdrawals = 0
        
    
        for transaction in account_transactions:
            if transaction.startswith("Deposited"):
                deposits += 1
            elif transaction.startswith("Withdrew"):
                withdrawals += 1
        
        print(f"Account {account_number} - Deposits: {deposits}, Withdrawals: {withdrawals}")
    else:
        print(f"Account {account_number} not found.")


def menu():
    while True:
        print("\nMenu:")
        print("1. Transaction Type Summary")
        print("2. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = int(input("Enter the account number: "))
            transaction_type_summary(account_number)
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")




    
9
transactions = {
    1001: [
        {"timestamp": "2025-05-01 10:00", "description": "Deposited $100"},
        {"timestamp": "2025-05-02 11:00", "description": "Withdrew $50"},
        {"timestamp": "2025-05-03 12:00", "description": "Deposited $200"},
        {"timestamp": "2025-05-04 13:00", "description": "Withdrew $30"},
        {"timestamp": "2025-05-05 14:00", "description": "Deposited $500"},
        {"timestamp": "2025-05-06 15:00", "description": "Withdrew $100"},
    ],
    1002: [
        {"timestamp": "2025-05-01 09:00", "description": "Deposited $300"}
    ],
    1003: [] 
}


def transaction_history(account_number):
    if account_number in transactions:
        account_transactions = transactions[account_number]
        
        if not account_transactions:
            print(f"Account {account_number} has no transactions.")
            return
        

        last_five = account_transactions[-5:]
        
        print(f"\nLast {len(last_five)} transactions for account {account_number}:")
        for txn in last_five:
            print(f"{txn['timestamp']} - {txn['description']}")
    else:
        print("Account not found.")


def menu():
    while True:
        print("\nMenu:")
        print("1. View Last 5 Transactions")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            acc_num = int(input("Enter account number: "))
            transaction_history(acc_num)
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

# menu()


account_number = []
account_details = []

def create_account():
    customer_id = input("\nEnter the account user id: ")
    acc_number = str(random.randint(1000, 9999))  
    holder_name = input("Enter your account holder name: ")
    initial_balance = input("Enter the Initial balance : ")

    account_number.append(acc_number)
    account_details.append({
        "account_number": acc_number,
        "holder_name": holder_name,
        "balance": initial_balance
    })

    with open("accounts.txt", "a") as accounts_file:
        accounts_file.write(f"{customer_id},{acc_number},{holder_name},{initial_balance}\n")

    print("Account created successfully!\n", "customer_id : ", customer_id, "acc_number :", "holder_name :", holder_name,  "initial_balance :", initial_balance  )

