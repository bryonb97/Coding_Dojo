class BankAccount:
    def __init__(self, int_rate = 12.68, balance): 
        self.int_rate = int_rate
        self.balance = balance 

    def deposit(self, amount):
        print("{} Made a deposit of ${}".format(self.name, amount))
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        print("{} Made a withdrawl of ${}".format(self.name, amount))
        self.balance -= amount
        return self.balance

    def display_account_info(self):
        print("{} balance is: ${}".format(self.name, self.balance))
        return self.balance

    def yield_interest(self):
        self.int_rate = int_rate
        interest = balance * int_rate
        print("{} is the interest rate and {} is the interest on your account".format(int_rate, interest))


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self.account = BankAccount(int_rate=0.02, balance=0)	# added this line


    def make_deposit(self, amount):
        print("{} Made a deposit of ${}".format(self.name, amount))
        self.account_balance += amount
        return self.account_balance

    def make_withdrawl(self, amount):
        print("{} Made a withdrawl of ${}".format(self.name, amount))
        self.account_balance -= amount
        return self.account_balance

    def transfer_money(self, other_user, amount):
        print("{} transfered ${} to {}".format(self.name, amount, other_user.name))
        self.account_balance -= amount
        other_user.account_balance += amount

    def display_user_balance(self):
        print("{} balance is: ${}".format(self.name, self.account_balance))
        return self.account_balance

michael = User("Michael Levy", "mlevy@gmail.com")
kevin = User("Kevin Spacey", "kspacey@yahoo.com")
jeff = User("Jeff McJefferson", "jeffy123@hotmail.com")

michael.make_deposit(500).make_deposit(25).make_deposit(25).make_withdrawl(50).display_user_balance()

kevin.make_deposit(25).make_deposit(25).make_withdrawl(30).make_withdrawl(20).display_user_balance()

jeff.make_deposit(75).make_withdrawl(25).make_withdrawl(25).make_withdrawl(25).display_user_balance()


michael.transfer_money(jeff, 100)
jeff.display_user_balance()
michael.display_user_balance()

