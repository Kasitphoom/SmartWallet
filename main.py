import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import QSize, QRect
from PySide6.QtGui import QFont
from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        label = self.findChild(QPushButton, "graphButton")
        customFont = QFont(":./otfs/Font Awesome 6 Free-Solid-900.otf")
        label.setFont(customFont)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())