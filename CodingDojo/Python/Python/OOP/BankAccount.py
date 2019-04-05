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
