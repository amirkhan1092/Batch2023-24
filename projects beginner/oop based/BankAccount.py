class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def display_balance(self):
        return f"Account Number: {self.account_number}\nOwner: {self.owner}\nBalance: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit of ${amount} successful. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal of ${amount} successful. New balance: ${self.balance}"
        else:
            return "Insufficient funds"

    def monthly_statement(self):
        return "Monthly statement: No interest or fees applied."


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, interest_rate=0.02):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_earned = self.balance * self.interest_rate
        self.balance += interest_earned
        return f"Interest of ${interest_earned} applied. New balance: ${self.balance}"

    def monthly_statement(self):
        return super().monthly_statement() + f"\nInterest Rate: {self.interest_rate * 100}%"


class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, overdraft_limit=500):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return f"Withdrawal of ${amount} successful. New balance: ${self.balance}"
        else:
            return "Exceeded overdraft limit"

accounts = []
print('welcome to ABC Bank')
while 1:
    print('Menu\n1> Saving Account\n2> checking account\n3> Display All Account\n4> Exit')
    ch = int(input('enter the choice 1/2/3/4 '))
    if ch == 4:
        break
    elif ch == 1:
        print('Enter Saving Account details ')
        name = input('Enter account holder name ')
        balance = int(input('Enter initial balance '))
        mobile = input('Enter the mobile number ')
        account = SavingsAccount(mobile, name, balance)
        accounts.append(account)
        print('Saving account succesfully created ')
        while 1:
            print('1> Deposit\n2> Withdraw\n3> Check Balance\n4> display Account\n5> Exit ')
            ch = int(input('enter the choice 1/2/3/4/5 '))
            if ch == 1:
                amount = int(input('Enter the ammount '))
                print(account.deposit(amount))
            elif ch == 2:
                amount = int(input('Enter the ammount '))
                print(account.withdraw(amount))
            elif ch == 3:
                print(account.display_balance())
            elif ch == 5:
                break
            

                
            
