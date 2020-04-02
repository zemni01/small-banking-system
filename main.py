"""

small banking system 
author : Houssem Zemni 
year : 2020

"""

# import neccessary libraries 
from abc import  ABCMeta, abstractmethod
from random import randint
import savingsAccounts
from savingsAccounts import * 


savingsAccount = SavingsAccount()
while True:
    print("Enter 1 to create a new account")
    print('Enter 2 to access an existing acocunt')
    print("Enter 3 to exit")
    userChoise = int(input())
    if userChoise is 1 :
        print('Enter your name : ')
        name = input()    
        print("enter the initiale deposit : ")
        deposit = int(input())
        while (deposit < 2000):
            print("the deposit must be greater than 2000, enter a convenient number :")
            deposit = int(input())
        savingsAccount.createAccount(name, deposit)
    elif userChoise is 2 :
        print('enter your name : ')
        name = input()
        print("enter your account number : ")
        accountNumber = int(input())
        authentificateStatus = savingsAccount.authenticate(name, accountNumber)
        while authentificateStatus is True :
            print("enter 1 to withdraw ")
            print('enter 2 to deposite ')
            print('enter 3 to display balance ')
            userChoise = int(input())
            if userChoise is 1 :
                print("enter a withdraw amount : ")
                withdrawAmount = int(input())
                savingsAccount.withdraw(withdrawAmount)
            elif userChoise is 2 :
                print("enter an amount to be deposited")
                depositAmount = int(input())
                savingsAccount.deposit(depositAmount)
            elif userChoise is 3 :
                savingsAccount.displayBalance()
            elif userChoise is 4 :
                break
    elif userChoise is 3 :
        quit()
        
        