account_details = []
account_number = []

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ CREATE CUSTOMER ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

def create_customer():
    user_id = input("\nEnter your user ID: ")
    username = input("Enter the user name: ")
    password = input("Enter your password: ") 
    nic = input("Enter your NIC number: ")
    address = input("Enter your valuable address: ")
    t_no = input("Enter your Mobile number: ")
    DOB = input("Enter your date of birth(DD/MM/YYYY): ")

    with open("customers.txt", "a") as customer_file:
        customer_file.write(f'{user_id}\t{username}\t{password}\t{nic}\t{address}\t{t_no}\t{DOB}\n')

    print("\nCustomer created successfully. Now you're a customer of the Mini Banking!")
    print(f"Hii {username}, Welcome to the Mini Banking System!\n")

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ CREATE ACCOUNT ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]    

def create_account():
    customer_id = input("\nEnter the account user id: ")
    acc_number = input("Enter the account number: ")
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

    print("Account created successfully!\n")

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ DEPOSIT OPTION ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

def deposit_amount():
    try:
        acc_no = input("\nEnter your account number: ")  
        amount = float(input("Enter your deposit amount: RS. "))
        updated = False

        with open("accounts.txt", "r") as file:
            lines = file.readlines()

        with open("accounts.txt", "w") as file:
            for line in lines:
                data = line.strip().split(',')
                if data[1] == acc_no:
                    balance = float(data[3])
                    new_balance = balance + amount
                    file.write(f"{data[0]},{data[1]},{data[2]},{new_balance}\n")
                    updated = True
                    from datetime import datetime
                    now = datetime.now().strftime("%d/%m/%Y %H:%M")
                    with open("transaction.txt", "a") as tf:
                        tf.write(f"{now},{acc_no},Deposit,{amount},{new_balance}\n")
                else:
                    file.write(line)

        if updated:
            print(f"\nDeposit successful! New balance: RS. {new_balance}")
        else:
            print("\nAccount not found!")

    except ValueError:
        print("Invalid amount. Enter numbers only.\n")

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ WITHDRAW OPTION ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

def withdraw_amount():
    try:
        acc_no = input("\nEnter your account number: ")  
        amount = float(input("Enter your withdraw amount: RS. "))
        updated = False

        with open("accounts.txt", "r") as file:
            lines = file.readlines()

        with open("accounts.txt", "w") as file:
            for line in lines:
                data = line.strip().split(',')
                if data[1] == acc_no:
                    balance = float(data[3])
                    if amount > balance:
                        print("Insufficient balance!")
                        file.write(line)
                    else:
                        new_balance = balance - amount
                        file.write(f"{data[0]},{data[1]},{data[2]},{new_balance}\n")
                        updated = True
                        from datetime import datetime
                        now = datetime.now().strftime("%d/%m/%Y %H:%M")
                        with open("transaction.txt", "a") as tf:
                            tf.write(f"{now},{acc_no},Withdraw,{amount},{new_balance}\n")
                else:
                    file.write(line)

        if updated:
            print(f"\nWithdraw successful! New balance: RS. {new_balance}")
        else:
            print("\nAccount not found!")

    except ValueError:
        print("Invalid amount. Enter numbers only.\n")

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ CHECK BALANCE ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

def show_balance():
    acc_no = input("Enter your account number to check balance: ")
    found = False
    with open("accounts.txt", "r") as file:
        for line in file:
            data = line.strip().split(',')
            if data[1] == acc_no:
                print(f"\nYour current balance is: RS. {data[3]}")
                found = True
                break
    if not found:
        print("Account not found.")
        
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ TRANSACTION HISTORY ]]][[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]    

def transaction_history():
    acc_no = input("\nEnter your account number to view transaction history: ")
    found = False
    try:
        with open("transaction.txt", "r") as transaction_file:
            print("--- Transaction History ---\n")
            for line in transaction_file:
                details = line.strip().split(',')
                if acc_no == details[1]:
                    print(f"Date & Time: {details[0]}")
                    print(f"Transaction: {details[2]}")
                    print(f"Amount: Rs {details[3]}")
                    print(f"New Balance: Rs {details[4]}")
                    print("-" * 30)
                    found = True
        if not found:
            print("\nNo transactions found for this account.")

    except FileNotFoundError:
        print("\nTransaction file not found.")

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ ADMIN MENU ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

def admin_menu():
    while True:
        print("\n-----WELCOME TO MINI BANKING----")
        print("1. Create Customer ")
        print("2. Create Account")
        print("3. View Transaction History")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            create_account()
        elif choice == "3":
            transaction_history()
        elif choice == "4":
            print("\nThank you for your service. Goodbye!")
            exit()
        else:
            print("\nInvalid Input. Try again!")

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ CUSTOMER MENU ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

def customer_menu():
    while True:
        print("\n-----WELCOME TO MINI BANKING----\n")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")
        
        choice = input("\nEnter your choice(1-5): ")

        if choice == "1":
            deposit_amount()
        elif choice == "2":
            withdraw_amount()
        elif choice == "3":
            show_balance()
        elif choice == "4":
            transaction_history()
        elif choice == "5":
            print("\nThank you for your service. Goodbye!")
            exit()
        else:
            print("\nInvalid choice. Please try again.")

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ ADMIN LOGIN ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]            

def admin_login():
    while True:
        admin_name = "kavish"
        admin_password = "kavish2004"
        admin_id = "A01"
        print("\n1. Admin Login")
        print("2. Load Admin from File")
        print("3. Back")
        choice = input("Enter the choice(1-3): ")

        if choice == "1": 
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            user_id = input("Enter the user ID:")

            if username == admin_name and password == admin_password and user_id == admin_id:
                print("\nLogin Successful!!")
                print(f"Hi! {username}, Welcome to the system Admin")
                admin_menu()
        elif choice == "2":
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            user_id = input("Enter the user ID : ")

            with open("users.txt", "r") as users_file:  
                for user in users_file:
                    users_login_details = user.strip().split()
                    if username in users_login_details and password in users_login_details and user_id in users_login_details:
                        print("Login Successful!")
                        admin_menu()
        elif choice == "3":
            break
        else:
            print("\nAdmin Details Not correct. Try Again!")

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ CUSTOMET LOGIN ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]            

def customer_login():
    while True:
        customer_name = input("Enter the customer name: ")
        customer_password = input("Enter the customer password: ")
        customer_id = input("Enter the customer ID : ")

        with open("customers.txt", "r") as customers_file:  
            for customer in customers_file:
                customer_login_details = customer.strip().split()
                if customer_name in customer_login_details and customer_password in customer_login_details and customer_id in customer_login_details:
                    print("Login Successful!!")
                    print(f"Hi! {customer_name}, Welcome to the system customer!")   
                    customer_menu()
                    return
        print("\nCustomer Details Not correct. Try Again!")
        break

# MAIN MENU
while True:
    print("\n================ MINI BANKING SYSTEM ================\n")
    print("1. Admin")
    print("2. Customer\n")
    role = input("Enter the Role (1 or 2): ") 
    
    if role == "1":
        admin_login()
    elif role == "2":
        customer_login()
    else:
        print("Login Unsuccessful. Try Again!")
        print("Please choose 1 OR 2")

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
