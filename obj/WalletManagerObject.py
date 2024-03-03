from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFrame, QTreeWidget, QTreeWidgetItem, QLineEdit, QLayoutItem, QLayout, QHBoxLayout
from PySide6.QtCore import QSize, QRect, Qt, Slot, QTimer
from PySide6.QtGui import QFont, QFontDatabase, QMouseEvent, QImage, QPixmap

class TransactionFrame(QFrame):
    def __init__(self, parent, transaction):
        super().__init__(parent)
        self.transaction = transaction
        self.initUI()
    
    def initUI(self):
        self.setGeometry(QRect(0, 0, 300, 100))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName("frame")
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(10)
        self.layout.setObjectName("HorizontalLayout")
        
        self.recipient_label = QLabel(self)
        self.recipient_label.setText(self.transaction.recipient)
        self.layout.addWidget(self.recipient_label)
        
        self.amount_layout = QVBoxLayout()
        self.amount_layout.setObjectName("VerticalLayout")
        self.type = QLabel(self)
        self.type.setText(self.transaction.__class__.__name__.upper())
        self.type.setObjectName("type")
        self.amount_layout.addWidget(self.type)
        self.amount = QLabel(self)
        self.amount.setText(f"${self.transaction.amount}")
        self.amount.setObjectName("amount")
        
        self.thb = QLabel(self)
        self.thb.setText("THB")
        self.thb.setObjectName("thb")
        self.layout.addWidget(self.amount)
        