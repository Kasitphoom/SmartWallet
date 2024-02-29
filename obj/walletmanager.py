from datetime import datetime
from obj.account import Account
import calendar
import random

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
    
    def calculate_daily_limit(self, category):
        # limit is monthly limit divided by number of days in that month minus with all transactions in that category in that day
        if not category in self.account.monthly_limits:
            return "Category not found"
        
        if not category in self.account.monthly_limits:
            self.account.monthly_limits[category] = self.account.limits_rate[category] * self.account.average_income
                
        limit = self.account.monthly_limits[category] / calendar.monthrange(self.current_date.year, self.current_date.month)[1]
        for transaction in self.account.transactions:
            if transaction.date.month == self.current_date.month and transaction.date.day == self.current_date.day and transaction.category == category:
                limit -= transaction.amount
        print("Calculate daily limit:", self.account.monthly_limits, category)
        return limit
    
    def get_max_daily_limit(self, category):
        if category in self.account.monthly_limits:
            return self.account.monthly_limits[category] / calendar.monthrange(self.current_date.year, self.current_date.month)[1]
        return "Category not found"
    
    def get_total_expense_of_this_month(self):
        total = 0
        for transaction in self.account.transactions:
            if transaction.date.month == self.current_date.month:
                total += transaction.amount
        return total
    
    def set_account(self, accountID):
        self.account = root.accounts[accountID]
    
    def login_account(self, email, password):
        for account in root.accounts.values():
            print(account.login(email, password), account.email, account.password, email, password)
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
