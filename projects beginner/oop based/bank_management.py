# Bank Management System 

class Bank:
    def __init__(self,name,initialAmount = 0) -> None:
        self.bankBalance = initialAmount
        self.name = name
        print('Account Successfully Opened')
    def deposit(self,depositAmount):
        if depositAmount <= 0:
            print("Sorry, Invalid Amount! ")
        else:
            self.bankBalance += depositAmount
            print(f"Rs. {depositAmount} has been deposited.\nCurrent Balance: Rs. {self.bankBalance}")
    def withdraw(self,withdrawAmount):
        if withdrawAmount > self.bankBalance:
            print("Sorry, the withdraw amount is too large.")
        else:
            self.bankBalance -= withdrawAmount
            print(f"Amount Rs.{withdrawAmount} has been withdrawn.\nCurrent Amount: Rs.{self.bankBalance}")
    def checkBalance(self):
        print(f'''
            Name: {self.name}
            Current Balance: {self.bankBalance}''')

# main code 
account_holder = input('Enter the Acount Holder Name ')
initial_amount = eval(input('Enter the initial Amount '))
print('Welcome to ABC bank')
account1 = Bank(account_holder, initial_amount)
while 1:
    print('''Menu:

    1. Deposit
    2. Withdraw
    3. Balance Check
    4. Exit
        
        ''')
    choice = int(input('Enter the choice 1/2/3/4 '))
    if choice == 1:
        pass
    elif choice == 4:

        break

print()