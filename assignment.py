# file = open('user.txt','r')
# file.write(f'{user_id}\t')
# file.write(f'{user}\t')
# file.write(f'{pwd}\t')
# file.write(f'{NIC}\t')
# file.write(f'{Ph.no}\t')
# file.write(F'{Address}\t')
# file.write('\n')
# file.close()
# file.write(f"{user_id}: \n")

print("---WELCOME TO MINI BANKING---")

admin_username = input("Enter your admin username: ")
admin_password = int(input("Enter your admin password: "))
while True:
    correct_user = input("Enter the username: ")
    correct_pwd = int(input("Enter the password: "))
    if correct_user == admin_username and correct_pwd == admin_password:
        print("Login Successful.Welcome admin(Kavish!)")
        break
    else:
        print("Login Unsuccessful.Try Again!")

username = ()
password = ()
CustomerCredential = {}

# CREATE CUSToMER=========================================


def creart_customer():
    user_id = input("Enter the customer's ID: ")
    user = input("Enter Customer's name:")
    pwd = int(input("Enter the password: "))
    file = open("customer.txt", "a")
    file.write(f'{user_id}\t')
    file.write(f'{user}\t')
    file.write(f'{pwd}\t')
    file.write(f'{NIC}\t')
    file.write(f'{Ph.no}\t')
    file.write(F'{Address}\t')
    file.write('\n')
    file.close()

    CustomerCredential[user_id] = {
        "Name": user,
        "Password": pwd
    }
    print("customer Created Succesful")
    print("Welcome", CustomerCredential[user_id]["Name"])

# CREART ACCOUNT===================================


def creart_account():
    customer_id = input("enter the customer ID: ")
    account = input("Enter the account number: ")
    balance = int(input("Enter the initial balance:"))
    user_NIC = int(input("Enter the NIC number: "))
    file = open("account.txt", "a")
    file.write(f'{user_id}\t')
    file.write(f'{user}\t')
    file.write(f'{pwd}\t')
    file.write(f'{NIC}\t')
    file.write(f'{Ph.no}\t')
    file.write(F'{Address}\t')
    file.write('\n')
    file.close()

    if customer_id in CustomerCredential:
        print("Account Number: ", account, "Customer ID: ", customer_id, "Initial balance: ", balance)
    else:
        print("Try Again!")
        exit()

# DEPOSIT===============================================================================================


def Deposit():
    try:
        deposit_amount = int(input("Enter your deposit amount: $"))
        if deposit_amount > 0:
            print("Deposit successful! New Balance: $", {balance + deposit_amount})
        else:
            print("Invalid amount! Deposit must be greater than 0.")

    except ValueError:
        print("You must enter a number only!")

# WITHDRAW===============================================================================================


def withdraw():
    try:
        global balance
        withdrawal_amount = int(input("Enter your withdrawal amount: $"))
        if withdrawal_amount < balance:
            balance = balance - withdrawal_amount
            print("Withdrawal successful! New Balance: $", balance)
        else:
            print("Insufficient Balance! Try again.")
    except ValueError:
        print("You must enter a number only!")

# CHECK BALANCE===========================================================================================


def show_balance():
    if name == user and password == pwd:
        print("Your current account balance is: $", balance)
    else:
        print("Trt Again!")

# TRANSACTION HISTORY=====================================================================================


def transaction_history():
    transaction_history.appened("deposit: ", amount)
    transaction_history.appened("withdraw ", amount)

# DELETE OPTION===========================================================================================


def delete():
    delete_id = int(input("Enter user ID to delete: "))
    if delete_id in users:
        del users[delete_id]
        print(f"User {delete_id} deleted.")
    else:
        print("User ID not found.")

# UPDATE OPTION===========================================================================================


def update():
    new_user = input("Enter the new user id: ")
    new_account = input("Enter the new account number: ")
    balance += deposit_amount
    balance = balance = deposit_amount
    balance -= withdrawal_amount
    balance = balance - withdrawal_amount

# ACCOUNT DETAILS=========================================================================================


# ========================================================================================================

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
    choice = input("Enter your choice(1-7):")

    try:
        if choice == "1":
            creart_customer()
        elif choice == "2":
            creart_account()
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
            pass
        else:
            print("Thank you for your service.Goodbye!")
            break

    except ValueError:
        print("You must only enter the number")

file.write(f'{admin_username}\n')
file.write(f'{admin_password}\n')
content = file.read()
print(content.splitlines())
admin_username = ""
admin_password = 2004
file.close()


print("---WELCOME TO MINI BANKING---")

customer_username = input("Enter your customer username: ")
customer_password = int(input("Enter your customer password: "))

while True:
    correct_user = input("Enter the username: ")
    correct_pwd = int(input("Enter the password: "))
    if correct_user == customer_username and correct_pwd == customer_password:
        print("Login Successful.Welcome admin(name)")
        break
    else:
        print("Login Unsuccessful.Try Again!")


while True:
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")
choice = input("Enter your choice: ")

name = input(("Enter your name: "))
NIC = int(input("Enter your NIC number: "))
age = int(input("Enter your current year age: "))
acc = input("Enter your current address: ")
DOB = int(input("Enter your Date of Birth: "))
gender = input("Enter your Gender: ")
status = input("Enter your current status: ")
