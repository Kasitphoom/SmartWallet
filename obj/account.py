import persistent

class Account(persistent.Persistent):
    def __init__(self, name, balance, ID, average_income = 0):
        self.name = name
        self.balance = balance
        self.ID = ID
        self.transactions = []
        self.average_income = average_income
        self.limits_rate = {
            "food": 0.2,
            "transport": 0.15,
            "saving": 0.2,
            "entertainment": 0.1,
            "healthcare": 0.05,
            "others": 0.1
        }
        self.monthly_limits = {}
        
    def addTransaction(self, transaction):
        self.transactions.append(transaction)
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
    
    def getID(self):
        return self.ID
        
    def getBalance(self):
        """Return in format of 1,000 THB"""
        return self.balance

    def getMonthlyLimits(self):
        return self.monthly_limits
    
    def __str__(self):
        return "%s: %s" % (self.name, self.balance)