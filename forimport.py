class Account(persistent.Persistent):
    def __init__(self: self, name: str, balance: float, ID: str, password: str, email: str, average_income: float = 0, pin: str = None):
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
        self.pin = pin
        self.pin_pc = None
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
        
    def login(email: str, password: str) -> bool:
        return self.email == email and self.password == password
    
    def addTransaction(transaction: Transaction):
        self.transactions.append(transaction)
        
    def deposit(amount: float):
        self.balance += amount
        
    def withdraw(amount: float):
        self.balance -= amount
    
    def getID() -> str:
        return self.ID
    
    def getName() -> str:
        return self.name
    
    def getEmail() -> str:
        return self.email
        
    def getBalance() -> float:
        # return balance that is formatted to 2 decimal places
        return round(self.balance, 2)

    def getMonthlyLimits() -> dict[str, float]:
        return self.monthly_limits
    
    def updateMonthlyLimits():
        self.monthly_limits["housing"] = self.limits_rate["housing"] * self.average_income
        self.monthly_limits["food"] = self.limits_rate["food"] * self.average_income
        self.monthly_limits["transport"] = self.limits_rate["transport"] * self.average_income
        self.monthly_limits["saving"] = self.limits_rate["saving"] * self.average_income
        self.monthly_limits["entertainment"] = self.limits_rate["entertainment"] * self.average_income
        self.monthly_limits["healthcare"] = self.limits_rate["healthcare"] * self.average_income
        self.monthly_limits["others"] = self.limits_rate["others"] * self.average_income
    
    def toggleParentalControl():
        self.parental_control = not self.parental_control
    
    def toggleAllowOverBudget():
        self.allow_over_budget = not self.allow_over_budget
    
    def getTotalSavings() -> float:
        return self.total_savings
    
    def __str__() -> str:
        return "%s: %s" % (self.name, self.balance)
    
    def setPin(pin: str):
        self.pin = pin

    def getPin(pin:str):
        return self.pin
    
    def setPinPC(pin: str):
        self.pin_pc = pin

    def getPinPC(pin: str) -> str:
        return self.pin_pc

class Transaction(persistent.Persistent):
    def __init__(self: self, transactionID: str, date: datetime, time: time, amount: float, sender: Account, recipient: Account, spendlimit: int = 0, saved: int = 0, spend: int = 0, description: str = ""):
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

    def __str__() -> str:
        return f"{self.date} {self.amount} {self.description} {self.date}"
    
    def isOverLimit() -> bool:
        return self.amount > self.spendlimit
    
    def getOverLimitAmount() -> float:
        return round(self.amount - self.spendlimit, 2)
    
    def warn_str():
        pass
    
    def setItemList(itemList: list[list[str]]):
        self.itemList = itemList

class Food(Transaction):
    def __init__(self: self, transactionID: str, date: datetime, time: time, amount: float, sender: Account, recipient: Account, spendlimit: float = 0, saved: float = 0, spend: float = 0, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spendlimit, saved, spend, description)

class Housing(Transaction):
    def __init__(self: self, transactionID: str, date: datetime, time: time, amount: float, sender: Account, recipient: Account, spendlimit: float = 0, saved: float = 0, spend: float = 0, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spendlimit, saved, spend, description)

class Transport(Transaction):
    def __init__(self: self, transactionID: str, date: datetime, time: time, amount: float, sender: Account, recipient: Account, spendlimit: float = 0, saved: float = 0, spend: float = 0, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spendlimit, saved, spend, description)

class Entertainment(Transaction):
    def __init__(self: self, transactionID: str, date: datetime, time: time, amount: float, sender: Account, recipient: Account, spendlimit: float = 0, saved: float = 0, spend: float = 0, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spendlimit, saved, spend, description)

class Healthcare(Transaction):
    def __init__(self: self, transactionID: str, date: datetime, time: time, amount: float, sender: Account, recipient: Account, spendlimit: float = 0, saved: float = 0, spend: float = 0, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spendlimit, saved, spend, description)
        
class Lend(Transaction):
    def __init__(self: self, transactionID: str, date: datetime, time: time, amount: float, sender: Account, recipient: Account, spendlimit: float = 0, saved: float = 0, spend: float = 0, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spendlimit, saved, spend, description)

class Return(Transaction):
    def __init__(self: self, transactionID: str, date: datetime, time: time, amount: float, sender: Account, recipient: Account, spendlimit: float = 0, saved: float = 0, spend: float = 0, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spendlimit, saved, spend, description)

class Others(Transaction):
    def __init__(self: self, transactionID: str, date: datetime, time: time, amount: float, sender: Account, recipient: Account, spendlimit: float = 0, saved: float = 0, spend: float = 0, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spendlimit, saved, spend, description)

class Bill(Transaction):
    def __init__(self: self, transactionID: str, date: datetime, time: time, amount: float, sender: Account, recipient: Account, description: str = ""):
        super().__init__(transactionID, date, time, amount, sender, recipient, spend = amount, description = description)

class TransactionFrame(QFrame):
    clicked = Signal(Transaction)
    def __init__(self: self, parent: QWidget, transaction: Transaction, self_account_number: str):
        super().__init__(parent)
        self.transaction = transaction
        self.self_account_number = self_account_number
        self.setStyleSheet("font-size: 16px; font-family: 'Montserrat';")
        self.initUI()
        
    def checkExpense(self: self):
        return self.transaction.sender.getID() == self.self_account_number

    def mousePressEvent(self: self, event: QMouseEvent) -> None:
        self.clicked.emit(self.transaction)
        return super().mousePressEvent(event)
    
    def initUI(self: self):
        # self.setGeometry(QRect(0, 0, 300, 100))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName("frame")
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 10)
        self.layout.setSpacing(10)
        self.layout.setObjectName("HorizontalLayout")
        
        self.receiver_label = QLabel(self)
        name = self.transaction.recipient.getName() if self.checkExpense() else self.transaction.sender.getName()
        self.receiver_label.setText((name[:13] + '...') if len(name) > 13 else name)
        self.receiver_label.setAlignment(Qt.AlignBottom)
        self.receiver_label.setStyleSheet("width: 100px;")
        self.layout.addWidget(self.receiver_label)
        
        self.amount_type_layout = QHBoxLayout()
        self.amount_type_layout.setObjectName("HorizontalLayoutAmountType")
        
        self.amount_layout = QVBoxLayout()
        self.amount_layout.setObjectName("VerticalLayout")
        self.amount_layout.setSpacing(0)
        
        self.type = QLabel(self)
        self.type.setText(self.transaction.__class__.__name__.upper())
        self.type.setObjectName("type")
        self.type.setStyleSheet(f"color: {'rgba(79, 186, 116, 0.3)' if not self.checkExpense() else 'rgba(171, 52, 40, 0.35)'}; font-size: 10px; font-weight: bold; text-align: right;")
        self.type.setAlignment(Qt.AlignRight)
        
        self.amount_layout.addWidget(self.type)
        self.amount = QLabel(self)
        self.amount.setText(f"{-self.transaction.amount if self.checkExpense() else self.transaction.amount: ,.2f}")
        self.amount.setObjectName("amount")
        self.amount.setStyleSheet(f"font-size: 16px; font-weight: bold; color: {'#AB3428' if self.checkExpense() else '#4FBA74'}; text-align: right;")
        self.amount.setAlignment(Qt.AlignRight)
        self.amount_layout.addWidget(self.amount)
        self.amount_type_layout.addLayout(self.amount_layout)
        
        self.thb = QLabel(self)
        self.thb.setText("THB")
        self.thb.setObjectName("thb")
        self.thb.setAlignment(Qt.AlignBottom)
        self.thb.setStyleSheet(f"font-size: 10px; color: {'#AB3428' if self.checkExpense() else '#4FBA74'};")
        self.amount_type_layout.addWidget(self.thb)
        
        self.layout.addLayout(self.amount_type_layout)
        self.layout.setStretch(0, 1)

class BillFrame(QFrame):
    def __init__(self: self, parent: QWidget, name: str = "", amount: float = 0):
        super().__init__(parent)
        self.name = name
        self.amount = amount
        self.setStyleSheet("font-size: 16px; font-family: 'Montserrat'; background-color: #F5F5F5; border-radius: 10px; padding: 10px;")
        self.initUI()
    
    def initUI(self: self):
        self.setMaximumHeight(58)
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName("frame")
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setAlignment(Qt.AlignVCenter)
        
        self.nameInput = QLineEdit(self)
        self.nameInput.setText(self.name)
        self.nameInput.setStyleSheet("border-bottom: 1px solid black; border-radius: 0px;")
        
        self.amountInput = QLineEdit(self)
        self.amountInput.setText(str(self.amount))
        self.amountInput.setStyleSheet("border-bottom: 1px solid black; border-radius: 0px;")
        self.amountInput.setValidator(QIntValidator())
        
        self.deleteButton = QPushButton(self)
        self.deleteButton.setText("Trash")
        self.deleteButton.clicked.connect(self.delete)
        self.deleteButton.setStyleSheet("background-color: #AB3428; color: white; border-radius: 5px; padding: 10px; font-size: 16px; font-family: 'Font Awesome 6 Free'; font-weight: bold; width: auto;")
        self.deleteButton.setCursor(Qt.PointingHandCursor)
        
        self.layout.addWidget(self.nameInput, stretch=2)
        self.layout.addWidget(self.amountInput, stretch=1)
        self.layout.addWidget(self.deleteButton)
    
    def delete(self: self):
        self.deleteLater()
    
    def getValues(self: self):
        return [self.nameInput.text(), self.amountInput.text()]

