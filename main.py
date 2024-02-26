import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFrame
from PySide6.QtCore import QSize, QRect, Qt
from PySide6.QtGui import QFont, QFontDatabase, QMouseEvent
from mainwindow import Ui_MainWindow

from pathlib import Path

from obj.walletmanager import WalletManager
from obj.account import Account

import pickle

import ZODB, ZODB.config
import BTrees.OOBTree, transaction

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
    def __init__(self, manager):
        super().__init__()
        self.account_manager = manager
        self.account_number_visibility = False
        # Add fonts in QFontDatabase before setting up the UI
        QFontDatabase.addApplicationFont('otfs/Font Awesome 6 Brands-Regular-400.otf')
        QFontDatabase.addApplicationFont('otfs/Font Awesome 6 Free-Regular-400.otf')
        QFontDatabase.addApplicationFont('otfs/Font Awesome 6 Free-Solid-900.otf')
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.frame_10.installEventFilter(self)
        
        self.ui.eyeButton.clicked.connect(self.handleAccountNumberVisibility)

    def eventFilter(self, obj, event):
        if type(event) == QMouseEvent and obj == self.ui.frame_10 and event.button() == Qt.MouseButton.LeftButton:
            self.customPressEvent(event)
            return True
        return super().eventFilter(obj, event)

    def customPressEvent(self, event):
        print("Frame clicked!")
    
    def handleAccountNumberVisibility(self):
        self.account_number_visibility = not self.account_number_visibility
        if self.account_number_visibility:
            self.ui.accountNumberlabel.setText(str(self.account_manager.account.ID))
        else:
            self.ui.accountNumberlabel.setText("*" * 9 + str(self.account_manager.account.ID)[-4:])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = WalletManager(root.accounts[123456789])
    print(root.accounts[123456789].ID)
    main = MainWindow(manager)
    main.show()
    sys.exit(app.exec())