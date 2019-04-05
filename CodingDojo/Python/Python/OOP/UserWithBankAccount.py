class BankAccount:
    def __init__(self, name, balance = 0, int_rate = 0.3): 
        self.name = name
        self.int_rate = int_rate
        self.balance = balance 

    def deposit(self, amount):
        print("{} Made a deposit of ${}".format(self.name, amount))
        self.balance += amount
        return self

    def withdraw(self, amount):
        print("{} Made a withdrawl of ${}".format(self.name, amount))
        self.balance -= amount
        return self

    def display_account_info(self):
        print("{} balance is: ${}".format(self.name, self.balance))
        return self

    def yield_interest(self):
        interest = self.balance * self.int_rate
        print("{} is the interest rate and {} is the interest on your account".format(self.int_rate, interest))
        return self

bob = BankAccount("Bob")
joe = BankAccount('Joe')

bob.deposit(100).deposit(50).deposit(50).withdraw(100).yield_interest().display_account_info()

joe.deposit(1000).deposit(200).withdraw(100).withdraw(50).withdraw(25).withdraw(25).yield_interest().display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount("Account1",int_rate=0.02, balance=0)	# added this line


    def make_deposit(self, amount):
        print("{} Made a deposit of ${}".format(self.name, amount))
        self.account += amount
        return self

    def make_withdrawl(self, amount):
        print("{} Made a withdrawl of ${}".format(self.name, amount))
        self.account -= amount
        return self

    def transfer_money(self, other_user, amount):
        print("{} transfered ${} to {}".format(self.name, amount, other_user.name))
        self.account -= amount
        other_user.account_balance += amount
        return self

    def display_user_balance(self):
        print("{} balance is: ${}".format(self.name, self.account))
        return self

michael = User("Michael Levy", "mlevy@gmail.com")
kevin = User("Kevin Spacey", "kspacey@yahoo.com")
jeff = User("Jeff McJefferson", "jeffy123@hotmail.com")

michael.make_deposit(500).make_deposit(25).make_deposit(25).make_withdrawl(50).display_user_balance()

kevin.make_deposit(25).make_deposit(25).make_withdrawl(30).make_withdrawl(20).display_user_balance()

jeff.make_deposit(75).make_withdrawl(25).make_withdrawl(25).make_withdrawl(25).display_user_balance()


michael.transfer_money(jeff, 100)
jeff.display_user_balance()
michael.display_user_balance()


