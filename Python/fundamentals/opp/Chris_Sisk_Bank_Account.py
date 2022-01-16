class BankAccount:

    account_population = []

    def __init__(self, int_rate = .001, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.account_population.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if BankAccount.can_withdrawal(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print("Balance: " + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @staticmethod
    def can_withdrawal(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

    @classmethod
    def all_balances(cls):
        for account in cls.account_population:
            print("Balance: " + str(account.balance))

first = BankAccount()
second = BankAccount(.002, 500)

first.deposit(500).deposit(400).deposit(200).withdrawal(300).display_account_info()

second.deposit(800).deposit(400).withdrawal(100).withdrawal(200).withdrawal(300).withdrawal(400).yield_interest().display_account_info()

second.withdrawal(2000).display_account_info()

BankAccount.all_balances()