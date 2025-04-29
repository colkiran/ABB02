
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self):
        print("Account.....")

    @abstractmethod
    def get_balance(self):
        pass

class Savings(Account):
    
    def get_balance(self):
        print("Balance in t")
    def deposit(self):
        print("Amount credited into the account.....")

sav = Savings()