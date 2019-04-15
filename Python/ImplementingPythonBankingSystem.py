"""
Give a prompt to the user asking if they wish to create a new savings Account or to access an existing one

If the user would like to create a new account, accept their name and initial deposit, create a random number and make it as the account
number of their savings account

if they are accessing an existing account, accept their name and account number to validate the user, and give them options to withdraw, deposit
or display the available balance
"""
import random

class Customer:
    def user_requirment(self):
        print('Enter the user name')
        name = input()
        account_details = Account_Details(name)
        while True:
            print('1. Create a new Savings Account \n2. Access an existing One  \n3. Quit')
            data=int(input())
            if (data == 1):
                print('Enter the initial Deposit')
                user_deposit = int(input())
                account_details.createNewAccount(user_deposit)
            elif(data == 2):
                print('Enter the account number')
                account_number = int(input())
                print('Enter the name for validation purpose')
                customer_name  = input()
                print('1. To Withdraw the Amount, \n2. To Deposit the Amount \n3. To print Details')
                option= int(input())
                if (option == 1):
                    print('Enter the Amount to With Draw')
                    withdraw_amount = int(input())
                    available_balance=account_details.deposit
                    if(available_balance > withdraw_amount):
                        account_details.withdraw_amount(customer_name,account_number,withdraw_amount)
                    else:
                        print('Available funds is insufficient')
                elif (option ==2):
                    print('Enter the Amount to Deposit')
                    deposit_amount =int(input())
                    if (deposit_amount <0):
                        print('Cannot do the deposit as the amount provided is negative')
                    else:
                        account_details.additional_amount_deposit(customer_name,account_number,deposit_amount)
                elif (option ==3):
                    account_details.print_details(customer_name)
            elif (data == 3):
                 quit()



class Account_Details:
    def __init__(self, name):
        self.name = name
        self.deposit = 0
        self.AccountNumber = 0
    def createNewAccount(self,initialdeposit):
        self.deposit+=initialdeposit
        randomnumber = random.randint(10000,99999)
        self.AccountNumber = randomnumber
        print('Account Number is :',self.AccountNumber)
    def print_details(self,customer_name):
        if(self.name == customer_name):
            print('Account Number :',self.AccountNumber)
            print('Deposit :',self.deposit)
    def withdraw_amount(self,customer_name, useraccountnumber, withdrawamount):
        if( self.name == customer_name) and (self.AccountNumber == useraccountnumber):
            self.deposit-=withdrawamount
    def additional_amount_deposit(self,customer_name, useraccountnumber, depositamount):
        if( self.name == customer_name) and (self.AccountNumber == useraccountnumber):
            self.deposit+=depositamount
1
customer =Customer()
customer.user_requirment()

