class User:

    def __init__(self, name):
        self.name = name
        self.checking = BankAccount("Checking ")
        self.savings = BankAccount("Savings ", .001)

    def make_deposit(self, account, amount):
        account.deposit(amount)
        return self

    def make_withdrawal(self, account, amount):
        account.withdrawal(amount)
        return self

    def display_user_balances(self):
        print("User: " + self.name)
        self.checking.display_account_info()
        self.savings.display_account_info()
        return self


class BankAccount:

    account_population = []

    def __init__(self, type, int_rate = .002, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.account_population.append(self)
        self.type = type

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
        print(self.type + "Balance: " + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    def transfer_money(self, recipient_account, amount):
        if BankAccount.can_withdrawal(self.balance, amount):
            self.withdrawal(amount)
            recipient_account.deposit(amount)
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
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

chris = User("Chris")
chris.checking.deposit(300)
chris.savings.deposit(200)
chris.display_user_balances()

terran = User("Terran")
terran.checking.deposit(1000).transfer_money(chris.checking, 500)
terran.display_user_balances()
chris.display_user_balances()

chris.make_deposit(chris.checking, 500)
chris.make_withdrawal(chris.savings, 100).display_user_balances()