class TransactionItem(QFrame):
    def __init__(self: self, parent: QWidget, item: list):
        super().__init__(parent)
        self.item = item
        self.setStyleSheet("font-size: 16px; font-family: 'Montserrat';")
        self.initUI()
        
    def initUI(self: self):
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName("TransactionItemFrame")
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        self.itemName = QLabel(self)
        self.itemName.setText(self.item[0] if len(self.item[0]) < 17 else self.item[0][:17] + "...")
        self.itemName.setObjectName("itemName")
        self.itemName.setStyleSheet("font-size: 16px; font-weight: bold; color: #979797;")
        self.layout.addWidget(self.itemName)
        
        self.amountFrame = QFrame(self)
        self.amountFrame.layout = QHBoxLayout(self.amountFrame)
        self.amountFrame.layout.addStretch(1)
        
        self.itemAmount = QLabel(self)
        self.itemAmount.setText(f"{float(self.item[1]): ,.2f}")
        self.itemAmount.setObjectName("itemAmount")
        self.itemAmount.setStyleSheet("font-size: 16px; font-weight: bold; color: black;")
        
        self.layout.addStretch(1)
        
        self.thb = QLabel(self)
        self.thb.setText("THB")
        self.thb.setObjectName("thb")
        self.thb.setStyleSheet("font-size: 10px; font-family: 'Montserrat'; color: black;")
        
        self.amountFrame.layout.addWidget(self.itemAmount)
        self.amountFrame.layout.addWidget(self.thb)
        
        self.layout.addWidget(self.amountFrame)
        
        self.setLayout(self.layout)

class WalletManager():
    def __init__(self: self):
        self.account: Account = None
        self.current_date = datetime.now()

    def get_account_name(self: self):
        return self.account.getName()
    
    def get_account_number_non_visible(self: self):
        return f"xxx-x-{str(self.get_account_number())[4:8]}-x"
    
    def get_account_number(self: self):
        return self.account.getID()
    
    def get_account_number_visible(self: self):
        return f"{str(self.get_account_number())[:3]}-{str(self.get_account_number())[3]}-{str(self.get_account_number())[4:8]}-{str(self.get_account_number())[8:]}"
    
    def get_balance(self: self):
        return "{:,}".format(self.account.getBalance())
    
    def isSelfExpense(self: self, transaction: Transaction):
        return transaction.sender == self.account
    
    def getTransactionsHistory(self: self):
        return self.account.transactions[::-1]
    
    def calculate_daily_limit(self: self, category: str):
        # limit is monthly limit divided by number of days in that month minus with all transactions in that category in that day
        if not category in self.account.monthly_limits:
            return "Category not found"
        
        limit = self.account.monthly_limits[category] / calendar.monthrange(self.current_date.year, self.current_date.month)[1]
        for transaction in self.account.transactions:
            if self.isSelfExpense(transaction) and transaction.date.month == self.current_date.month and transaction.date.day == self.current_date.day and transaction.__class__.__name__.lower() == category:
                limit -= transaction.amount
        return limit
    
    def get_max_daily_limit(self: self, category: str):
        if category in self.account.monthly_limits:
            return self.account.monthly_limits[category] / calendar.monthrange(self.current_date.year, self.current_date.month)[1]
        return "Category not found"
    
    def calculate_monthly_limit(self: self, category:str):
        if not category in self.account.monthly_limits:
            return "Category not found"
        
        limit = self.account.monthly_limits[category]
        for transaction in self.account.transactions:
            if self.isSelfExpense(transaction) and transaction.date.month == self.current_date.month and transaction.__class__.__name__.lower() == category:
                limit -= transaction.amount
        return limit
    
    def get_max_monthly_limit(self: self, category: str):
        if category in self.account.monthly_limits:
            return self.account.monthly_limits[category]
        return "Category not found"
    
    def get_total_expense_of_this_month(self: self):
        total = 0
        for transaction in self.account.transactions:
            if self.isSelfExpense(transaction) and transaction.date.month == self.current_date.month:
                total += transaction.amount
        return total
    
    def get_total_expense_period(self: self, start_date: datetime, end_date: datetime):
        total = 0
        for transaction in self.account.transactions:
            if self.isSelfExpense(transaction) and start_date <= transaction.date <= end_date:
                total += transaction.amount
        return total
    
    def get_total_income_period(self: self, start_date: datetime, end_date: datetime):
        total = 0
        for transaction in self.account.transactions:
            if not self.isSelfExpense(transaction) and start_date <= transaction.date <= end_date:
                total += transaction.amount
        return total
    
    def get_total_income_of_this_month(self: self):
        total = 0
        for transaction in self.account.transactions:
            if not self.isSelfExpense(transaction) and transaction.date.month == self.current_date.month:
                total += transaction.amount
        return total
    
    def set_account(self: self, accountID: str):
        self.account = root.accounts[accountID]
    
    def login_account(self, email, password):
        for account in root.accounts.values():
            if account.login(email, password):
                self.account = account
                return self.account
            
        return None

    def register_account(self: self, name: str, email: str, password: str):
        account = Account(name, 0, self.generate_account_number(), password, email)
        root.accounts[account.getID()] = account
        connection.transaction_manager.commit()
        
    def generate_account_number(self: self):
        randnum = str(random.randint(000000000, 999999999))
        if not randnum in root.accounts:
            return randnum
        else:
            return self.generate_account_number()
        
    def check_accounts(self: self, accountID: str):
        return accountID in root.accounts
    
    def get_limits(self: self):
        limits = self.account.limits_rate
        return limits
    
    def get_average_income(self: self):
        return self.account.average_income
    
    def save_limits_and_income(self: self, limits: float, income: float):
        self.account.limits_rate = limits
        self.account.average_income = income
        self.account.updateMonthlyLimits()
        root._p_changed = True
        connection.transaction_manager.commit()

    def accountNumberIsValid(self: self, accountID: str):
        try:
            account_id_int = int(accountID)
            if len(str(account_id_int)) == 9 and self.check_accounts(accountID) and self.account.getID() != accountID:
                return True
            else:
                return False
        except ValueError:
            return False
    
    def handleTransfer(self, accountID: str, amount: str, transferType: str) -> (bool, Transaction):
        if amount > self.account.getBalance():
            print("Not enough balance")
            return False, False
        
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
                return False, False
            # user chose to proceed

        return transaction, transactionID
    
    def transfer(self, accountID: str, amount: float, transaction: Transaction, transactionID: str):
        root.transactions[transactionID] = transaction
        
        self.account.addTransaction(root.transactions[transactionID])
        self.account.withdraw(amount)
        
        recipient = root.accounts[accountID]
        recipient.deposit(amount)
        recipient.addTransaction(root.transactions[transactionID])
        
        root._p_changed = True
        connection.transaction_manager.commit()
    
    def getName(self: self):
        return self.account.getName()
    
    def getEmail(self: self):
        return self.account.getEmail()
    
    def getGraphData(self: self, date: datetime, type: str) -> dict:
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
            "expense": {i: 0 for i in x_axis},
            "total_income": 0,
            "total_expense": 0,
        }
            
        
        #get all transactions of that period
        transactions = [
            transaction for transaction in self.account.transactions if (
                (type == "day" and transaction.date == period) or
                (type == "month" and transaction.date.month == period) or
                (type == "year" and transaction.date.year == period)
            )
        ]
            
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
                data["total_expense"] += transaction.amount
            else:
                data["income"][key] += transaction.amount
                data["total_income"] += transaction.amount

        return data
    
    def toggleParentalControl(self: self):
        self.account.toggleParentalControl()
        root._p_changed = True
        connection.transaction_manager.commit()
    
    def getParentalControl(self: self) -> bool:
        return self.account.parental_control
    
    def toggleAllowOverBudget(self: self):
        self.account.toggleAllowOverBudget()
        root._p_changed = True
        connection.transaction_manager.commit()
    
    def getAllowOverBudget(self: self) -> bool:
        return self.account.allow_over_budget
    
    def setPin(self: self, pin: str):
        self.account.setPin(pin)
        root._p_changed = True
        connection.transaction_manager.commit()

    def checkPin(self: self, pin: str) -> bool:
        # print("entered pin: ", pin)
        # print("account pin: ", self.account.pin)
        return pin == self.account.pin
    
    def getPin(self: self) -> str:
        return self.account.getPin()
    
    def addBill(self: self, item: list, total: float, billName: str) -> bool:
        try:
            transaction = Bill(str(uuid.uuid4()), self.current_date, datetime.now().time(), float(total), self.account, self.account, billName)
            transaction.setItemList(item)
            root.transactions[transaction.transactionID] = transaction
            self.account.addTransaction(root.transactions[transaction.transactionID])
            
            root._p_changed = True
            connection.transaction_manager.commit()
            return True
        except ValueError:
            return False
    
    def checkPinPC(self: self, pin: str) -> bool:
        return pin == self.account.pin_pc
    
    def getPinPC(self: self) -> str:
        return self.account.getPinPC()
    
    def setPinPC(self: self, pin: str):
        self.account.setPinPC(pin)
        root._p_changed = True
        connection.transaction_manager.commit()

