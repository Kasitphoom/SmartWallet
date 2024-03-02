from PySide6.QtCore import Qt, QRectF, QPoint
from PySide6.QtGui import QPainter, QPainterPath, QPen, QColor, QBrush, QFont, QFontDatabase
from PySide6.QtWidgets import QVBoxLayout, QSlider, QWidget, QApplication
from pathlib import Path

class roundProgressBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.percentage = 0
        self.setMinimumSize(56, 56)
        # Load FontAwesome font
        font_id = QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "../otfs/Font Awesome 6 Free-Solid-900.otf").as_posix())
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.font_awesome = QFont(font_family)

    def update_value(self, percentage):
        if self.percentage == percentage:
            return
        self.percentage = percentage
        self.update()

    def paintEvent(self, e):
        if self.height() > self.width():
            self.setFixedWidth(self.height())
        if self.width() > self.height():
            self.setFixedHeight(self.width())
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        center = self.cal_center()
        circle_diameter = self.cal_circle_diameter()
        circle_radius = circle_diameter / 2
        circle_rect = QRectF(center.x() - circle_radius, center.y() - circle_radius, circle_diameter, circle_diameter)
        self.draw_progressed_arc(p, center, circle_rect)
        self.draw_remaining_arc(p, center, circle_rect)
        self.draw_percentage_text(p, center)
    
    def cal_center(self):
        return self.rect().center()
    
    def cal_circle_diameter(self):
        return min(self.width(), self.height()) - 8

    def draw_progressed_arc(self, p, center, circle_rect):
        percentage_degree = self.percentage * 360
        path = QPainterPath()
        path.moveTo(center.x(), center.y() - circle_rect.height() / 2)
        path.arcTo(circle_rect, 90, - percentage_degree)
        pen = QPen(QColor("#30b7e0"))
        pen.setCapStyle(Qt.FlatCap)
        pen.setWidthF(self.width() / 10)
        p.strokePath(path, pen)

    def draw_remaining_arc(self, p, center, circle_rect):
        percentage_degree = self.percentage * 360
        remaining_degree = 360 - percentage_degree
        path = QPainterPath()
        path.moveTo(center.x(), center.y() - circle_rect.height() / 2)
        path.arcTo(circle_rect, 90, remaining_degree)
        pen = QPen(QColor("#d7d7d7"))
        pen.setCapStyle(Qt.FlatCap)
        pen.setWidthF(self.width() / 10)
        p.strokePath(path, pen)

    def draw_percentage_text(self, p, center):
        # Set FontAwesome font
        self.font_awesome.setPointSize(16)
        p.setFont(self.font_awesome)
        
        # Set font color
        font_color = QColor("#30b7e0")
        p.setPen(font_color)
        
        # Calculate text size
        text = "bowl-food"
        text_rect = p.fontMetrics().boundingRect(text)
        
        # Calculate the position for drawing text
        text_position = center - QPoint(text_rect.width() / 2, -text_rect.height() / 2 + 2)
        
        # Draw text at the specified position
        p.drawText(text_position, text)

    def get_percentage(self):
        return int(self.percentage * 100)

# class Test(QWidget):
#     def __init__(self):
#         super().__init__()
#         l = QVBoxLayout(self)
#         p = roundProgressBar(self)
#         s = QSlider(Qt.Horizontal, self)
#         s.setMinimum(0)
#         s.setMaximum(100)
#         l.addWidget(p)
#         l.addWidget(s)
#         self.setLayout(l)
#         s.valueChanged.connect(lambda: p.upd(s.value() / s.maximum()))


# if __name__ == '__main__':
#     app = QApplication()
#     main_widget = Test()
#     main_widget.show()
#     app.exec_()