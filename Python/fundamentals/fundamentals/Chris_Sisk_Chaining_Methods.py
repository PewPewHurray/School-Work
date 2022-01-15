class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self

    def transfer_money(self, recipient, amount):
        self.account_balance -= amount
        recipient.account_balance += amount
        return self

chris = User("Chris")
terran = User("Terran")
bob = User("Bob")

chris.make_deposit(500).make_deposit(700).make_deposit(400).make_withdrawal(300).display_user_balance()

terran.make_deposit(1300).make_deposit(400).make_withdrawal(300).make_withdrawal(200).display_user_balance()

bob.make_deposit(3500).make_withdrawal(800).make_withdrawal(600).make_withdrawal(100).display_user_balance()

chris.transfer_money(bob, 700).display_user_balance()
bob.display_user_balance()