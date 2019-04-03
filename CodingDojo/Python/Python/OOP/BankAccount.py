class BankAccount:
    def __init__(self, int_rate = 12.68, balance): 
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
        self.int_rate = int_rate
        interest = balance * int_rate
        print("{} is the interest rate and {} is the interest on your account".format(int_rate, interest))
        return self

bob = BankAccount(12.68, 100)
joe = BankAccount(200)

bob.deposit(100).deposit(50).deposit(50).withdraw(100).yield_interest().display_account_info()

joe.deposit(1000).deposit(200).withdraw(100).withdraw(50).withdraw(25).withdraw(25).yield_interest().display_account_info()
