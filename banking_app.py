account_details = []
account_number = []

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ CREATE CUSTOMER ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

def create_customer():
    user_id = input("\nEnter your user ID: ")
    username = input("Enter the user name: ")
    password = input("Enter your password: ") 
    nic = int(input("Enter your NIC number: "))
    address = input("Enter your valuable address: ")
    t_no = int(input("Enter your Mobile number: "))
    DOB = input("Enter your date of birth(DD/MM/YYYY)\n: ")

    with open("customers.txt", "a") as customer_file:
        customer_file.write(f'{user_id}\t{username}\t{password}\t{nic}\t{address}\t{t_no}\t{DOB}\n')

    print("\n Customer created successfully. Now you're a customer of the Mini Banking!")
    print(f"Hii {username}, Welcome to the Mini Banking System!\n")
    
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ CREATE ACCOUNT ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

def create_account():
    customer_id = input("\nEnter the account user id: ")
    acc_number = input("Enter the account number: ")
    holder_name = input("Enter your account holder name: ")
    initial_balance = int(input("Enter the Initial balance : "))

    account_number.append(acc_number)  
    account_details.append({
        "account_number": acc_number,
        "holder_name": holder_name,
        "balance": initial_balance
    })
             
    with open("accounts.txt", "a") as accounts_file:
        accounts_file.write(f"{customer_id},{acc_number},{holder_name},{initial_balance}\n")

    print("Account created successfully!\n")
    
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ DEPOSIT OPTION ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]   

def deposit_amount():
    try:
        acc_no = input("\n Enter your account number: ")  
        with open ("accounts.txt","r") as accounts_file:
            for lines in accounts_file:
                line = lines.strip().split(',')
                
                if acc_no == line[1]:
                    amount = float(input("Enter your deposit amount: RS. "))
                    new_balance = float(line[3]) + amount 
                    
                    with open ("accounts_details.txt",'r') as accounts_file:
                        line = lines.strip().split(',')
                        
                    with open ("accounts.txt",'w') as accounts_file:
                        line = lines.strip().split(',')
                        
                        if lines[0] == acc_no:
                            lines[2] == new_balance
                            accounts_file(f"{lines[0]},{lines[1]},{lines[2]},{lines[3]}/n")
                            
                    from datetime import datetime
                    current_date_time = datetime.now()
                    new_date_time == current_date_time.strftime("%d/%m/%y %H:%M")    
                    
                    with open ("transaction.txt","r")as tansaction_file:
                        tansaction_file.write(f"{new_date_time},{acc_no},Deposit'{amount},{new_balance}n")
                        print(f"\nDeposit Successfull.\n Deposit amount : Rs {amount}\n new_balance: RS {new_balance}")
                        found = True
                                    
            if not found:
                print("\nAccount not found!") 
            
    except ValueError:
        print("You must enter a number only!\n")  
                
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ WITHRRAWEL OPTION ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]      
          
def withdraw_amount():
    try:
        acc_no = input("\n Enter your account number: ")  
        
        with open ("accounts.txt","r") as accounts_file:
            for lines in accounts_file:
                line = lines.strip().split(',')
                
                if acc_no == line[1]:
                    amount = float(input("Enter your deposit amount: RS. \n"))
                    new_balance = float(line[3]) + amount 
                    
                    with open ("accounts_details.txt",'r') as accounts_file:
                        line = lines.strip().split(',')
                        
                    with open ("accounts.txt",'w') as accounts_file:
                        line = lines.strip().split(',')
                        
                    if lines[0] == acc_no:
                            lines[2] == new_balance
                            accounts_file(f"{lines[0]},{lines[1]},{lines[2]},{lines[3]}/n")
                            
                    from datetime import datetime
                    current_date_time = datetime.now()
                    new_date_time == current_date_time.strftime("%d/%m/%y %H:%M")
                        
                   
                    with open ("transaction.txt","r")as tansaction_file:
                        tansaction_file.write(f"{new_date_time},{acc_no},withdraw'{amount},{new_balance}n")
                        print(f"\nWithdraw Successfull.\n Withdraw amount : Rs {amount}\n new_balance: RS {new_balance}")
                        found = True
                                    
            if not found:
                print("\n Account not found!") 
            
    except ValueError:
        print("You must enter a number only!\n")  
                        
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ CHECK BALANCE [[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]          

def show_balance():
    print(f"\n Your current account balance is: RS.{balance:.2f}")  
    
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ TRANSACTION HISTORY [[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
   
def transaction_history():
    acc_no = input("\n Enter your account number to view transaction history: ")

    try:
        with open("transaction.txt", "r") as transaction_file:
            found = False
            print("--- Transaction History ---\n")
            for line in transaction_file:
                details = line.strip().split(',')

                if acc_no == details[1]:
                    print(f"\n Date & Time: {details[0]}")
                    print(f"Transaction: {details[2]}")
                    print(f"Amount: Rs {details[3]}")
                    print(f"New Balance: Rs {details[4]}")
                    print("-" * 30)
                    found = True

            if not found:
                print("\n No transactions found for this account.")

    except ValueError:
        print("\n Transaction file not found.")

         
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ ADMIN MENU ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

def admin_menu():
    while True:
        print("\n-----WELCOME TO MINI BANKING----")
        print("1. Create Customer ")
        print("2. Create Account")
        print("3. View Transaction History")
        print("4. Exit")
        
        choice = input("\n Enter your choice (1-4) ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            create_account()
        elif choice == "3":
            transaction_history()
        elif choice == "4":
            print("\n Thank you for your service. Goodbye!")
            exit()
        else:
            print("\n Invalid Input. Try again!")
            
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[Customer Menu ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]         
                                 
def customer_menu():
    while True:
        print("\n-----WELCOME TO MINI BANKING----\n")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")
        
        choice = input("\n Enter your choice(1-5): ")

        if choice == "1":
            deposit_amount()
        elif choice == "2":
            withdraw_amount()
        elif choice == "3":
            show_balance()
        elif choice == "4":
            transaction_history()
        elif choice == "5":
            print("\n Thank you for your service. Goodbye!")
            break
        else:
            print("\n Invalid choice. Please try again.")
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ Admin Login ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]         
                                 
def admin_login():
    while True:
        admin_name = "kavish"
        admin_password = "kavish2004"
        admin_id = "A01"
        choice = input("Enter the choice(1-3):")

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
                        admin_menu()
                        
        else:
            print("\n Admin Details Not correct. Try Again!")
            break
        
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ Customer Login ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]         
                                 
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
            
            print("\n Customer Details Not correct. Try Again!")
            break

while True:
    print("1. Admin")
    print("2. Customer \n ")
    role = input("Enter the Role (1 or 2): ")
    if role == "1":
        admin_login()
    elif role == "2":
        customer_login()
    else:
        print("Login Unsuccessful. Try Again!")
        print("Please choose 1 OR 2")
        break

#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]