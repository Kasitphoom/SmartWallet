import persistent

class Account(persistent.Persistent):
    def __init__(self, name, balance, ID):
        self.name = name
        self.balance = balance
        self.ID = ID
        self.transactions = []
        
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
    
    def __str__(self):
        return "%s: %s" % (self.name, self.balance)