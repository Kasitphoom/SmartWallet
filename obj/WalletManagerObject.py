from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFrame, QTreeWidget, QTreeWidgetItem, QLineEdit, QLayoutItem, QLayout, QHBoxLayout
from PySide6.QtCore import QSize, QRect, Qt, Slot, QTimer
from PySide6.QtGui import QFont, QFontDatabase, QMouseEvent, QImage, QPixmap

class TransactionFrame(QFrame):
    def __init__(self, parent, transaction, self_account_number):
        super().__init__(parent)
        self.transaction = transaction
        self.self_account_number = self_account_number
        self.setStyleSheet("font-size: 16px; font-family: 'Montserrat';")
        self.initUI()
        
    def checkExpense(self):
        return self.transaction.sender.getID() == self.self_account_number
    
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
        self.receiver_label.setText(self.transaction.recipient.getName() if self.checkExpense() else self.transaction.sender.getName())
        self.receiver_label.setAlignment(Qt.AlignBottom)
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
        