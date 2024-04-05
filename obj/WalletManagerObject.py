from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFrame, QTreeWidget, QTreeWidgetItem, QLineEdit, QLayoutItem, QLayout, QHBoxLayout, QLineEdit
from PySide6.QtCore import QSize, QRect, Qt, Slot, QTimer, Signal
from PySide6.QtGui import QFont, QFontDatabase, QMouseEvent, QImage, QPixmap, QIntValidator

class TransactionFrame(QFrame):
    clicked = Signal()
    def __init__(self, parent, transaction, self_account_number):
        super().__init__(parent)
        self.transaction = transaction
        self.self_account_number = self_account_number
        self.setStyleSheet("font-size: 16px; font-family: 'Montserrat';")
        self.initUI()
        
    def checkExpense(self):
        return self.transaction.sender.getID() == self.self_account_number

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.clicked.emit()
        return super().mousePressEvent(event)
    
    def initUI(self):
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
    def __init__(self, parent, name = "", amount = 0):
        super().__init__(parent)
        self.name = name
        self.amount = amount
        self.setStyleSheet("font-size: 16px; font-family: 'Montserrat'; background-color: #F5F5F5; border-radius: 10px; padding: 10px;")
        self.initUI()
    
    def initUI(self):
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
    
    def delete(self):
        self.deleteLater()
    
    def getValues(self):
        return [self.nameInput.text(), self.amountInput.text()]
        
class TransactionInfo(QFrame):
    def __init__(self, parent, transaction):
        super().__init__(parent)
        self.transaction = transaction
        self.setStyleSheet("font-size: 16px; font-family: 'Montserrat';")
        self.initUI()
        
    def initUI(self):
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName("frame")
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        self.sender_label = QLabel(self)
        self.sender_label.setText(self.transaction.sender.getName())
        self.sender_label.setAlignment(Qt.AlignBottom)
        self.layout.addWidget(self.sender_label)
        
        self.receiver_label = QLabel(self)
        self.receiver_label.setText(self.transaction.recipient.getName())
        self.receiver_label.setAlignment(Qt.AlignBottom)
        self.layout.addWidget(self.receiver_label)
        
        self.amount_label = QLabel(self)
        self.amount_label.setText(str(self.transaction.amount))
        self.amount_label.setAlignment(Qt.AlignBottom)
        self.layout.addWidget(self.amount_label)
        
        self.date_label = QLabel(self)
        self.date_label.setText(self.transaction.date.strftime("%d/%m/%Y"))
        self.date_label.setAlignment(Qt.AlignBottom)
        self.layout.addWidget(self.date_label)
        
        self.time_label = QLabel(self)
        self.time_label.setText(self.transaction.time.strftime("%H:%M"))
        self.time_label.setAlignment(Qt.AlignBottom)
        self.layout.addWidget(self.time_label)
        
        self.description_label = QLabel(self)
        self.description_label.setText(self.transaction.description)
        self.description_label.setAlignment(Qt.AlignBottom)
        self.layout.addWidget(self.description_label)
        
        self.setLayout(self.layout)