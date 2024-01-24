# Bank Management System 

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            return "Amount credited successfully"
        else:
            return('Invalid Amount')
    def withdraw(self,amount):
        if amount>self.balance:
            return "Insufficient balance"
        elif amount<=0:
            return "Invalid amount"
        else:
            self.balance-=amount
            return f"Rs.{amount} debited from your account"
    def checkBalance(self):
        return f"Total Balance: {self.balance}"
    def getAccInfo(self):
        return f'''Account number: {self.account_number}
Account Holder: {self.account_holder}
Total Balance: {self.balance}'''



# main code 
if __name__ == '__main__':
    name = input('Enter the name ')
    account_number = 1002382028224
    ac = BankAccount(account_number, name)
    while 1:
        print('''Menu
              
1. Deposit
2. Withdraw
3. Check balance
4. account info
5. Exit
              ''')
        choice = int(input('Enter the choice 1/2/3/4/5 '))
        if choice == 5:
            break
        elif choice==4:
            print(ac.getAccInfo())
        elif choice==3:
            print(ac.checkBalance())
        elif choice==2:
            amt=int(input("Enter amount: "))
            print(ac.withdraw(amt))
        elif choice==1:
            amt=int(input("Enter amount: "))
            print(ac.deposit(amt))
        else:
            print("Invalid input. Choose from the options below: ")
    