class ToggleSwitch(QCheckBox):
    def __init__(
        self,
        width: int = 64,
        bg_color: str = "#5B5B5B",
        circle_color: str = "#FFFFFF",
        active_color: str = "#4FBA74",
        animation_curve: QEasingCurve = QEasingCurve.OutQuint,
        circle_margin: int = 3,
    ):
        QCheckBox.__init__(self)

        # Set default size
        self.setMinimumSize(width, 28)
        self.setCursor(Qt.PointingHandCursor)

        # Colors
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        # Animation Curve
        self._circle_position = circle_margin if not self.isChecked() else self.width() - self.height() + circle_margin
        
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)


        # Circle Margin (circle position)
        self._circle_margin = circle_margin
        
        # Connect State Changed
        self.stateChanged.connect(self.startTransition)

    def resizeEvent(self: self, event: QResizeEvent) -> None:
        self._circle_position = self._circle_margin if not self.isChecked() else self.width() - self.height() + self._circle_margin
        return super().resizeEvent(event)

    # Create new set and get property for animation
    @Property(int)
    def circle_position(self: self) -> int:
        return self._circle_position
    
    @circle_position.setter
    def circle_position(self: self, pos: int):
        self._circle_position = pos
        self.update()

    def startTransition(self: self, value: bool):
        # Stop animation if running
        self.animation.stop()

        if value:
            self.animation.setEndValue(self.width() - self.height() + self._circle_margin)
        else:
            self.animation.setEndValue(self._circle_margin)
            # im am here

        # Start Animation
        self.animation.start()
        

    # Set new hit area
    def hitButton(self: self, pos: QPoint):
        return self.contentsRect().contains(pos)
    
    # Paint Event (Draw Toggle Switch)
    def paintEvent(self: self, event: QPaintEvent):
        # SET Painter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # SET Pen
        painter.setPen(Qt.NoPen)
        
        # Draw Rectangle
        rect = QRect(0, 0, self.width(), self.height())

        if not self.isChecked():
            # Draw Background
            bg_color = QColor(self._bg_color)
            painter.setBrush(bg_color)
            painter.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)
            
            # Draw Circle
            painter.setBrush(QColor(self._circle_color))
            painter.drawEllipse(self._circle_position, 3, 22, 22)

        else:
            # Draw Background
            bg_color = QColor(self._active_color)
            painter.setBrush(bg_color)
            painter.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            # Draw Circle
            painter.setBrush(QColor(self._circle_color))
            painter.drawEllipse(self._circle_position, 3, 22, 22)

        # End
        painter.end()

class Notification:
    def __init__(self, exceeded_limit: int, limit_type: str, allow_over_limit: bool=True):
        self.exceeded_limit = exceeded_limit
        self.limit_type = limit_type
        self.allow_over_limit = allow_over_limit

    def show_notification(self):
        if self.allow_over_limit:
            return self.show_choice()
        else:
            return self.show_warning()
        
    def show_warning(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Limit Exceeded")
        msg.setText(f"The {self.limit_type} limit has been exceeded by {self.exceeded_limit}.")
        msg.exec_()
    
    def show_choice(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Limit Exceeded")
        msg.setText(f"The {self.limit_type} limit has been exceeded by {self.exceeded_limit}.")
        msg.setInformativeText("Would you like to proceed?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        ret = msg.exec_()
        return ret == QMessageBox.Ok
        
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)

#     # Example usage:
#     notification = Notification(10, "food")
#     notification.show_notification()

#     sys.exit(app.exec_())
class roundProgressBar(QWidget):
    def __init__(self: self, parent: QWidget, category: str = "food"):
        super().__init__(parent)
        self.category = category
        self.percentage = 0
        self.setMinimumSize(56, 56)
        # Load FontAwesome font
        font_id = QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "../otfs/Font Awesome 6 Free-Solid-900.otf").as_posix())
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.font_awesome = QFont(font_family)
        self.limit_font_awesome_map = {
            "housing": "building",
            "food": "bowl-food",
            "transport": "car",
            "entertainment": "film",
            "healthcare": "heart-pulse",
        }
        self.animation_speed = 10
        self.animation_duration = 500
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.animate_progress)
        self.animation_timer.setInterval(10)  # Interval in milliseconds

    def update_value(self: self, percentage: float):
        if self.percentage == percentage:
            return
        self.start_animation(percentage)

    def start_animation(self: self, target_percentage: float):
        self.target_percentage = target_percentage
        # Calculate the number of steps and interval time for smooth animation
        num_steps = int(self.animation_duration / self.animation_timer.interval())
        self.step_percentage = (self.target_percentage - self.percentage) / num_steps
        self.animation_step = 0
        self.animation_timer.start()

    def animate_progress(self: self):
        self.percentage += self.step_percentage
        self.animation_step += 1
        self.update()
        if self.animation_step >= self.animation_duration / self.animation_timer.interval():
            self.percentage = self.target_percentage
            self.animation_timer.stop()
            self.update()

    def animate_from_zero(self: self):
        percentage = self.percentage
        self.percentage = 0
        self.update_value(percentage)

    def paintEvent(self: self, event: QPaintEvent):
        if self.height() > self.width():
            self.setFixedWidth(self.height())
        if self.width() > self.height():
            self.setFixedHeight(self.width())
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        center = self.cal_center()
        circle_diameter = self.cal_circle_diameter()
        circle_radius = circle_diameter / 2
        circle_rect = QRectF(center.x() - circle_radius, center.y() - circle_radius, circle_diameter, circle_diameter)
        self.draw_progressed_arc(p, center, circle_rect)
        self.draw_remaining_arc(p, center, circle_rect)
        self.draw_percentage_text(p, center)
    
    def cal_center(self: self) -> QPoint:
        return self.rect().center()
    
    def cal_circle_diameter(self: self) -> int:
        return min(self.width(), self.height()) - 8

    def draw_progressed_arc(self: self, p: QPainter, center: QPoint, circle_rect: QRectF):
        percentage_degree = self.percentage * 360
        path = QPainterPath()
        path.moveTo(center.x(), center.y() - circle_rect.height() / 2)
        path.arcTo(circle_rect, 90, - percentage_degree)
        if self.gray_color:
            self.color = QColor("#D9D9D9")
        elif percentage_degree >= 50:
            self.color = QColor("#37C768")
        elif percentage_degree >= 25:
            self.color = QColor("#FDA653")
        else:
            self.color = QColor("#E06053")
        pen = QPen(self.color)
        pen.setCapStyle(Qt.FlatCap)
        pen.setWidthF(self.width() / 10)
        p.strokePath(path, pen)

    def draw_remaining_arc(self: self, p: QPainter, center: QPoint, circle_rect: QRectF):
        percentage_degree = self.percentage * 360
        remaining_degree = 360 - percentage_degree
        path = QPainterPath()
        path.moveTo(center.x(), center.y() - circle_rect.height() / 2)
        path.arcTo(circle_rect, 90, remaining_degree)
        pen = QPen(QColor("#D9D9D9"))
        pen.setCapStyle(Qt.FlatCap)
        pen.setWidthF(self.width() / 10)
        p.strokePath(path, pen)

    def draw_percentage_text(self: self, p: QPainter, center: QPoint):
        # Set FontAwesome font
        self.font_awesome.setPointSize(16)
        p.setFont(self.font_awesome)
        
        # Set font color
        font_color = self.color
        p.setPen(font_color)
        
        # Calculate text size
        text = self.limit_font_awesome_map[self.category]
        text_rect = p.fontMetrics().boundingRect(text)
        
        # Calculate the position for drawing text
        text_position = center - QPoint(text_rect.width() / 2, -text_rect.height() / 2 + 2)
        
        # Draw text at the specified position
        p.drawText(text_position, text)

    def get_category(self: self) -> str:
        return self.category
    
    def set_gray_color(self: self, boolean: bool):
        self.gray_color = boolean

    def get_if_gray_color(self: self) -> bool:
        return self.gray_color

