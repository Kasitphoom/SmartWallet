# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import test_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(393, 852)
        MainWindow.setMinimumSize(QSize(393, 852))
        MainWindow.setMaximumSize(QSize(393, 852))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(False)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(206, 255, 224);")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.content)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dashboardPage = QWidget()
        self.dashboardPage.setObjectName(u"dashboardPage")
        self.verticalLayout_3 = QVBoxLayout(self.dashboardPage)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.dashboardPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 389, 749))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.logoHeader = QFrame(self.scrollAreaWidgetContents)
        self.logoHeader.setObjectName(u"logoHeader")
        self.logoHeader.setStyleSheet(u"background-image: url(:/images/image/sw_logo_section.svg);\n"
"background-color: rgb(153, 255, 243);")
        self.logoHeader.setFrameShape(QFrame.StyledPanel)
        self.logoHeader.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.logoHeader)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 233, 146);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(79, 186, 116);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.dashboardPage)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.content)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"background-color: rgb(119, 255, 88);")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.footer)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(19, 23, 19, 23)
        self.frame = QFrame(self.footer)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(False)
        self.frame.setStyleSheet(u"background-color: rgb(79, 186, 116);\n"
"border-radius: 25px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(39)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(19, -1, 19, -1)
        self.graphButton = QPushButton(self.frame)
        self.graphButton.setObjectName(u"graphButton")
        font = QFont()
        font.setFamilies([u"Font Awesome 6 Free Solid"])
        self.graphButton.setFont(font)
        self.graphButton.setStyleSheet(u"background-color: rgb(255, 115, 102);\n"
"height:33px;\n"
"font-size: 24px;\n"
"color: white;\n"
"")

        self.horizontalLayout.addWidget(self.graphButton)

        self.historyButton = QPushButton(self.frame)
        self.historyButton.setObjectName(u"historyButton")
        self.historyButton.setFont(font)
        self.historyButton.setStyleSheet(u"background-color: rgb(148, 255, 124);\n"
"height: 33px;\n"
"font-size: 24px;\n"
"color: white;")

        self.horizontalLayout.addWidget(self.historyButton)

        self.dashboardButton = QPushButton(self.frame)
        self.dashboardButton.setObjectName(u"dashboardButton")
        font1 = QFont()
        font1.setFamilies([u"Font Awesome 6 Free Solid"])
        font1.setBold(True)
        self.dashboardButton.setFont(font1)
        self.dashboardButton.setStyleSheet(u"background-color: rgb(240, 255, 105);\n"
"height: 33px;\n"
"font-size: 24px;\n"
"color: white;")

        self.horizontalLayout.addWidget(self.dashboardButton)

        self.budgetplannerButton = QPushButton(self.frame)
        self.budgetplannerButton.setObjectName(u"budgetplannerButton")
        self.budgetplannerButton.setFont(font1)
        self.budgetplannerButton.setStyleSheet(u"background-color: rgb(183, 124, 255);\n"
"height: 33px;\n"
"font-size: 24px;\n"
"color: white;")

        self.horizontalLayout.addWidget(self.budgetplannerButton)

        self.othersButton = QPushButton(self.frame)
        self.othersButton.setObjectName(u"othersButton")
        self.othersButton.setFont(font1)
        self.othersButton.setStyleSheet(u"background-color: rgb(93, 123, 255);\n"
"height: 33px;\n"
"font-size: 24px;\n"
"color: white;")

        self.horizontalLayout.addWidget(self.othersButton)


        self.verticalLayout_4.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.graphButton.setText(QCoreApplication.translate("MainWindow", u"chart-line", None))
        self.historyButton.setText(QCoreApplication.translate("MainWindow", u"history", None))
        self.dashboardButton.setText(QCoreApplication.translate("MainWindow", u"house", None))
        self.budgetplannerButton.setText(QCoreApplication.translate("MainWindow", u"sack-dollar", None))
        self.othersButton.setText(QCoreApplication.translate("MainWindow", u"ellipsis", None))
    # retranslateUi

