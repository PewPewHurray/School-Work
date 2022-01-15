class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.name, self.account_balance)

    def transfer_money(self, recipient, amount):
        self.account_balance -= amount
        recipient.account_balance += amount

chris = User("Chris")
terran = User("Terran")
bob = User("Bob")

chris.make_deposit(500)
chris.make_deposit(700)
chris.make_deposit(400)
chris.make_withdrawal(300)
chris.display_user_balance()

terran.make_deposit(1300)
terran.make_deposit(400)
terran.make_withdrawal(300)
terran.make_withdrawal(200)
terran.display_user_balance()

bob.make_deposit(3500)
bob.make_withdrawal(800)
bob.make_withdrawal(600)
bob.make_withdrawal(100)
bob.display_user_balance()

chris.transfer_money(bob, 700)
bob.display_user_balance()
chris.display_user_balance()