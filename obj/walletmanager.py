from datetime import datetime
from obj.account import Account
import calendar
class WalletManager():
    def __init__(self, account: Account):
        self.account = account
        self.current_date = datetime.now()
    
    def get_account_number_non_visible(self):
        return f"XXX-X-{str(self.get_account_number())[4:8]}-X"
    
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

        return limit
    
    def get_max_daily_limit(self, category):
        if category in self.account.monthly_limits:
            return self.account.monthly_limits[category] / calendar.monthrange(self.current_date.year, self.current_date.month)[1]
        return "Category not found"