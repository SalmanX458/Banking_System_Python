import random
from datetime import datetime
import json

trans = {}

def load_data(trans):
    try:
        with open("transactions.json") as file:
            trans = json.load(file)
    except FileNotFoundError:
        print("File not found")

class Transactions:
    def __init__(self, amount, transaction_type):
        self.date = datetime.now()
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.date} - {self.amount}$ - {self.transaction_type}"

def random_account_number():
    """Function that generates a random account number"""
    return random.randint(10000, 99999)

class BankAccount:
    def __init__(self, account_Holder):
        self.account_Holder = account_Holder
        self.accountID = random_account_number()
        self.balance = 0
        self.transanctions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}$, New Balance: {self.balance}$")
            self.transanctions.append(Transactions(amount, "Deposit"))
        else:
            print("Deposit amount must be positive.")

    def withdrawal(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal: {amount}$, Remaining: {self.balance}$")
            self.transanctions.append(Transactions(amount, "Withraw"))
        else:
            print("Insufficient amount or Invalid withdrawal amount")

    def show_details(self):
        print(f"Account ID: {self.accountID}")
        print(f"Account Holder Name: {self.account_Holder}")
        print(f"Current Balance: {self.balance}")

    def print_transactions(self):
        print("Transactions history")
        for transaction in self.transanctions:
            print(transaction)

class savingsAccount(BankAccount):
    def __init__(self, account_Holder, minimum_balance):
        super().__init__(account_Holder)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print("Cannot Withdraw. Minimum account balance requirement not met.")
        else:
            super().withdrawal()
            self.transanctions.append(Transactions(amount, "Withdraw"))

class CheckingsAccount(BankAccount):
    def __init__(self, account_Holder):
        super().__init__(account_Holder)
        self.checkbook_issued = False

    def issue_checkbbok(self):
        if not self.checkbook_issued:
            self.checkbook_issued = True
            print("Checkbook Issued..")
        else:
            print("Checkbook already issued")


