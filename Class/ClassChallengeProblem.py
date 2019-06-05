"""
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""

class Account():

    def __init__(self,owner_name,balance):
        self.owner=owner_name
        self.balance =balance

    def __str__(self):
        return 'Account owner:'+self.owner+'\n'+'Account balance:'+str(self.balance)

    def deposit(self,amount):
        self.balance=self.balance+amount
        print('Deposit Accepted')

    def withdrawal(self,amount):
        if self.balance >= amount:
            self.balance=self.balance-amount
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable')

acct1=Account('Jose',100)
print(acct1)
print('Owner Name',acct1.owner)
print('Balance',acct1.balance)
acct1.deposit(50)
print('After Deposit')
print(acct1)
acct1.withdrawal(75)
print('After WithDrawal')
print(acct1)
acct1.withdrawal(500)

