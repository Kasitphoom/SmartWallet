from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFrame, QTreeWidget, QTreeWidgetItem, QLineEdit, QLayoutItem, QLayout, QCheckBox
from PySide6.QtCore import QSize, QRect, Qt, Slot, QTimer, QPoint, QEasingCurve, QPropertyAnimation, Property
from PySide6.QtGui import QPainter, QColor, QPen, QBrush, QFont, QPixmap, QIcon

class ToggleSwitch(QCheckBox):
    def __init__(
        self,
        width = 60,
        bg_color = "#5B5B5B",
        circle_color = "#FFFFFF",
        active_color = "#4FBA74",
        animation_curve = QEasingCurve.OutQuint,
        circle_margin = 3,
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
        self._circle_position = circle_margin
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)


        # Circle Margin (circle position)
        self._circle_margin = circle_margin

        # Connect State Changed
        self.stateChanged.connect(self.startTransition) 

    # Create new set and get property for animation
    @Property(int)
    def circle_position(self):
        return self._circle_position
    
    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()

    def startTransition(self, value):
        # Stop animation if running
        self.animation.stop()

        if value:
            self.animation.setEndValue(self.width() - self.height() + self._circle_margin)
        else:
            self.animation.setEndValue(self._circle_margin)
            # im am here

        # Start Animation
        self.animation.start()
        
        # print(f"Status: {self.isChecked()}")

    # Set new hit area
    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)
    
    # Paint Event (Draw Toggle Switch)
    def paintEvent(self, event):
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
