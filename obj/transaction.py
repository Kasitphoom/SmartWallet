import persistent
from datetime import datetime
from obj.account import Account
class Transaction(persistent.Persistent):
    def __init__(self, transactionID: str, date: datetime, amount: float, sender: Account, recipient: Account, spendlimit: int = 0, saved: int = 0, spend: int = 0, description: str = ""):
        self.transactionID = transactionID
        self.date = date
        self.amount = amount
        self.description = description
        self.sender = sender
        self.recipient = recipient
        self.spendlimit = spendlimit
        self.saved = saved
        self.spend = spend

    def __str__(self):
        return f"{self.date} {self.amount} {self.description}"
    
    def isOverLimit(self):
        return self.amount > self.spendlimit
    
    def warn_str(self):
        pass

class Food(Transaction):
    def __init__(self, transactionID, date: datetime, amount: float, sender, recipient, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        super().__init__(transactionID, date, amount, sender, recipient, spendlimit, saved, spend, description)

class Housing(Transaction):
    def __init__(self, transactionID, date: datetime, amount: float, sender, recipient, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        super().__init__(transactionID, date, amount, sender, recipient, spendlimit, saved, spend, description)

class Transport(Transaction):
    def __init__(self, transactionID, date: datetime, amount: float, sender, recipient, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        super().__init__(transactionID, date, amount, sender, recipient, spendlimit, saved, spend, description)

class Entertainment(Transaction):
    def __init__(self, transactionID, date: datetime, amount: float, sender, recipient, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        super().__init__(transactionID, date, amount, sender, recipient, spendlimit, saved, spend, description)

class Healthcare(Transaction):
    def __init__(self, transactionID, date: datetime, amount: float, sender, recipient, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        super().__init__(transactionID, date, amount, sender, recipient, spendlimit, saved, spend, description)
        
class Lend(Transaction):
    def __init__(self, transactionID, date: datetime, amount: float, sender, recipient, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        super().__init__(transactionID, date, amount, sender, recipient, spendlimit, saved, spend, description)

class Return(Transaction):
    def __init__(self, transactionID, date: datetime, amount: float, sender, recipient, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        super().__init__(transactionID, date, amount, sender, recipient, spendlimit, saved, spend, description)

class Others(Transaction):
    def __init__(self, transactionID, date: datetime, amount: float, sender, recipient, spendlimit = 0, saved = 0, spend = 0, description: str = ""):
        super().__init__(transactionID, date, amount, sender, recipient, spendlimit, saved, spend, description)
