from datetime import datetime
from datetime import time
from obj.account import Account
from obj.transaction import *
from obj.notification import Notification
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

    def get_account_name(self):
        return self.account.getName()
    
    def get_account_number_non_visible(self):
        return f"xxx-x-{str(self.get_account_number())[4:8]}-x"
    
    def get_account_number(self):
        return self.account.getID()
    
    def get_account_number_visible(self):
        return f"{str(self.get_account_number())[:3]}-{str(self.get_account_number())[3]}-{str(self.get_account_number())[4:8]}-{str(self.get_account_number())[8:]}"
    
    def get_balance(self):
        return "{:,}".format(self.account.getBalance())
    
    def isSelfExpense(self, transaction):
        return transaction.sender == self.account
    
    def getTransactionsHistory(self):
        return self.account.transactions[::-1]
    
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
    
    def get_total_expense_period(self, start_date, end_date):
        total = 0
        for transaction in self.account.transactions:
            if self.isSelfExpense(transaction) and start_date <= transaction.date <= end_date:
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
                daily_limit = self.calculate_daily_limit("food") if self.calculate_daily_limit("food") != 0 else 0.01
                transaction = Food(transactionID, self.current_date, datetime.now().time(), amount, self.account, root.accounts[accountID], self.calculate_daily_limit("food"), amount / daily_limit * 100, (1 - amount / daily_limit) * 100)
            case "housing":
                daily_limit = self.calculate_daily_limit("housing") if self.calculate_daily_limit("housing") != 0 else 0.01
                transaction = Housing(transactionID, self.current_date, datetime.now().time(), amount, self.account, root.accounts[accountID], self.calculate_daily_limit("housing"), amount / daily_limit * 100, (1 - amount / daily_limit) * 100)
            case "transport":
                daily_limit = self.calculate_daily_limit("transport") if self.calculate_daily_limit("transport") != 0 else 0.01
                transaction = Transport(transactionID, self.current_date, datetime.now().time(), amount, self.account, root.accounts[accountID], self.calculate_daily_limit("transport"), amount / daily_limit * 100, (1 - amount / daily_limit) * 100)
            case "entertainment":
                daily_limit = self.calculate_daily_limit("entertainment") if self.calculate_daily_limit("entertainment") != 0 else 0.01
                transaction = Entertainment(transactionID, self.current_date, datetime.now().time(), amount, self.account, root.accounts[accountID], self.calculate_daily_limit("entertainment"), amount / daily_limit * 100, (1 - amount / daily_limit) * 100)
            case "healthcare":
                daily_limit = self.calculate_daily_limit("healthcare") if self.calculate_daily_limit("healthcare") != 0 else 0.01
                transaction = Healthcare(transactionID, self.current_date, datetime.now().time(), amount, self.account, root.accounts[accountID], self.calculate_daily_limit("healthcare"), amount / daily_limit * 100, (1 - amount / daily_limit) * 100)
            case "lend":
                transaction = Lend(transactionID, self.current_date, datetime.now().time(), amount, self.account, root.accounts[accountID], float("-inf"), 0, amount)
            case "return":
                transaction = Return(transactionID, self.current_date, datetime.now().time(), amount, self.account, root.accounts[accountID], float("inf"), 0, amount)
            case "others":
                daily_limit = self.calculate_daily_limit("others") if self.calculate_daily_limit("others") != 0 else 0.01
                transaction = Others(transactionID, self.current_date, datetime.now().time(), amount, self.account, root.accounts[accountID], self.calculate_daily_limit("others"), amount / daily_limit * 100, (1 - amount / daily_limit) * 100)
            case _:
                transaction = Transaction(transactionID, self.current_date, datetime.now().time(), amount, self.account, root.accounts[accountID])
        
        if transaction.isOverLimit():
            notification = Notification(transaction.getOverLimitAmount(), type(transaction).__name__, self.account.allow_over_budget)
            if not notification.show_notification():
                # user chose to cancel
                return False
            # user chose to proceed
        
        root.transactions[transactionID] = transaction
        
        self.account.addTransaction(root.transactions[transactionID])
        self.account.withdraw(amount)
        
        recipient = root.accounts[accountID]
        recipient.deposit(amount)
        recipient.addTransaction(root.transactions[transactionID])
        
        root._p_changed = True
        connection.transaction_manager.commit()
        
        return True
    
    def getName(self):
        return self.account.getName()
    
    def getEmail(self):
        return self.account.getEmail()
    
    def getGraphData(self, date, type):
        period = None

        match type:
            case "day":
                period = date
            case "month":
                period = date.month()
            case "year":
                period = date.year()
            case _:
                print("type : ", type)
                raise ValueError("Invalid type of period in getGraphData()")
            
        x_axis = None
        if type == "day":
            x_axis = [str(i)+":00" for i in range(24)]
        elif type == "month":
            x_axis = [str(i)+"/"+str(date.month()) for i in range(1, calendar.monthrange(date.year(), date.month())[1]+1)]
        elif type == "year":
            x_axis = [calendar.month_name[i] for i in range(1, 13)]

        data = {
            "income": {i: 0 for i in x_axis},
            "expense": {i: 0 for i in x_axis}
        }
            
        
        #get all transactions of that period
        transactions = [
            transaction for transaction in self.account.transactions if (
                (type == "day" and transaction.date == period) or
                (type == "month" and transaction.date.month == period) or
                (type == "year" and transaction.date.year == period)
            )
        ]

        for transaction in self.account.transactions:
            print("-----------------")
            print(transaction.date.year)
            print(period)
            print(transaction.date.year == period)
            
        # put all transactions into data
        for transaction in transactions:
            key = None
            if type == "day":
                key = str(transaction.date.hour)+":00"
            elif type == "month":
                key = str(transaction.date.day)+"/"+str(transaction.date.month)
            elif type == "year":
                key = calendar.month_name[transaction.date.month]

            if self.isSelfExpense(transaction):
                data["expense"][key] += transaction.amount
            else:
                data["income"][key] += transaction.amount

        return data
    
    def toggleParentalControl(self):
        self.account.toggleParentalControl()
        root._p_changed = True
        connection.transaction_manager.commit()
    
    def getParentalControl(self):
        return self.account.parental_control
    
    def toggleAllowOverBudget(self):
        self.account.toggleAllowOverBudget()
        root._p_changed = True
        connection.transaction_manager.commit()
    
    def getAllowOverBudget(self):
        return self.account.allow_over_budget