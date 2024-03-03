from datetime import datetime
from obj.account import Account
from obj.transaction import *
import calendar
import random
import uuid

import ZODB, ZODB.config

path = "./db/config.xml"
db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root

class WalletManager():
    def __init__(self):
        self.account: Account = None
        self.current_date = datetime.now()
    
    def get_account_number_non_visible(self):
        return f"xxx-x-{str(self.get_account_number())[4:8]}-x"
    
    def get_account_number(self):
        return self.account.getID()
    
    def get_account_number_visible(self):
        return f"{str(self.get_account_number())[:3]}-{str(self.get_account_number())[3]}-{str(self.get_account_number())[4:8]}-{str(self.get_account_number())[8:]}"
    
    def get_balance(self):
        return "{:,}".format(self.account.getBalance())
    
    def isSelfExpense(self, transaction):
        return transaction.sender == self.get_account_number()
    
    def calculate_daily_limit(self, category):
        # limit is monthly limit divided by number of days in that month minus with all transactions in that category in that day
        if not category in self.account.monthly_limits:
            return "Category not found"
                
        limit = self.account.monthly_limits[category] / calendar.monthrange(self.current_date.year, self.current_date.month)[1]
        for transaction in self.account.transactions:
            if self.isSelfExpense(transaction) and transaction.date.month == self.current_date.month and transaction.date.day == self.current_date.day and transaction.__class__.__name__.lower() == category:
                limit -= transaction.amount
        return limit
    
    def get_max_daily_limit(self, category):
        if category in self.account.monthly_limits:
            return self.account.monthly_limits[category] / calendar.monthrange(self.current_date.year, self.current_date.month)[1]
        return "Category not found"
    
    def calculate_monthly_limit(self, category):
        if not category in self.account.monthly_limits:
            return "Category not found"
        
        limit = self.account.monthly_limits[category]
        for transaction in self.account.transactions:
            if self.isSelfExpense(transaction) and transaction.date.month == self.current_date.month and transaction.__class__.__name__.lower() == category:
                limit -= transaction.amount
        return limit
    
    def get_max_monthly_limit(self, category):
        if category in self.account.monthly_limits:
            return self.account.monthly_limits[category]
        return "Category not found"
    
    def get_total_expense_of_this_month(self):
        total = 0
        for transaction in self.account.transactions:
            if self.isSelfExpense(transaction) and transaction.date.month == self.current_date.month:
                total += transaction.amount
        return total
    
    def set_account(self, accountID):
        self.account = root.accounts[accountID]
    
    def login_account(self, email, password):
        for account in root.accounts.values():
            if account.login(email, password):
                self.account = account
                return self.account
            
        return None

    def register_account(self, name, email, password):
        account = Account(name, 0, self.generate_account_number(), password, email)
        root.accounts[account.getID()] = account
        connection.transaction_manager.commit()
        
    def generate_account_number(self):
        randnum = str(random.randint(000000000, 999999999))
        if not randnum in root.accounts:
            return randnum
        else:
            return self.generate_account_number()
        
    def check_accounts(self, accountID):
        return accountID in root.accounts
    
    def get_limits(self):
        limits = self.account.limits_rate
        for key in limits:
            limits[key] = limits[key] * 100
        return limits
    
    def get_average_income(self):
        return self.account.average_income
    
    def save_limits_and_income(self, limits, income):
        self.account.limits_rate = limits
        self.account.average_income = income
        self.account.updateMonthlyLimits()
        root._p_changed = True
        connection.transaction_manager.commit()

    def accountNumberIsValid(self, accountID):
        try:
            account_id_int = int(accountID)
            if len(str(account_id_int)) == 9 and self.check_accounts(accountID) and self.account.getID() != accountID:
                return True
            else:
                return False
        except ValueError:
            return False
    
    def handleTransfer(self, accountID, amount, transferType):
        if amount > self.account.getBalance():
            print("Not enough balance")
            return False
        
        transactionID = str(uuid.uuid4())
        
        match transferType:
            case "food":
                transaction = Food(transactionID, self.current_date, amount, self.get_account_number(), accountID, self.calculate_daily_limit("food"), amount / self.calculate_daily_limit("food") * 100, (1 - amount / self.calculate_daily_limit("food")) * 100)
            case "housing":
                transaction = Housing(transactionID, self.current_date, amount, self.get_account_number(), accountID, self.calculate_daily_limit("housing"), amount / self.calculate_daily_limit("housing") * 100, (1 - amount / self.calculate_daily_limit("housing")) * 100)
            case "transport":
                transaction = Transport(transactionID, self.current_date, amount, self.get_account_number(), accountID, self.calculate_daily_limit("transport"), amount / self.calculate_daily_limit("transport") * 100, (1 - amount / self.calculate_daily_limit("transport")) * 100)
            case "entertainment":
                transaction = Entertainment(transactionID, self.current_date, amount, self.get_account_number(), accountID, self.calculate_daily_limit("entertainment"), amount / self.calculate_daily_limit("entertainment") * 100, (1 - amount / self.calculate_daily_limit("entertainment")) * 100)
            case "healthcare":
                transaction = Healthcare(transactionID, self.current_date, amount, self.get_account_number(), accountID, self.calculate_daily_limit("healthcare"), amount / self.calculate_daily_limit("healthcare") * 100, (1 - amount / self.calculate_daily_limit("healthcare")) * 100)
            case "lend":
                transaction = Lend(transactionID, self.current_date, amount, self.get_account_number(), accountID, "-INF", 0, amount)
            case "return":
                transaction = Return(transactionID, self.current_date, amount, self.get_account_number(), accountID, "INF", 0, amount)
            case "others":
                transaction = Other(transactionID, self.current_date, amount, self.get_account_number(), accountID, self.calculate_daily_limit("others"), amount / self.calculate_daily_limit("others") * 100, (1 - amount / self.calculate_daily_limit("others")) * 100)
            case _:
                transaction = Transaction(transactionID, self.current_date, amount, self.get_account_number(), accountID)
        
        if transaction.isOverLimit():
            print("Over limit")
            return False
        
        root.transactions[transactionID] = transaction
        
        self.account.addTransaction(root.transactions[transactionID])
        self.account.withdraw(amount)
        
        recipient = root.accounts[accountID]
        recipient.deposit(amount)
        recipient.addTransaction(root.transactions[transactionID])
        
        root._p_changed = True
        connection.transaction_manager.commit()
        
        return True