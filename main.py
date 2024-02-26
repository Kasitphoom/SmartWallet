import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFrame
from PySide6.QtCore import QSize, QRect, Qt
from PySide6.QtGui import QFont, QFontDatabase, QMouseEvent
from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Add fonts in QFontDatabase before setting up the UI
        QFontDatabase.addApplicationFont('otfs/Font Awesome 6 Brands-Regular-400.otf')
        QFontDatabase.addApplicationFont('otfs/Font Awesome 6 Free-Regular-400.otf')
        QFontDatabase.addApplicationFont('otfs/Font Awesome 6 Free-Solid-900.otf')
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.frame_10.installEventFilter(self)

    def eventFilter(self, obj, event):
        if type(event) == QMouseEvent and obj == self.ui.frame_10 and event.button() == Qt.MouseButton.LeftButton:
            self.customPressEvent(event)
            return True
        return super().eventFilter(obj, event)

    def customPressEvent(self, event):
        print("Frame clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())