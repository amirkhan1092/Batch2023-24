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


# Example usage:
savings_account = SavingsAccount(account_number=1, owner="Alice", balance=1000)
checking_account = CheckingAccount(account_number=2, owner="Bob", balance=500)

print("Savings Account Details:")
print(savings_account.display_balance())
print(savings_account.monthly_statement())
print(savings_account.apply_interest())
print(savings_account.display_balance())

print("\nChecking Account Details:")
print(checking_account.display_balance())
print(checking_account.withdraw(200))
print(checking_account.withdraw(1000))  # Attempt to exceed overdraft limit
print(checking_account.display_balance())