class MainWindow(QMainWindow):
    def __init__(self: self, manager: WalletManager):
        super().__init__()
        self.manager = manager
        self.account_number_visibility = False
        self.calculated_limits = {}
        self.__salt = "rT8jllFhs7"
        self.transfer_type_selected = "others"
        self.current_date = datetime.now()
        # self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)
        self.detector = cv2.QRCodeDetector()
        self.pil_myQr = None
        self.page = {
            # stacked widget
            "dashboard": 0,
            "transfer": 1,
            "budgetplanner": 2,
            "directtransfer": 3,
            "history": 4,
            "scanqrcode": 5,
            "others": 6,
            "setting": 7,
            "myQRcode": 8,
            "parentalcontrol": 9,
            "graph": 10,
            "addbill": 11,
            "transactionInfo": 12,
            "captureReceipt": 13,
            # stacked widget 2
            "main": 0,
            "login": 1,
            "register": 2,
            "pin": 3,
        }
        

        # Add fonts in QFontDatabase before setting up the UI
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Font Awesome 6 Free-Solid-900.otf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-Black.ttf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-Bold.ttf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-ExtraBold.ttf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-ExtraLight.ttf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-Light.ttf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-Medium.ttf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-Regular.ttf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-SemiBold.ttf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-Thin.ttf").as_posix())
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        if user_cache == "":
            self.ui.stackedWidget_2.setCurrentIndex(self.page["login"])
        elif manager.check_accounts(user_cache):
            self.manager.set_account(user_cache)
            self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
            self.update_window()
            # set initial budget page
            self.setupBudget()
            self.setupOthersPage()
            # generate My QR code
            self.createMyQRcode()
            # setup parental control toggle
            self.pcToggleSetup()
            # setup graph page
            self.setupGraph()
        else:
            self.ui.stackedWidget_2.setCurrentIndex(self.page["login"])
        
        self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"])
        self.ui.frame_10.installEventFilter(self)
        
        # login page
        self.ui.loginButton.clicked.connect(self.handleLogin)
        self.ui.registerButton.clicked.connect(self.handleRegister)
        
        # show/hide account number
        self.ui.eyeButton.clicked.connect(self.handleAccountNumberVisibility)
        self.ui.eyeButtonDT.clicked.connect(self.handleAccountNumberVisibility)
        
        # buttons to change page
        self.ui.dashboardButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"]))
        self.ui.ftransferButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["transfer"]))
        self.ui.fbudgetplannerButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["budgetplanner"]))
        self.ui.budgetplannerButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["budgetplanner"]))
        self.ui.redirectToRegisterButton.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(self.page["register"]))
        self.ui.redirectToLoginButton.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(self.page["login"]))
        self.ui.transferbackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"]))
        self.ui.navigateToDirectTransferButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["directtransfer"]))
        self.ui.navigateToDirectQrcodeButton.clicked.connect(self.handleNavigationToScanQRCode)
        self.ui.fhistoryButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["history"]))
        self.ui.historyButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["history"]))
        self.ui.othersButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["others"]))
        self.ui.setting_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["setting"]))
        self.ui.fmyqrButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["myQRcode"]))
        self.ui.parental_control_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["parentalcontrol"]))
        self.ui.faddbillsButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["addbill"]))
        self.ui.graphButton.clicked.connect(self.handleNavigationToGraph)
        self.ui.fsummaryButton.clicked.connect(self.handleNavigationToGraph)
        self.ui.add_bill_open_cameraButton.clicked.connect(self.handleNaviationToCaptureReceipt)
        self.ui.capturereceiptBackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["addbill"]))
        self.ui.captureButton.clicked.connect(self.capture_image)

        
        # back buttons
        self.ui.budgetBackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"]))
        self.ui.dicrectTransferBackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["transfer"]))
        self.ui.historybackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"]))
        self.ui.othersBackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"]))
        self.ui.scanQRCodeBackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["transfer"]))
        self.ui.settingBackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["others"]))
        self.ui.transferbackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"]))
        self.ui.parentalControlBackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["setting"]))
        self.ui.graphBackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"]))
        self.ui.addbillBackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"]))

        # Pin
        self.pin_labels = [self.ui.pin_1, self.ui.pin_2, self.ui.pin_3, self.ui.pin_4, self.ui.pin_5, self.ui.pin_6]
        self.ui.pin_num_0.clicked.connect(lambda: self.addNumberToPin("0"))
        self.ui.pin_num_1.clicked.connect(lambda: self.addNumberToPin("1"))
        self.ui.pin_num_2.clicked.connect(lambda: self.addNumberToPin("2"))
        self.ui.pin_num_3.clicked.connect(lambda: self.addNumberToPin("3"))
        self.ui.pin_num_4.clicked.connect(lambda: self.addNumberToPin("4"))
        self.ui.pin_num_5.clicked.connect(lambda: self.addNumberToPin("5"))
        self.ui.pin_num_6.clicked.connect(lambda: self.addNumberToPin("6"))
        self.ui.pin_num_7.clicked.connect(lambda: self.addNumberToPin("7"))
        self.ui.pin_num_8.clicked.connect(lambda: self.addNumberToPin("8"))
        self.ui.pin_num_9.clicked.connect(lambda: self.addNumberToPin("9"))
        self.ui.pin_delete.clicked.connect(self.deletePin)

        # handle page change
        self.ui.stackedWidget_2.currentChanged.connect(self.page_changed_handler_2)
        self.ui.stackedWidget.currentChanged.connect(self.page_changed_handler)

        # setup transfer confirm button
        self.ui.dt_confirmButton.clicked.connect(self.handleTransfer)
        
        # handle history type change
        self.ui.history_all_button.clicked.connect(lambda: self.update_history_page("all"))
        self.ui.history_expense_button.clicked.connect(lambda: self.update_history_page("expense"))
        self.ui.history_income_button.clicked.connect(lambda: self.update_history_page("income"))
        
        # handle logout
        self.ui.logout_button.clicked.connect(self.handleLogout)

        # setup my QR code page
        self.ui.saveMyQRcodeButton.clicked.connect(self.saveMyQRcode)

        # handle Radio button in graph page
        self.ui.dayradioButton.toggled.connect(self.updateGraph)
        self.ui.monthradioButton.toggled.connect(self.updateGraph)
        self.ui.yearradioButton.toggled.connect(self.updateGraph)
        self.ui.lineradioButton.toggled.connect(self.updateGraph)
        self.ui.barradioButton.toggled.connect(self.updateGraph)
        self.ui.allradioButton.toggled.connect(self.updateGraph)
        self.ui.incomeradioButton.toggled.connect(self.updateGraph)
        self.ui.expenseradioButton.toggled.connect(self.updateGraph)

        self.ui.dateEdit.dateChanged.connect(self.updateGraph)
        
        # handle add bill
        self.ui.add_single_billButton.clicked.connect(self.addSingleBill)
        self.ui.add_bill_choose_fileButton.clicked.connect(self.addBillFromFile)
        self.ui.finish_addbillButton.clicked.connect(self.finishAddBill)

# ================================== Login and Registration Handling ==================================

    def handleLogin():
        email = self.ui.loginEmailLineEdit.text()
        password = self.ui.loginPasswordLineEdit.text() + self.__salt
        
        hash_object = hashlib.sha256(password.encode())
        password = hash_object.hexdigest()
        
        account = self.manager.login_account(email, password)
        
        if account:
            # save to cache
            with open(USER_CACHE_FILE, "wb") as f:
                user_cache = account.getID()
                self.manager.set_account(user_cache)
                pickle.dump(user_cache, f)
            if not self.manager.getPin():
                self.nagivateToPin("Create your PIN")
                self.ui.pinLineEdit.textChanged.connect(self.handlePinRegister)
            else:
                self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
                self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"])
                self.update_window()
                self.setupBudget()
                self.setupOthersPage()
                self.createMyQRcode()
        else:
            self.ui.loginError.setText("Invalid email or password")

    def handleRegister():
        fullname = self.ui.registerFullNameENLineEdit.text()
        email = self.ui.registerEmailLineEdit.text()
        password = self.ui.registerPasswordLineEdit.text() + self.__salt
        confirm_password = self.ui.registerConfirmPasswordLineEdit.text() + self.__salt
        
        if password != confirm_password:
            self.ui.registerConfirmPasswordError.setText("Password does not match")
            return
        
        hash_object = hashlib.sha256(password.encode())
        password = hash_object.hexdigest()
        
        self.manager.register_account(fullname, email, password)
        self.ui.stackedWidget_2.setCurrentIndex(self.page["login"])

    def handlePinRegister():
        if len(self.ui.pinLineEdit.text()) <= 6 and len(self.ui.pinLineEdit.text()) > 0:
            self.pin_labels[len(self.ui.pinLineEdit.text())-1].setStyleSheet("background-image: url(:/images/image/pin_dot.svg); background-repeat: no-repeat;")
        if len(self.ui.pinLineEdit.text()) == 6:
            pin = self.ui.pinLineEdit.text() + self.__salt
            hash_object = hashlib.sha256(pin.encode())
            pin = hash_object.hexdigest()
            self.manager.setPin(pin)
            self.ui.pinLineEdit.textChanged.disconnect()
            self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
            self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"])
            self.update_window()
            self.setupBudget()
            self.setupOthersPage()
            self.createMyQRcode()
        

