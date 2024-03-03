from PySide6.QtCore import Qt, QRectF, QPoint, QTimer
from PySide6.QtGui import QPainter, QPainterPath, QPen, QColor, QBrush, QFont, QFontDatabase
from PySide6.QtWidgets import QVBoxLayout, QSlider, QWidget, QApplication, QPushButton
from pathlib import Path

class roundProgressBar(QWidget):
    def __init__(self, parent, category="food"):
        super().__init__(parent)
        self.category = category
        self.percentage = 0
        self.setMinimumSize(56, 56)
        # Load FontAwesome font
        font_id = QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "../otfs/Font Awesome 6 Free-Solid-900.otf").as_posix())
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.font_awesome = QFont(font_family)
        self.limit_font_awesome_map = {
            "housing": "building",
            "food": "bowl-food",
            "transport": "car",
            "entertainment": "film",
            "healthcare": "heart-pulse",
        }
        self.animation_speed = 10
        self.animation_duration = 500
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.animate_progress)
        self.animation_timer.setInterval(10)  # Interval in milliseconds

    def update_value(self, percentage):
        if self.percentage == percentage:
            return
        self.start_animation(percentage)

    def start_animation(self, target_percentage):
        self.target_percentage = target_percentage
        # Calculate the number of steps and interval time for smooth animation
        num_steps = int(self.animation_duration / self.animation_timer.interval())
        self.step_percentage = (self.target_percentage - self.percentage) / num_steps
        self.animation_step = 0
        self.animation_timer.start()

    def animate_progress(self):
        self.percentage += self.step_percentage
        self.animation_step += 1
        self.update()
        if self.animation_step >= self.animation_duration / self.animation_timer.interval():
            self.percentage = self.target_percentage
            self.animation_timer.stop()
            self.update()

    def animate_from_zero(self):
        percentage = self.percentage
        self.percentage = 0
        self.update_value(percentage)

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
        if self.gray_color:
            self.color = QColor("#D9D9D9")
        elif percentage_degree >= 50:
            self.color = QColor("#37C768")
        elif percentage_degree >= 25:
            self.color = QColor("#FDA653")
        else:
            self.color = QColor("#E06053")
        pen = QPen(self.color)
        pen.setCapStyle(Qt.FlatCap)
        pen.setWidthF(self.width() / 10)
        p.strokePath(path, pen)

    def draw_remaining_arc(self, p, center, circle_rect):
        percentage_degree = self.percentage * 360
        remaining_degree = 360 - percentage_degree
        path = QPainterPath()
        path.moveTo(center.x(), center.y() - circle_rect.height() / 2)
        path.arcTo(circle_rect, 90, remaining_degree)
        pen = QPen(QColor("#D9D9D9"))
        pen.setCapStyle(Qt.FlatCap)
        pen.setWidthF(self.width() / 10)
        p.strokePath(path, pen)

    def draw_percentage_text(self, p, center):
        # Set FontAwesome font
        self.font_awesome.setPointSize(16)
        p.setFont(self.font_awesome)
        
        # Set font color
        font_color = self.color
        p.setPen(font_color)
        
        # Calculate text size
        text = self.limit_font_awesome_map[self.category]
        text_rect = p.fontMetrics().boundingRect(text)
        
        # Calculate the position for drawing text
        text_position = center - QPoint(text_rect.width() / 2, -text_rect.height() / 2 + 2)
        
        # Draw text at the specified position
        p.drawText(text_position, text)

    def get_category(self):
        return self.category
    
    def set_gray_color(self, boolean):
        self.gray_color = boolean

    def get_if_gray_color(self):
        return self.gray_color

# class Test(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.layout = QVBoxLayout(self)
#         self.progress_bar = roundProgressBar(self)
#         self.slider = QSlider(Qt.Horizontal)
#         self.slider.setMinimum(0)
#         self.slider.setMaximum(100)
#         self.layout.addWidget(self.progress_bar)
#         self.layout.addWidget(self.slider)
#         self.setLayout(self.layout)

#         # Create buttons
#         self.button_to_50 = QPushButton("Change to 50")
#         self.button_to_0 = QPushButton("Change to 0")

#         # Add buttons to layout
#         self.layout.addWidget(self.button_to_50)
#         self.layout.addWidget(self.button_to_0)

#         # Connect button signals
#         self.button_to_50.clicked.connect(self.set_progress_to_50)
#         self.button_to_0.clicked.connect(self.set_progress_to_0)
#         self.slider.valueChanged.connect(self.update_progress_bar)

#     def set_progress_to_50(self):
#         self.progress_bar.update_value(0.5)

#     def set_progress_to_0(self):
#         self.progress_bar.update_value(0)

#     def update_progress_bar(self, value):
#         self.progress_bar.update_value(value / 100)


if __name__ == '__main__':
    app = QApplication([])
    main_widget = Test()
    main_widget.show()
    app.exec_()