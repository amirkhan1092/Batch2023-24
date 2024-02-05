# Bank Management System 
class BankAccount:
    def __init__(self, account_num, account_holder, balance=0):
        self.account_num = account_num
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f'You Successfully deposit {amount} in account {self.account_num}')
            print(f'the updated balance is {self.balance}')
        else:
            print('Not valid amount')
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'{self.account_holder} successfully withraw amount {amount} ')
            print(f'the updated balance is {self.balance}')
        else:
            print(f'Insufficient amount in account {self.account_num}')

    def checkbalance(self):
        return self.balance
    def account_info(self):
        return f'''Name: {self.account_holder}
Account Number: {self.account_num}
Balance: {self.balance}'''
    


class SavingAccount(BankAccount):
    def __init__(self, account_num, account_holder, balance=0, interest_rate=1.56):
        self.interest_rate = interest_rate
        super().__init__(account_num, account_holder, balance)
    def add_interest(self):
        self.balance += self.balance * self.interest_rate
        
class CheckingAccount(BankAccount):
    def __init__(self, account_num, account_holder, balance=0, overdraft_limit=100):
        self.overdraft_limit = overdraft_limit
        super().__init__(account_num, account_holder, balance)
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f'{self.account_holder} successfully withraw amount {amount} ')
            print(f'the updated balance is {self.balance}')
        else:
            print(f'Insufficient amount in account {self.account_num}')



saving_account1 = SavingAccount(1, 'ravi', 100, 2.4)
checking_account1 = CheckingAccount(2, 'saket', 120, 100)


saving_account1.deposit(100)
print(saving_account1.checkbalance())


