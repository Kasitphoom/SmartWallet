import persistent
from datetime import datetime
from datetime import time
from obj.account import Account
class Transaction(persistent.Persistent):
    def __init__(self, transactionID: str, date: datetime, time: time, amount: float, sender: Account, recipient: Account, spendlimit: int = 0, saved: int = 0, spend: int = 0, description: str = ""):
        self.transactionID = transactionID
        self.date = date
        self.time = time
        self.amount = amount
        self.description = description
        self.sender = sender
        self.recipient = recipient
        self.spendlimit = spendlimit
        self.saved = saved
        self.spend = spend
        self.itemList = [["Not Specified", amount]]

    def __str__(self):
        return f"{self.date} {self.amount} {self.description} {self.date}"
    
    def isOverLimit(self):
        return self.amount > self.spendlimit
    
    def getOverLimitAmount(self):
        return round(self.amount - self.spendlimit, 2)
    
    def warn_str(self):
        pass
    
    def setItemList(self, itemList):
        self.itemList = itemList

    def checkTransactionPeriod(self, type, period):
        if (type == "day" and self.date == period) or (type == "month" and self.date.month == period) or (type == "year" and self.date.year == period):
            return True
        return False

class Food(Transaction):
    def __init__(self, transactionID, date: datetime, time: time, amount: float, sender, recipient, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spendlimit, saved, spend, description)

class Housing(Transaction):
    def __init__(self, transactionID, date: datetime, time: time, amount: float, sender, recipient, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spendlimit, saved, spend, description)

class Transport(Transaction):
    def __init__(self, transactionID, date: datetime, time: time, amount: float, sender, recipient, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spendlimit, saved, spend, description)

class Entertainment(Transaction):
    def __init__(self, transactionID, date: datetime, time: time, amount: float, sender, recipient, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spendlimit, saved, spend, description)

class Healthcare(Transaction):
    def __init__(self, transactionID, date: datetime, time: time, amount: float, sender, recipient, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spendlimit, saved, spend, description)
        
class Lend(Transaction):
    def __init__(self, transactionID, date: datetime, time: time, amount: float, sender, recipient, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spendlimit, saved, spend, description)

class Return(Transaction):
    def __init__(self, transactionID, date: datetime, time: time, amount: float, sender, recipient, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spendlimit, saved, spend, description)

class Others(Transaction):
    def __init__(self, transactionID, date: datetime, time: time, amount: float, sender, recipient, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spendlimit, saved, spend, description)

class Bill(Transaction):
    def __init__(self, transactionID, date: datetime, time: time, amount: float, sender, recipient, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spend = amount, description = description)