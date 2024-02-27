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
        self.today_date = QtCore.QDate.currentDate()
        self.manager = manager
        self.account_number_visibility = False
        self.calculated_limits = {}
        
        
        
        # Add fonts in QFontDatabase before setting up the UI
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Font Awesome 6 Free-Solid-900.otf").as_posix())
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.frame_10.installEventFilter(self)
        
        self.ui.eyeButton.clicked.connect(self.handleAccountNumberVisibility)
        
        # set text as this format XXX-X-1234-X
        self.ui.accountNumberlabel.setText(self.manager.get_account_number_non_visible())
        
        # set balance
        self.ui.d_balance_amount.setText(self.manager.get_balance() + " THB")
        
        self.update_daily_limit()

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
    
    def update_daily_limit(self):
        self.ui.foodlimitlabel.setText(str(self.manager.calculate_daily_limit("food")))
        self.ui.transportationlimitlabel.setText(str(self.manager.calculate_daily_limit("transport")))
        self.ui.entertainmentlimitlabel.setText(str(self.manager.calculate_daily_limit("entertainment")))
        self.ui.healthcarelimitlabel.setText(str(self.manager.calculate_daily_limit("healthcare")))
        self.ui.label_10.setText(str(self.manager.calculate_daily_limit("others")))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = WalletManager(root.accounts["123456789"])
    main = MainWindow(manager)
    main.show()
    sys.exit(app.exec())