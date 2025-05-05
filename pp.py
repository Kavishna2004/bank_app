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


# if __name__ == "__main__":
#     main()
    
#     balance = 100000  # defined globally
# transaction_history = []

# def withdraw():
#     global balance
#     try:
#         withdrawal_amount = int(input("Enter your withdrawal amount: $"))
#         if withdrawal_amount > 0 and balance >= withdrawal_amount:
#             balance -= withdrawal_amount
#             transaction_history.append(f"Withdrew: ${withdrawal_amount}")
#             print(f"Withdrawal successful! New Balance: ${balance:.2f}")
#         else:
#             print("Insufficient balance or invalid amount!")
#     except ValueError:
#         print("You must enter a number only!")

balance = 100000
def deposit():
    try:
        deposit_amount = int(input("Enter your deposit amount: $"))
        if deposit_amount > 0:
            print(f"Deposit successful! New Balance: $ {balance + deposit_amount:.2f}")
        else:
            print("Invalid amount! Deposit must be greater than 0.")

    except ValueError:
        print("You must enter a number only!")
        
deposit()