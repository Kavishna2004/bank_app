username = ()
password = ()
CustomerCredential = {}
account_details = []
address = ()
balance = 100000
transaction_history = []

print("---WELCOME TO MINI BANKING---")

# def create_customer():
#     user_id = int(input("Enter the customer's ID: "))
#     user = input("Enter Customer's name:")
#     pwd = int(input("Enter the password: "))
#     NIC = int(input("Enter your NIC number: "))
#     BOD = int(input("Enter your date of birth: "))
#     ph_no = int(input("Enter your valuable current address: "))
#     address = input("Enter your current address: ")
    
#     CustomerCredential[user_id] = {
#         "customer_id": "user_id",
#         "Name": user,
#         "Password": pwd,
#         "NIC number": NIC,
#         "Date of birth" : BOD,
#         "Phone number":ph_no,
#         "Address": address 
#         }
#     print("customer Created Succesful")
#     print("Welcome", CustomerCredential[user_id]["Name"])
    
#--------------------------CREATE ACCOUNT----------------------------------------

def create_account():
    customer_id = input("enter the customer ID: ")
    user = input("Enter your username: ")
    pwd = int(input("Enter the password: "))
    NIC = int(input("Enter the NIC number: "))
    account = input("Enter the account number: ")
    balance = int(input("Enter the initial balance:"))
    
    file = open("account.txt", "a")
    file.write(f'{customer_id}\t')
    file.write(f'{user}\t')
    file.write(f'{pwd}\t')
    file.write(f'{NIC}\t')
    file.write(f'{account}\t')
    file.write(f'{balance}\t')
    file.write('\n')
    file.close()
            
    if customer_id in CustomerCredential:
        print("Account Number: ", account, "Customer ID: ", customer_id, "Initial balance: ", balance)
    else:
        print("Try Again!")
        exit()

#------------------------------------------------DEPOSIT OPTION-------------------------------------------

def deposit():
    try:
        deposit_amount = int(input("Enter your deposit amount: $"))
        if deposit_amount > 0:
            print(f"Deposit successful! New Balance: $ {balance + deposit_amount:.2f}")
        else:
            print("Invalid amount! Deposit must be greater than 0.")

    except ValueError:
        print("You must enter a number only!")

#---------------------------------------------WITHDRAW OPTION----------------------------------------------

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
        
# # #-------------------------------------------------CHECK BALANCE--------------------------------------------

# def show_balance():
#     name = input("Enter your username: ")
#     password = int(input("Enter your password: "))
    
#     if name == username and password == pwd:
#         print("Your current account balance is: $", Balance)
#     else:
#         print("Trt Again!")
        
# show_balance()
# #---------------------------------------------Transaction History-------------------------------------------

# def transaction_history():
#     transaction_history.append("deposit: ", amount)
#     transaction_history.append("withdraw ", amount)

# #-------------------------------------------------DELETE OPTION--------------------------------------------

# def delete():
#     delete_id = int(input("Enter user ID to delete: "))
#     if delete_id in users:
#         del users[delete_id]
#         print(f"User {delete_id} deleted.")
#     else:
#         print("User ID not found.")

# #--------------------------------------------UPDATE OPTION----------------------------------------
#     new_user = input("Enter the new user id: ")
#     new_account = input("Enter the new account number: ")
#     balance += deposit_amount
#     balance = balance = deposit_amount
#     balance -= withdrawal_amount
#     balance = balance - withdrawal_amount
    
#=========================================================================================================
while True:
    try:
        login = input("Enter the Role(admin or customer):")
        if login == "admin":
            admin_user_ID = int(input("Enter your user ID: "))
            user_name = input("Enter your username: ")
            pwd = int(input("Enter your password: "))
            print("Login Successful.Welcome Admin", user_name)  
            
            file = open("Credential.txt", "a")
            file.write(f'{admin_user_ID}\t')
            file.write(f'{user_name}\t')
            file.write(f'{pwd}\t')
            file.write('\n')
            file.close()
            
            while True:
                print("1. Create Customer")
                print("2. Create Account")
                print("3. Deposit Money")
                print("4. Withdraw Money")
                print("5. Check Balance")
                print("6. Transaction History ")
                print("7 .Delete option")
                print("8 .Update option")
                print("9. Acoount Details")
                print("10. Exit")
                choice = input("Enter your choice(1-10):")

    
                if choice == "1":
                    create_customer()
                elif choice == "2":
                    create_account()
                elif choice == "3":
                    Deposit()
                elif choice == "4":
                    withdraw()
                elif choice == "5":
                    show_balance()
                elif choice == "6":
                    transaction_history()
                elif choice == "7":
                    delete()
                elif choice == "8":
                    update()
                elif choice == "9":
                    acc = input("Enter the account number: ")
                    account_details[account_number] = {'Holder Name': Name , 'Current Balance': balance ,'Deposit': amount ,'Withdraw': amount}
                elif choice == "10":
                    print("Thank you for your service.Goodbye!")
                    break
                else:
                    print("Invalid Input.Try again!")
                
        elif login == "customer":
            customer_user_ID = int(input("Enter your user ID: "))
            user_name = input("Enter your username: ")
            pwd = int(input("Enter your password: "))
            print("Login Successful.Welcome Customer ", user_name)  
            
            while True:
                print("-----MENU----")
                print("1. Deposit Money")
                print("2. Withdraw Money")
                print("3. Check Balance")
                print("4. Transaction History")
                print("5. Exit")
                choice = input("Enter your choice: ")
                
                file = open("Credential.txt", "a")
                file.write(f'{deposit}\t')
                file.write('\n')
                file.close()
                
                if choice == "1":
                    deposit()
                elif choice == "2":
                    withdraw_amount()
                elif choice == "3":
                    print("Your current balance is:$")
                elif choice == "4":
                    transaction_history()
                elif choice == "5":
                    print("Thank you for your service.Goodbye!")
                    break
                    
        else:
            print("Login Unsuccessful.Try Again!")
            
    except ValueError:
        print("You must only enter the number")
        
