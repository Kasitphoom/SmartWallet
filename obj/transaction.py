import persistent
from datetime import datetime
from obj.account import Account
class Transaction(persistent.Persistent):
    def __init__(self, date: datetime, amount: float, target_account: Account, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        self.date = date
        self.amount = amount
        self.description = description
        self.target_account = target_account
        self.spendlimit = spendlimit
        self.saved = saved
        self.spend = spend

    def __str__(self):
        return f"{self.date} {self.amount} {self.description}"