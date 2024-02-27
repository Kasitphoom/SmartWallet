from datetime import datetime
from obj.account import Account
class WalletManager():
    def __init__(self, account: Account):
        self.account = account
        self.current_date = datetime.now()
        
        self.check_monthly_limit()
    
    def get_account_number_non_visible(self):
        return f"XXX-X-{str(self.get_account_number())[4:8]}-X"
    
    def get_account_number(self):
        return self.account.getID()
    
    def get_account_number_visible(self):
        return f"{str(self.get_account_number())[:3]}-{str(self.get_account_number())[3]}-{str(self.get_account_number())[4:8]}-{str(self.get_account_number())[8:]}"
    
    def get_balance(self):
        return "{:,}".format(self.account.getBalance())
    
    def check_monthly_limit(self):
        if not "month" in self.account.monthly_limits or self.current_date.month != self.account.monthly_limits["month"]:
            self.account.monthly_limits["month"] = self.current_date.month
            self.account.monthly_limits["food"] = self.account.limits_rate["food"] * self.account.average_income
            self.account.monthly_limits["transport"] = self.account.limits_rate["transport"] * self.account.average_income
            self.account.monthly_limits["saving"] = self.account.limits_rate["saving"] * self.account.average_income
            self.account.monthly_limits["entertainment"] = self.account.limits_rate["entertainment"] * self.account.average_income
            self.account.monthly_limits["healthcare"] = self.account.limits_rate["healthcare"] * self.account.average_income
            self.account.monthly_limits["others"] = self.account.limits_rate["others"] * self.account.average_income
        return self.account.monthly_limits
    
    def calculate_daily_limit(self, category):
        # limit is monthly limit divided by number of days in that month minus with all transactions in that category in that day
        if not category in self.account.monthly_limits:
            return "Category not found"
        
        for transaction in self.account.transactions:
            if transaction.date.month == self.current_date.month and transaction.date.day == self.current_date.day and transaction.category == category:
                if not category in self.account.monthly_limits:
                    self.account.monthly_limits[category] = self.account.limits_rate[category] * self.account.average_income
                self.account.monthly_limits[category] -= transaction.amount
        
        return self.account.monthly_limits[category]