import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import QSize, QRect
from PySide6.QtGui import QFont, QFontDatabase
from mainwindow import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Add fonts in QFontDatabase before setting up the UI
        QFontDatabase.addApplicationFont('otfs\Font Awesome 6 Brands-Regular-400.otf')
        QFontDatabase.addApplicationFont('otfs\Font Awesome 6 Free-Regular-400.otf')
        QFontDatabase.addApplicationFont('otfs\Font Awesome 6 Free-Solid-900.otf')
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #-----------------Font testing-----------------
        # font_path = 'otfs\Sushi Sushi.ttf'
        # id = QFontDatabase.addApplicationFont(font_path)
        # if id < 0:
        #     print('Failed to load font')
        # families = QFontDatabase.applicationFontFamilies(id)
        # if len(families) > 0:
        #     print(families[0])
        #     print(type(families[0]))
        # button = self.ui.graphButton
        # button.setFont(QFont('Sushi Sushi'))
        #-----------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())