# ================================== Dashboard ==================================

    def update_window():
        self.ui.d_balance_amount.setText(self.manager.get_balance() + " THB")
        
        # set text as this format XXX-X-1234-X
        self.ui.accountNumberlabel.setText(self.manager.get_account_number_non_visible())
        self.ui.accountNumberlabelDT.setText(self.manager.get_account_number_non_visible())
        
        # set balance
        self.ui.d_balance_amount.setText(self.manager.get_balance() + " THB")
        
        self.update_daily_limit()
        self.update_total_month_expense()
        
        # set transfer balance and budget amount
        self.ui.dt_balance_amount.setText(self.manager.get_balance() + " THB")
        
        # update month to date expense (from 1st of the month to today compare with 1st of last month to the same date as today)
        self.update_month_to_date_expense()
        
        # update history page
        self.update_history_page()
        
        self.update_total_savings()
        self.setupTransferPage()

    def update_daily_limit():
        # Update daily limit for each category and set the color of the limit frame and icon.
        # house limit
        housing_limit = self.manager.calculate_daily_limit("housing")
        max_housing_limit = self.manager.get_max_daily_limit("housing")
        
        
        self.ui.housinglimitlabel.setText(f"{housing_limit:,.2f}")
        self.ui.housinglimiticon.setStyleSheet(f"color: {'#B3625A' if housing_limit < max_housing_limit * 0.25 else '#F49E4C' if housing_limit < max_housing_limit * 0.50 else '#4FBA74'}")
        self.ui.housinglimitframe.setStyleSheet(self.style_sheet_color_limit("housing"))
        
        # food limit
        food_limit = self.manager.calculate_daily_limit("food")
        max_food_limit = self.manager.get_max_daily_limit("food")
        
        self.ui.foodlimitlabel.setText(f"{food_limit:,.2f}")
        self.ui.foodlimitframe.setStyleSheet(self.style_sheet_color_limit("food"))
        self.ui.foodlimiticon.setStyleSheet(f"color: {'#B3625A' if food_limit < max_food_limit * 0.25 else '#F49E4C' if food_limit < max_food_limit * 0.50 else '#4FBA74'}")
        
        # transport limit
        transport_limit = self.manager.calculate_daily_limit("transport")
        max_transport_limit = self.manager.get_max_daily_limit("transport")
        
        self.ui.transportationlimitlabel.setText(f"{transport_limit:,.2f}")
        self.ui.transportationlimitframe.setStyleSheet(self.style_sheet_color_limit("transport"))
        self.ui.transportationlimiticon.setStyleSheet(f"color: {'#B3625A' if transport_limit < max_transport_limit * 0.25 else '#F49E4C' if transport_limit < max_transport_limit * 0.50 else '#4FBA74'}")
        
        # entertainment limit
        entertainment_limit = self.manager.calculate_daily_limit("entertainment")
        max_entertainment_limit = self.manager.get_max_daily_limit("entertainment")
        
        self.ui.entertainmentlimitlabel.setText(f"{entertainment_limit:,.2f}")
        self.ui.entertainmentlimitframe.setStyleSheet(self.style_sheet_color_limit("entertainment"))
        self.ui.entertainmentlimiticon.setStyleSheet(f"color: {'#B3625A' if entertainment_limit < max_entertainment_limit * 0.25 else '#F49E4C' if entertainment_limit < max_entertainment_limit * 0.50 else '#4FBA74'}")
        
        # healthcare limit
        healthcare_limit = self.manager.calculate_daily_limit("healthcare")
        max_healthcare_limit = self.manager.get_max_daily_limit("healthcare")
        
        self.ui.healthcarelimitlabel.setText(f"{healthcare_limit:,.2f}")
        self.ui.healthcarelimitframe.setStyleSheet(self.style_sheet_color_limit("healthcare"))
        self.ui.healthcarelimiticon.setStyleSheet(f"color: {'#B3625A' if healthcare_limit < max_healthcare_limit * 0.25 else '#F49E4C' if healthcare_limit < max_healthcare_limit * 0.50 else '#4FBA74'}")
        
        # other limit
        other_limit = self.manager.calculate_daily_limit("others")
        max_other_limit = self.manager.get_max_daily_limit("others")
        
        self.ui.otherlimitlabel.setText(f"{other_limit:,.2f}")
        self.ui.otherlimitframe.setStyleSheet(self.style_sheet_color_limit("others"))
        self.ui.otherlimiticon.setStyleSheet(f"color: {'#B3625A' if other_limit < max_other_limit * 0.25 else '#F49E4C' if other_limit < max_other_limit * 0.50 else '#4FBA74'}")

    def update_total_month_expense():
        self.ui.d_expense_amount.setText(f"{self.manager.get_total_expense_of_this_month():,.2f} THB")

    def update_month_to_date_expense():
        this_month_expense = self.manager.get_total_expense_of_this_month()
        last_month_expense = self.manager.get_total_expense_period(datetime(self.current_date.year, self.current_date.month - 1, 1), datetime(self.current_date.year, self.current_date.month-1, self.current_date.day))
        percentage = this_month_expense / 1 if last_month_expense == 0 else last_month_expense * 100
        
        self.ui.mtdPercentagevaluelabel.setText(f"{percentage: .2f}")
        self.ui.mtdArrowindicator.setText("arrow-up" if this_month_expense > last_month_expense else "arrow-down")
        self.ui.monthtodateframe.setStyleSheet(f"QLabel {{ color: {'#B3625A' if this_month_expense > last_month_expense else '#4FBA74'} }}")

    def handleAccountNumberVisibility():
        self.account_number_visibility = not self.account_number_visibility
        if self.account_number_visibility:
            self.ui.accountNumberlabel.setText(self.manager.get_account_number_visible())
            self.ui.accountNumberlabelDT.setText(self.manager.get_account_number_visible())
        else:
            self.ui.accountNumberlabel.setText(self.manager.get_account_number_non_visible())
            self.ui.accountNumberlabelDT.setText(self.manager.get_account_number_non_visible())

    def style_sheet_color_limit(category: str) -> str:
        limit = self.manager.calculate_daily_limit(category)
        daily_limit = self.manager.get_max_daily_limit(category)
        qss = f"""
        QFrame {{
            background-color: {'rgba(171, 52, 40, 51)' if limit < daily_limit * 0.25 else 'rgb(255, 244, 234)' if limit < daily_limit * 0.50 else 'rgba(40, 171, 52, 51)'};
            border-radius: 5px;
        }}
        QLabel {{
            background-color: transparent;
            color: {'#B3625A' if limit < daily_limit * 0.25 else '#F49E4C' if limit < daily_limit * 0.50 else '#4FBA74'};
        }}
        """
        return qss
    
    def update_total_savings():
        self.ui.d_saving_amount.setText(f"{self.manager.get_total_income_of_this_month():,.2f} THB")

# ================================== Budget Planner ==================================

    def setupBudget():
        self.limit_ui = self.get_all_children_in_frame_and_map_to_strings(self.ui.planYourBudgetFrame, QLineEdit, LIMIT_LABEL)
        self.set_line_edits_read_only()
        self.update_limit_labels()
        self.ui.planEditButton.clicked.connect(self.enable_limits_edit)
        for ui in self.limit_ui.values():
            ui.textChanged.connect(self.update_total_limit)
        self.setupRoundProgressBars()

    def update_limit_labels():
        self.limits = self.manager.get_limits()
        self.ui.averageIncomeLineEdit.setText(str(float(self.manager.get_average_income())))
        # set line edit texts of limits
        for limit, ui in self.limit_ui.items():
            ui.setText(str(self.limits[limit] * 100))
        self.ui.planTotalLineEdit.setText(str(sum(self.limits.values()) * 100))
        if self.limits["saving"] == 0:
            self.ui.budgetAmountLabel.setText(str(float(self.manager.get_average_income())))
        else:
            self.ui.budgetAmountLabel.setText(str(float(self.manager.get_average_income()) - (float(self.manager.get_average_income()) * self.limits["saving"] / 100)))

    def set_line_edits_read_only():
        for ui in self.limit_ui.values():
            ui.setReadOnly(True)
        self.ui.averageIncomeLineEdit.setReadOnly(True)

    def toggle_edit_mode(enable_editing: bool):
        # Toggle editing mode for all limit UI elements
        for ui in self.limit_ui.values():
            ui.setReadOnly(not enable_editing)
        self.ui.averageIncomeLineEdit.setReadOnly(not enable_editing)

        # Change button text and style
        if enable_editing:
            self.ui.planEditButton.setText("Save")
            self.ui.planEditButton.setStyleSheet("background-color: #4FBA74; color: white;")
            self.ui.planEditButton.clicked.disconnect()
            self.ui.planEditButton.clicked.connect(self.save_limits_setting)
        else:
            self.ui.planEditButton.setText("Edit")
            self.ui.planEditButton.setStyleSheet("background-color: #FFF4EA; color: #F49E4C;")
            self.ui.planEditButton.clicked.disconnect()
            self.ui.planEditButton.clicked.connect(self.enable_limits_edit)

    def enable_limits_edit():
        if self.manager.getParentalControl():
            self.nagivateToPin("Enter your Parental PIN")
            self.ui.pinLineEdit.textChanged.connect(self.handleEditBudgetPinPC)
        else:
            self.toggle_edit_mode(True)

    def handleEditBudgetPinPC():
        if len(self.ui.pinLineEdit.text()) <= 6 and len(self.ui.pinLineEdit.text()) > 0:
            self.pin_labels[len(self.ui.pinLineEdit.text())-1].setStyleSheet("background-image: url(:/images/image/pin_dot.svg); background-repeat: no-repeat;")
        if len(self.ui.pinLineEdit.text()) == 6:
            pin = self.ui.pinLineEdit.text() + self.__salt
            hash_object = hashlib.sha256(pin.encode())
            pin = hash_object.hexdigest()
            if self.manager.checkPin(pin):
                self.ui.pinLineEdit.textChanged.disconnect()
                self.toggle_edit_mode(True)
                self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
            else:
                self.ui.pinErrorLabel.setText("Incorrect pin")
                self.resetPIN()

    def save_limits_setting():
        if self.check_total_limit():
            # Disable editing
            self.toggle_edit_mode(False)
            
            # Save limits
            self.limits_temp = {limit_name: float(ui.text()) / 100 for limit_name, ui in self.limit_ui.items()}
            self.manager.save_limits_and_income(self.limits_temp, float(self.ui.averageIncomeLineEdit.text()))
            self.update_limit_labels()
            self.update_window()
            self.updateRoundProgressBars()
            self.ui.planTotalErrorLabel.setText("")
        else:
            self.ui.planTotalErrorLabel.setText("Total limit is not 100%")

    def update_total_limit():
        self.ui.planTotalLineEdit.setText(str(sum([float(ui.text()) for ui in self.limit_ui.values()])))

    def check_total_limit() -> bool:
        return float(self.ui.planTotalLineEdit.text()) == 100.0
    
    def setupRoundProgressBars():     
        self.roundprogressbars = []
        self.progressbars_container = self.get_all_children_in_frame_and_map_to_strings(self.ui.plan_budget_all_progresses, QFrame, LIMIT_LABEL)
        self.progressbars_label = self.get_all_children_in_frame_and_map_to_strings(self.ui.plan_budget_all_progresses, QLabel, LIMIT_LABEL)
        for category, ui in self.progressbars_container.items():
            self.roundprogressbar = roundProgressBar(self, category)
            self.roundprogressbar.setObjectName(category + "ProgressBar")
            
            item = ui.layout().itemAt(0)
            if item:
                item.widget().deleteLater()
            
            ui.layout().addWidget(self.roundprogressbar)
            self.roundprogressbar.update_value(self.check_if_limit_is_zero(self.roundprogressbar, category))
            self.progressbars_label[category].setText(str(int(self.cal_used_monthly_limit_category(category) * 100)) + "%")
            self.roundprogressbars.append(self.roundprogressbar)

    def updateRoundProgressBars():
        for progressbar in self.roundprogressbars:
            self.check_if_limit_is_zero(progressbar, progressbar.get_category())
            progressbar.update_value(self.cal_used_monthly_limit_category(progressbar.get_category()))
            self.progressbars_label[progressbar.get_category()].setText(str(int(self.cal_used_monthly_limit_category(progressbar.get_category()) * 100)) + "%")

    def check_if_limit_is_zero(progressbar: roundProgressBar, category: str) -> float:
        percent_in_fraction = self.cal_used_monthly_limit_category(category)
        if percent_in_fraction == 0:
            progressbar.set_gray_color(True)
        else:
            progressbar.set_gray_color(False)
        return percent_in_fraction

    def cal_used_monthly_limit_category(category: str):
        if self.manager.get_max_monthly_limit(category) == 0:
            return 0
        return round(self.manager.calculate_monthly_limit(category)/self.manager.get_max_monthly_limit(category), 2)

