import persistent

class Account(persistent.Persistent):
    def __init__(self, name, balance, ID):
        self.name = name
        self.balance = balance
        self.ID = ID
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
        
    def __str__(self):
        return "%s: %s" % (self.name, self.balance)