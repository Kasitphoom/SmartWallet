import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFrame, QTreeWidget, QTreeWidgetItem
from PySide6.QtCore import QSize, QRect, Qt
from PySide6.QtGui import QFont, QFontDatabase, QMouseEvent
from mainwindow import Ui_MainWindow

from pathlib import Path

from obj.walletmanager import WalletManager
from obj.account import Account

import pickle

import ZODB, ZODB.config

path = "./db/config.xml"
db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root

USER_CACHE_FILE = Path.absolute(Path(__file__).parent / "cache/user_cache.pkl")

if USER_CACHE_FILE.exists():
    with open(USER_CACHE_FILE, "rb") as f:
        user_cache = pickle.load(f)
else:
    with open(USER_CACHE_FILE, "wb") as f:
        user_cache = {}
        pickle.dump(user_cache, f)

class MainWindow(QMainWindow):
    def __init__(self, manager: WalletManager):
        super().__init__()
        self.manager = manager
        self.account_number_visibility = False
        # Add fonts in QFontDatabase before setting up the UI
        QFontDatabase.addApplicationFont('otfs/Font Awesome 6 Brands-Regular-400.otf')
        QFontDatabase.addApplicationFont('otfs/Font Awesome 6 Free-Regular-400.otf')
        fontID = QFontDatabase.addApplicationFont('otfs/Font Awesome 6 Free-Solid-900.otf')
        QFontDatabase.addApplicationFont('otfs/Sushi Sushi.ttf')
        if fontID < 0:
            print('font not loaded')

        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.frame_12.installEventFilter(self)
        
        self.ui.eyeButton.clicked.connect(self.handleAccountNumberVisibility)
        
        # set text as this format XXX-X-1234-X
        self.ui.accountNumberlabel.setText(self.manager.get_account_number_non_visible())
        
        self.ui.label_10.setFont(QFont("Sushi Sushi", 12))
        
        # set balance
        self.ui.d_balance_amount.setText(self.manager.get_balance() + " THB")
        
        self.update_limit_dashboard()

    def eventFilter(self, obj, event):
        if type(event) == QMouseEvent and obj == self.ui.frame_12 and event.button() == Qt.MouseButton.LeftButton:
            self.customPressEvent(event)
            return True
        return super().eventFilter(obj, event)

    def customPressEvent(self, event):
        print("Frame clicked!")
    
    def handleAccountNumberVisibility(self):
        self.account_number_visibility = not self.account_number_visibility
        if self.account_number_visibility:
            self.ui.accountNumberlabel.setText(self.manager.get_account_number_visible())
        else:
            self.ui.accountNumberlabel.setText(self.manager.get_account_number_non_visible())
    
    def update_limit_dashboard(self):
        self.ui.foodlimitlabel.setText(f"{self.manager.calculate_limit('food')} THB")
        self.ui.transportationlimitlabel.setText(f"{self.manager.calculate_limit('transport')} THB")
        self.ui.entertainmentlimitlabel.setText(f"{self.manager.calculate_limit('entertainment')} THB")
        self.ui.healthcarelimitlabel.setText(f"{self.manager.calculate_limit('healthcare')} THB")
        self.ui.label_10.setText(f"{self.manager.calculate_limit('others')} THB")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = WalletManager(root.accounts["123456789"])
    main = MainWindow(manager)
    main.show()
    sys.exit(app.exec())