# ================================== Direct Transfer ==================================

    def setupTransferPage():
        self.selectable_transfer_type = self.get_all_children_in_frame_and_map_to_strings(self.ui.transfertypeframe, QPushButton, TRANSFER_TYPE_LABEL)
        for transfer_type, ui in self.selectable_transfer_type.items():
            ui.clicked.connect(lambda checked=False, transfer_type=transfer_type: self.update_type_selected(transfer_type))
        self.update_type_selected(self.transfer_type_selected)

    def update_type_selected(category: str):
        for transfer_type, ui in self.selectable_transfer_type.items():
            if transfer_type == category:
                self.transfer_type_selected = category
                ui.setStyleSheet("color: #F49E4C")
            else:
                ui.setStyleSheet("color: #C7C7C7")
        
        self.ui.dt_expense_amount.setText(f"{self.manager.calculate_daily_limit(category):,.2f} THB" if not category in ["return", "lend"] else "INF THB" if category == "return" else "-INF THB")

    def handleTransfer():
        accountID = self.ui.accountNumberLineEditDT.text()
        amount = self.ui.amountToTransferLineEditDT.text()
        accountIsValid = self.manager.accountNumberIsValid(accountID)
        amountIsValid = self.amountIsValid(amount)
        if not accountIsValid:
            self.ui.accountNumberTransferErrorLabel.setText("Account number is invalid")
        if accountIsValid and amountIsValid:
            self.ui.accountNumberTransferErrorLabel.setText("")
            transaction, transactionID = self.manager.handleTransfer(accountID, float(amount), self.transfer_type_selected)
            print(transaction, transactionID)
            if transaction: # if not over limit and not over balance
                self.nagivateToPin("Enter your PIN")
                self.ui.pinLineEdit.textChanged.connect(lambda: self.handlePinTransfer(accountID, float(amount), transaction, transactionID))
        self.update_window()
        
    def amountIsValid(amount: str) -> bool:
        try:
            amount = float(amount)
            if amount > 0:
                self.ui.amountTransferErrorLabel.setText("")
                return True
            else:
                self.ui.amountTransferErrorLabel.setText("Amount must be greater than 0")
                return False
        except ValueError:
            self.ui.amountTransferErrorLabel.setText("Invalid amount")
            return False
        
    def nagivateToPin(message: str="Enter your PIN"): 
        self.ui.pinLabel.setText(message)
        self.ui.stackedWidget_2.setCurrentIndex(self.page["pin"])
        self.ui.pinErrorLabel.setText("")
        self.resetPIN()

    def handlePinTransfer(accountID: str, amount: float, transaction: Transaction, transactionID: str):
        if len(self.ui.pinLineEdit.text()) <= 6 and len(self.ui.pinLineEdit.text()) > 0:
            self.pin_labels[len(self.ui.pinLineEdit.text())-1].setStyleSheet("background-image: url(:/images/image/pin_dot.svg); background-repeat: no-repeat;")

        if len(self.ui.pinLineEdit.text()) == 6:
            pin = self.ui.pinLineEdit.text() + self.__salt
            hash_object = hashlib.sha256(pin.encode())
            pin = hash_object.hexdigest()
            if self.manager.checkPin(pin):
                self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
                self.transfer(accountID, amount, transaction, transactionID)
                self.ui.pinLineEdit.textChanged.disconnect()
            else:
                self.ui.pinErrorLabel.setText("Incorrect pin")
                self.resetPIN()

    def addNumberToPin(num: str):
        self.ui.pinLineEdit.setText(self.ui.pinLineEdit.text() + num)

    def deletePin():
        if len(self.ui.pinLineEdit.text()) > 0:
            self.pin_labels[len(self.ui.pinLineEdit.text())-1].setStyleSheet("background-image: url(:/images/image/pin_no_dot.svg); background-repeat: no-repeat;")
            self.ui.pinLineEdit.setText(self.ui.pinLineEdit.text()[:-1])

    def resetPIN():
        self.ui.pinLineEdit.setText("")
        for i in range(6):
            self.pin_labels[i].setStyleSheet("background-image: url(:/images/image/pin_no_dot.svg); background-repeat: no-repeat;")
    def transfer(accountID: str, amount: float, transaction: Transaction, transactionID: str):
        self.manager.transfer(accountID, float(amount), transaction, transactionID)
        self.update_window()
        self.updateRoundProgressBars()
        self.ui.accountNumberLineEditDT.setText("")
        self.ui.amountToTransferLineEditDT.setText("")
        print("Transfer success")
        self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"])


# ================================== History page ==================================
    
    def update_history_page(history_type: str = "all"):
        for i in reversed(range(self.ui.transaction_history_frame.layout().count())):
            item = self.ui.transaction_history_frame.layout().itemAt(i)
            if item.widget():
                item.widget().deleteLater()
            elif item.spacerItem():
                self.ui.transaction_history_frame.layout().takeAt(i)
        
        old_date = None
        for transaction in self.manager.getTransactionsHistory():
            transaction_date = transaction.date.strftime("%d/%m/%Y")
            
            if old_date == None or old_date.strftime("%d/%m/%Y") != transaction_date:
                old_date = transaction.date
                date_label = QLabel(self.ui.transaction_history_frame)
                date_label.setObjectName(transaction_date)
                date_label.setText(transaction_date)
                date_label.setStyleSheet("color: #A1A5AD; font-size: 16px; font-weight: bold; font-family: Montserrat;")
                self.ui.transaction_history_frame.layout().addWidget(date_label)
            
            transaction_element = TransactionFrame(self.ui.transaction_history_frame, transaction, self.manager.get_account_number())
            transaction_element.clicked.connect(self.handleTransactionDetail)
            
            if history_type == "expense":
                if transaction.sender.getID() == self.manager.get_account_number():
                    self.ui.transaction_history_frame.layout().addWidget(transaction_element)
            elif history_type == "income":
                if transaction.recipient.getID() == self.manager.get_account_number():
                    self.ui.transaction_history_frame.layout().addWidget(transaction_element)
            else:
                self.ui.transaction_history_frame.layout().addWidget(transaction_element)
            print(transaction)
        self.ui.transaction_history_frame.layout().addStretch()
    
    @Slot(Transaction)
    def handleTransactionDetail(transaction: Transaction):
        self.ui.stackedWidget.setCurrentIndex(self.page["transactionInfo"])
        self.ui.sender_label.setText(transaction.sender.getName())
        self.ui.reciever_label.setText(transaction.recipient.getName())
        self.ui.date_time_label.setText(transaction.date.strftime("%d/%m/%Y %H:%M:%S"))
        self.ui.transaction_type_label.setText(transaction.__class__.__name__.upper())
        self.ui.total_amount_label.setText(f"{transaction.amount:,.2f}")
        self.ui.spend_limit_label.setText(f"{transaction.spendlimit:,.2f}")
        self.ui.saved_amount_label.setText(f"{transaction.saved:,.2f}")
        self.ui.spend_amount_label.setText(f"{transaction.spend:,.2f}")
        
        for i in reversed(range(self.ui.transactionDetailframe.layout().count())):
            item = self.ui.transactionDetailframe.layout().itemAt(i)
            if item.widget():
                item.widget().deleteLater()
            elif item.spacerItem():
                self.ui.transactionDetailframe.layout().takeAt(i)
        
        for item in transaction.itemList:
            item_frame = TransactionItem(self.ui.transactionDetailframe, item)
            self.ui.transactionDetailframe.layout().addWidget(item_frame)

