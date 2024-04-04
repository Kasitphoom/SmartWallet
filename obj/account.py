import persistent


class Account(persistent.Persistent):
    def __init__(self, name, balance, ID, password, email, average_income = 0):
        self.name = name
        self.password = password
        self.email = email
        self.balance = balance
        self.ID = ID
        self.transactions = []
        self.parental_control = False
        self.allow_over_budget = True
        self.average_income = average_income
        self.total_savings = 0
        self.limits_rate = {
            "housing": 0,
            "food": 0.4,
            "transport": 0.15,
            "saving": 0.2,
            "entertainment": 0.1,
            "healthcare": 0.05,
            "others": 0.1
        }
        self.monthly_limits = {
            "housing": 0,
            "food": 0,
            "transport": 0,
            "saving": 0,
            "entertainment": 0,
            "healthcare": 0,
            "others": 0
        }
        
        self.updateMonthlyLimits()
        
    def login(self, email, password):
        return self.email == email and self.password == password
    
    def addTransaction(self, transaction):
        self.transactions.append(transaction)
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
    
    def getID(self):
        return self.ID
    
    def getName(self):
        return self.name
    
    def getEmail(self):
        return self.email
        
    def getBalance(self):
        # return balance that is formatted to 2 decimal places
        return round(self.balance, 2)

    def getMonthlyLimits(self):
        return self.monthly_limits
    
    def updateMonthlyLimits(self):
        self.monthly_limits["housing"] = self.limits_rate["housing"] * self.average_income
        self.monthly_limits["food"] = self.limits_rate["food"] * self.average_income
        self.monthly_limits["transport"] = self.limits_rate["transport"] * self.average_income
        self.monthly_limits["saving"] = self.limits_rate["saving"] * self.average_income
        self.monthly_limits["entertainment"] = self.limits_rate["entertainment"] * self.average_income
        self.monthly_limits["healthcare"] = self.limits_rate["healthcare"] * self.average_income
        self.monthly_limits["others"] = self.limits_rate["others"] * self.average_income
    
    def toggleParentalControl(self):
        self.parental_control = not self.parental_control
    
    def toggleAllowOverBudget(self):
        self.allow_over_budget = not self.allow_over_budget
    
    def getTotalSavings(self):
        return self.total_savings
    
    def __str__(self):
        return "%s: %s" % (self.name, self.balance)