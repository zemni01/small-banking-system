"""

small banking system 
author : Houssem Zemni 
year : 2020

"""

# import neccessary libraries 
from abc import  ABCMeta, abstractmethod
from random import randint

# abstraction class base for accounts
class account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def authenticate():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def displayBalance():
        return 0

# savings accounts class that inherite account class 
class SavingsAccount(account):
    def __init__(self):
        # [key][0]=> name ; [key][1] => balance
        self.savingsAccounts = {}

    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000, 99999)
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]
        print("Creation was successful, Your account Number is : ", self.accountNumber)
        
    def authenticate(self, name, accountNumber):
        if (accountNumber in self.savingsAccounts.keys()):
            if self.savingsAccounts[accountNumber][0] == name :
                print("Authentification successful")
                self.accountNumber = accountNumber
                return True
            else :
                print("Authentification failed")
                return False
        else :
            print('authentification failed')
            return False    
        
    
    def withdraw(self, withdrawAmount):
        if (withdrawAmount > self.savingsAccounts[self.accountNumber][1]):
            print("Insufficient Balance")
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawAmount
            print("Withdraw was successful. ")
            self.displayBalance()
        

    
    def deposit(self, depositAmount):
        self.savingsAccounts[self.accountNumber][1] += depositAmount
        print("Deposit was successful.")
        self.displayBalance()
        

    def displayBalance(self):
        print("available balance : ", self.savingsAccounts[self.accountNumber][1])