#=================================== My QR Code ==================================
            
    def createMyQRcode():
        AccountID = self.manager.get_account_number()
        myQRcode = qrcode.make(AccountID)
        pil_myQr = myQRcode.get_image()
        self.pil_myQr = self.add_infomation_to_myQRcode(myQRcode, "Owner: "+self.manager.getName()+"\nAccount ID: "+ self.manager.get_account_number_non_visible())
        pixmap = pil_myQr.toqpixmap()
        self.ui.myQRcodeLabel.setPixmap(pixmap)

    def saveMyQRcode():
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("Image files (*.png, *.jpg, *.jpeg, *.xpm, *.bmp)")
        file_dialog.setDefaultSuffix("png")
        file_dialog.setWindowTitle("Save My QR Code")
        file_dialog.selectFile("MyQRCode.png")
        file_dialog.setDirectory(str(Path.home()))

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            self.pil_myQr.save(file_path, "PNG")


    def add_infomation_to_myQRcode(qr_code_image: Any, additional_info: str) -> Image:
        # Create a new image with the QR code and additional information
        new_image = Image.new('RGB', (max(qr_code_image.size[0], 200), qr_code_image.size[1] + 50), color="#4FBA74")
        new_image.paste(qr_code_image, (0, 0))

        # Draw additional information below the QR code
        draw = ImageDraw.Draw(new_image)
        font = ImageFont.truetype("otfs/Montserrat-Regular.ttf", 16)

        # Get the bounding box of the text
        text_bbox = draw.textbbox(((new_image.width - qr_code_image.size[0]) // 2, qr_code_image.size[1]),additional_info, font=font)

        # Draw the text using the bounding box
        draw.text(text_bbox[:2], additional_info, font=font, fill='White')

        return new_image


# ================================== Parental Control ==================================
        
    def pcToggleSetup():
        item = self.ui.pcPCMSwitchframe.layout().itemAt(2)
        if item:
            item.widget().deleteLater()
        
        self.parental_control_toggle = ToggleSwitch(width=64)
        self.ui.pcPCMSwitchframe.layout().addWidget(self.parental_control_toggle)
        self.parental_control_toggle.setObjectName("parentalControlToggle")
        self.parental_control_toggle.setChecked(self.manager.getParentalControl())
        self.parental_control_toggle.stateChanged.connect(self.toggleParentalControl)
        # print("at main", self.parental_control_toggle.width(), self.parental_control_toggle.height(), self.parental_control_toggle.parentWidget().width(), self.parental_control_toggle.parentWidget().height())

        self.allow_over_budget_toggle = ToggleSwitch(width=64)
        self.allow_over_budget_toggle.setObjectName("allowOverBudgetToggle")
        self.allow_over_budget_toggle.setEnabled(not self.manager.getParentalControl())
        self.allow_over_budget_toggle.setChecked(self.manager.getAllowOverBudget())
        self.allow_over_budget_toggle.stateChanged.connect(self.toggleAllowOverBudget)
        self.ui.pcAOBSwitchframe.layout().addWidget(self.allow_over_budget_toggle)

    def toggleParentalControl(): # disable or enable the button
        if self.manager.getParentalControl():
            self.nagivateToPin("Enter your Parental PIN")
            self.ui.pinLineEdit.textChanged.connect(self.handlePinPC)
        else:
            self.nagivateToPin("Create your Parental PIN")
            self.ui.pinLineEdit.textChanged.connect(self.handleCreatePinPC)

    def toggleAllowOverBudget():
        self.manager.toggleAllowOverBudget()

    def handlePinPC():
        if len(self.ui.pinLineEdit.text()) <= 6 and len(self.ui.pinLineEdit.text()) > 0:
            self.pin_labels[len(self.ui.pinLineEdit.text())-1].setStyleSheet("background-image: url(:/images/image/pin_dot.svg); background-repeat: no-repeat;")
        if len(self.ui.pinLineEdit.text()) == 6:
            pin = self.ui.pinLineEdit.text() + self.__salt
            hash_object = hashlib.sha256(pin.encode())
            pin = hash_object.hexdigest()
            if self.manager.checkPinPC(pin):
                self.ui.pinLineEdit.textChanged.disconnect()
                self.manager.toggleParentalControl()
                self.allow_over_budget_toggle.setEnabled(not self.manager.getParentalControl())
                self.allow_over_budget_toggle.setChecked(False)
                self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
            else:
                self.ui.pinErrorLabel.setText("Incorrect pin")
                self.resetPIN()

    def handleCreatePinPC():
        if len(self.ui.pinLineEdit.text()) <= 6 and len(self.ui.pinLineEdit.text()) > 0:
            self.pin_labels[len(self.ui.pinLineEdit.text())-1].setStyleSheet("background-image: url(:/images/image/pin_dot.svg); background-repeat: no-repeat;")
        if len(self.ui.pinLineEdit.text()) == 6:
            pin = self.ui.pinLineEdit.text() + self.__salt
            hash_object = hashlib.sha256(pin.encode())
            pin = hash_object.hexdigest()
            self.manager.setPinPC(pin)
            self.ui.pinLineEdit.textChanged.disconnect()
            # toggle the parental control
            self.manager.toggleParentalControl()
            self.allow_over_budget_toggle.setEnabled(not self.manager.getParentalControl())
            self.allow_over_budget_toggle.setChecked(False)
            self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
    
# ================================== Graph ==================================
    
    def setupGraph():
        #set date to today
        self.ui.dateEdit.setDate(self.current_date)
        # default check all radio button

        self.ui.dayradioButton.setChecked(True)
        self.ui.monthradioButton.setChecked(False)
        self.ui.yearradioButton.setChecked(False)

        self.ui.lineradioButton.setChecked(True)
        self.ui.barradioButton.setChecked(False)

        self.ui.allradioButton.setChecked(True)
        self.ui.incomeradioButton.setChecked(False)
        self.ui.expenseradioButton.setChecked(False)

        self.ui.total_expense_amount.setText("0")
        self.ui.total_income_amount.setText("0")
        self.ui.overall_amount.setText("0")

        # add layout to canvasframe
        self.ui.canvasframe.setLayout(QVBoxLayout(self.ui.canvasframe))
        self.ax, self.fig = plt.subplots()
        

    def handleNavigationToGraph():
        self.ui.stackedWidget.setCurrentIndex(self.page["graph"])
        self.updateGraph()

    def radio_button_state_changed():
        sender = self.sender()  # Get the radio button that triggered the signal
        if sender.isChecked():
            self.updateGraph()

    def updateGraph():
        # Check remove canvas from layout
        for i in reversed(range(self.ui.canvasframe.layout().count())):
            item = self.ui.canvasframe.layout().itemAt(i)
            if item.widget():
                item.widget().deleteLater()
            elif item.spacerItem():
                self.ui.canvasframe.layout().takeAt(i)
        
        #get date
        # self.ui.graphview.clear()
        date = self.ui.dateEdit.date()
        # get type
        type = ""
        if self.ui.dayradioButton.isChecked():
            type = "day"
        elif self.ui.monthradioButton.isChecked():
            type = "month"
        elif self.ui.yearradioButton.isChecked():
            type = "year"
        # get graph type
        graph_type = ""
        if self.ui.lineradioButton.isChecked():
            graph_type = "line"
        elif self.ui.barradioButton.isChecked():
            graph_type = "bar"
        # get history type
        history_type = ""
        if self.ui.allradioButton.isChecked():
            history_type = "all"
        elif self.ui.incomeradioButton.isChecked():
            history_type = "income"
        elif self.ui.expenseradioButton.isChecked():
            history_type = "expense"

        data = self.drawGraph(date, type, graph_type, history_type)
        self.ui.total_expense_amount.setText(f"{data['total_expense']:,.2f}")
        self.ui.total_income_amount.setText(f"{data['total_income']:,.2f}")
        self.ui.overall_amount.setText(f"{data['total_income'] - data['total_expense']:,.2f}")
        if data['total_income'] - data['total_expense'] < 0:
            self.ui.overall_amount.setStyleSheet("color: #B3625A")
            self.ui.overall_THBlabel.setStyleSheet("color: #B3625A")
        else:
            self.ui.overall_amount.setStyleSheet("color: #4FBA74")
            self.ui.overall_THBlabel.setStyleSheet("color: #4FBA74")

    def drawGraph(date: datetime, type: str, graph_type: str, history_type: str):
        self.ax.clear()
        self.fig.clear()
        data = self.manager.getGraphData(date, type)
        """ data = {
            "income": {income_date: income_amount},
            "expense": {expense_date: expense_amount}
            "total_income": total_income,
            "total_expense": total_expense,
        }
        """
        print(data)
        income_data = data["income"]
        expense_data = data["expense"]

        # Extract x and y from both dictionaries
        x = list(income_data.keys())
        y1 = list(income_data.values())
        y2 = list(expense_data.values())

        # Create a figure and axis object
        self.fig, self.ax = plt.subplots()

        # Plot your data
        if graph_type == "line":
            if history_type == "all":
                self.ax.plot(x, y1, label='Income', color="green")
                self.ax.plot(x, y2, label='Expense', color="red")
            elif history_type == "income":
                self.ax.plot(x, y1, label='Income', color="green")
            elif history_type == "expense":
                self.ax.plot(x, y2, label='Expense', color="red")
        if graph_type == "bar":
            if history_type == "all":
                self.ax.bar(x, y1, width=0.4, label='Income', color="green")
                self.ax.bar([i + 0.4 for i in range(len(x))], y2, width=0.4, label='Expense', color="red")
            elif history_type == "income":
                self.ax.bar(x, y1, width=0.4, label='Income', color="green")
            elif history_type == "expense":
                self.ax.bar(x, y2, width=0.4, label='Income', color="red")

        #Customize plot
        self.ax.set_ylabel('Baht', fontsize=9)
        self.ax.legend(fontsize=9)
        self.ax.set_ylim(0)
        self.ax.set_title(f'Summary: {history_type}', fontsize=9)
        
        self.ax.tick_params(axis='x', rotation=90)
        self.ax.tick_params(axis='both', labelsize=5)
        # plot the graph in the graph view
        canvas = FigureCanvas(self.fig)
        # add the canvas to the layout
        self.ui.canvasframe.layout().addWidget(canvas)
        return data


# ================================== Others ==================================

    def setupOthersPage():
        self.ui.others_name_label.setText(self.manager.getName())
        self.ui.others_email_label.setText(self.manager.getEmail())
        


# ================================== Camera ==================================

    def start_camera_feed():
        # Open the default camera (index 0)
        self.capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        ret, frame = self.capture.read()
        if not ret:
            self.capture = cv2.VideoCapture(0)
        # Set the width of the captured frame to 1200 pixels
        # self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.ui.camera_label.width())
        # Start a timer that triggers the update_camera_feed method at regular intervals
        self.camera_timer = QTimer(self)
        self.camera_timer.timeout.connect(self.update_camera_feed)
        # Start the timer with a timeout value of 50 millisecond (adjust as needed)
        self.camera_timer.start(30)

    @Slot()
    def update_camera_feed():
        # Read a frame from the camera
        ret, frame = self.capture.read()
        # Check if the frame was captured successfully
        if not ret:
            print("Failed to capture frame")
            return
        
        frame = self.scale_image_by_height(frame, self.ui.camera_label.height())
        frame = self.center_crop(frame, (self.ui.camera_label.width(), self.ui.camera_label.height()))
        
        # Detect a QR code from the frame
        accountID, bbox, _ = self.detector.detectAndDecode(frame)
        # Check if a QR code is detected
        if accountID:
            # Perform any actions you want with the detected QR code data
            print("QR Code detected:", accountID)
            # Disconnect the timer signal, release the camera, and handle the detected QR code
            self.camera_timer.timeout.disconnect()
            self.capture.release()
            self.handleRedirectFromScanQRCodeToDirectTransfer(accountID)
            return
        # Check if the current page is not the page where QR code scanning is expected
        elif self.ui.stackedWidget.currentIndex() != self.page["scanqrcode"]:
            # Disconnect the timer signal and release the camera
            self.camera_timer.timeout.disconnect()
            self.capture.release()
            return

        # Convert the OpenCV frame to QImage
        height, width, _ = frame.shape
        # Create a deep copy of the frame to ensure continuous memory
        frame_copy = frame.copy()
        qimg = QImage(frame_copy.data, width, height, frame_copy.strides[0], QImage.Format_BGR888)

        # Convert QImage to QPixmap for displaying
        pixmap = QPixmap.fromImage(qimg)

        # Update the QLabel with the new QPixmap
        self.ui.camera_label.setPixmap(pixmap)
    
    def center_crop(img: np.ndarray, dim: Tuple[int, int]) -> np.ndarray:
        """Returns center cropped image
        Args:
        img: image to be center cropped
        dim: dimensions (width, height) to be cropped
        """
        width, height = img.shape[1], img.shape[0]

        # process crop width and height for max available dimension
        crop_width = dim[0] if dim[0]<img.shape[1] else img.shape[1]
        crop_height = dim[1] if dim[1]<img.shape[0] else img.shape[0] 
        mid_x, mid_y = int(width/2), int(height/2)
        cw2, ch2 = int(crop_width/2), int(crop_height/2) 
        crop_img = img[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]
        return crop_img

    def scale_image_by_height(self, img: np.ndarray, height: int, factor: float = 1):
        """Returns resize image by scale factor.
        This helps to retain resolution ratio while resizing.
        Args:
        img: image to be scaled
        factor: scale factor to resize
        """
        ratio = img.shape[1] / img.shape[0]
        return cv2.resize(img, (int(height * ratio * factor), height * factor))
    
    def update_frame():
        ret, frame = self.camera.read()
        if ret:

            frame = self.scale_image_by_height(frame, self.ui.camera_label_4.height())
            frame = self.center_crop(frame, (self.ui.camera_label_4.width(), self.ui.camera_label_4.height()))
            # Convert OpenCV frame to QImage
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # Rezise the QImage to fit the QLabel dimensions
            if w != self.ui.camera_label_4.width() or h != self.ui.camera_label_4.height():
                qt_image = qt_image.scaled(self.ui.camera_label_4.width(), self.ui.camera_label_4.height())

            # Update QLabel with the QImage
            self.ui.camera_label_4.setPixmap(QPixmap.fromImage(qt_image))

    def capture_image():
        ret, frame = self.camera.read()
        if ret:
            # Save the captured frame
            cv2.imwrite("captured_image.jpg", frame)
            print("Image captured.")
            # Release the camera and stop the timer
            self.camera.release()
            self.timer.stop()
            
            #get the imgae path absolute path
            img_path = os.path.abspath("captured_image.jpg")
            self.file_selected(img_path)
            
            # Delete the captured image
            os.remove(img_path)
            # Navigate to the page where the captured image will be displayed
            self.ui.stackedWidget.setCurrentIndex(self.page["addbill"])

    def closeEvent(event: QCloseEvent):
        # Release the camera when closing the application
        self.camera.release()
        event.accept()

    
# ================================== Add Bill ==================================

    def addSingleBill(name: str='', amount:int=0):
        self.ui.single_bill_frame.layout().addWidget(BillFrame(self.ui.single_bill_frame, name, amount))
    
    def addBillFromFile():
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Image files (*.png *.jpg *.jpeg *.xpm *.bmp)")
        file_dialog.setWindowTitle("Select Image")
        file_dialog.fileSelected.connect(self.file_selected)
        file_dialog.exec()

    def file_selected(file_path: str):
        # Display the selected file path
        # img = Image.open(file_path)
        # text = pytesseract.image_to_string(img, lang='eng+tha')
        # print(text)
        url = "https://ocr.asprise.com/api/v1/receipt"
        res = requests.post(
            url,
            data={    
                'api_key': 'TEST',
                'recognizer': 'auto',
                'ref_no': 'oct_python_123'
            },
            files={
                'file': open(file_path, 'rb')
            }
        )
        data = res.json()
        # with open ("test.json", "r") as f:
        #     data = json.load(f)
            
        for data in data['receipts']:
            for item in data['items']:
                self.addSingleBill(item['description'], float(item['amount']))

    def finishAddBill():
        billName = self.ui.billName.text()
        
        items = []
        total = 0
        for item in self.ui.single_bill_frame.children():
            if isinstance(item, BillFrame):
                items.append(item.getValues())
                total += float(item.getValues()[1])
        
        if self.manager.addBill(items, total, billName):
            self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"])
            self.update_window()
            for item in self.ui.single_bill_frame.children():
                if isinstance(item, BillFrame):
                    item.deleteLater()
            self.ui.billName.setText("")
        else:
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setWindowTitle("Warning")
            warning.setText("Something Went wrong")
            warning.exec()
                
    def handleNaviationToCaptureReceipt():
        self.ui.stackedWidget.setCurrentIndex(self.page["captureReceipt"])
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)
        
        self.camera = cv2.VideoCapture(0)
    

# ================================== Event Handling & Helper Functions ==================================
    
    def page_changed_handler():
            if self.ui.accountNumberLineEditDT != "":
                self.ui.accountNumberLineEditDT.setText("")
                self.ui.accountNumberLineEditDT.setReadOnly(False)
            if self.ui.stackedWidget.currentIndex() == self.page["budgetplanner"]:
                for progress_bar in self.roundprogressbars:
                    progress_bar.animate_from_zero()

    def page_changed_handler_2():
        if self.ui.loginError.text() != "":
            self.ui.loginError.setText("")
        if self.ui.registerConfirmPasswordError.text() != "":
            self.ui.registerConfirmPasswordError.setText("")
   
    def handleNavigationToScanQRCode():
        self.ui.stackedWidget.setCurrentIndex(self.page["scanqrcode"])
        self.start_camera_feed()

    def handleRedirectFromScanQRCodeToDirectTransfer(accountID: str):
        self.ui.stackedWidget.setCurrentIndex(self.page["directtransfer"])
        self.ui.accountNumberLineEditDT.setReadOnly(True)
        self.ui.accountNumberLineEditDT.setText(accountID)

    def get_all_child_type_in_frame(frame: QFrame, QType: type) -> list:
        line_edits = []

        def traverse_children(widget):
            for child in widget.children():
                if type(child) == QType and any(name in child.objectName() for name in LOOK_UP_OBJ_NAME):
                    line_edits.append(child)
                elif isinstance(child, (QWidget, QLayout)):
                    traverse_children(child)
                elif isinstance(child, QLayoutItem):
                    item_widget = child.widget()
                    if item_widget:
                        traverse_children(item_widget)

        traverse_children(frame)
        return line_edits
    
    def map_child_to_string(line_edits: QLineEdit, child_name: str) -> dict:
        limit_ui_mapping = {}

        for obj in line_edits:
            obj_name = obj.objectName().lower()
            if "miscellaneous" in obj_name:
                limit_ui_mapping["others"] = obj
            else:
                for name in child_name:  # Use a copy of child_name to allow removal during iteration
                    if name in obj_name:
                        limit_ui_mapping[name] = obj
                        # child_name_copy.remove(name)  # Remove the matched item from child_name
                        break

        return limit_ui_mapping
    
    def get_all_children_in_frame_and_map_to_strings(self, frame: QFrame, QType: type, child_name: str) -> dict:
        line_edits = self.get_all_child_type_in_frame(frame, QType)
        return self.map_child_to_string(line_edits, child_name)
    
    def handleLogout():
        with open(USER_CACHE_FILE, "wb") as f:
            user_cache = ""
            pickle.dump(user_cache, f)
        self.ui.stackedWidget_2.setCurrentIndex(self.page["login"])
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = WalletManager()
    main = MainWindow(manager)
    main.show()
    sys.exit(app.exec())