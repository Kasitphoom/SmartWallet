# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import test_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(393, 852)
        MainWindow.setMinimumSize(QSize(393, 852))
        MainWindow.setMaximumSize(QSize(393, 852))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.content)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"border: none;")
        self.stackedWidget.setLineWidth(0)
        self.dashboardPage = QWidget()
        self.dashboardPage.setObjectName(u"dashboardPage")
        self.verticalLayout_3 = QVBoxLayout(self.dashboardPage)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.dashboardPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setAcceptDrops(False)
        self.scrollArea.setStyleSheet(u"width:0px;\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 391, 1074))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(14)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 14)
        self.logoHeader = QFrame(self.scrollAreaWidgetContents)
        self.logoHeader.setObjectName(u"logoHeader")
        self.logoHeader.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logoHeader.sizePolicy().hasHeightForWidth())
        self.logoHeader.setSizePolicy(sizePolicy1)
        self.logoHeader.setMinimumSize(QSize(0, 110))
        self.logoHeader.setStyleSheet(u"background-image: url(:/images/image/sw_logo_section.svg);")
        self.logoHeader.setFrameShape(QFrame.StyledPanel)
        self.logoHeader.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.logoHeader)

        self.accountNumberframe = QFrame(self.scrollAreaWidgetContents)
        self.accountNumberframe.setObjectName(u"accountNumberframe")
        sizePolicy1.setHeightForWidth(self.accountNumberframe.sizePolicy().hasHeightForWidth())
        self.accountNumberframe.setSizePolicy(sizePolicy1)
        self.accountNumberframe.setMinimumSize(QSize(0, 50))
        self.accountNumberframe.setStyleSheet(u"")
        self.accountNumberframe.setFrameShape(QFrame.StyledPanel)
        self.accountNumberframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.accountNumberframe)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.greenbar1 = QFrame(self.accountNumberframe)
        self.greenbar1.setObjectName(u"greenbar1")
        self.greenbar1.setStyleSheet(u"background-color: rgb(79, 186, 116);")
        self.greenbar1.setFrameShape(QFrame.StyledPanel)
        self.greenbar1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.greenbar1)

        self.frame_6 = QFrame(self.accountNumberframe)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(0, 40))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.accountNolabel = QLabel(self.frame_6)
        self.accountNolabel.setObjectName(u"accountNolabel")
        sizePolicy1.setHeightForWidth(self.accountNolabel.sizePolicy().hasHeightForWidth())
        self.accountNolabel.setSizePolicy(sizePolicy1)
        self.accountNolabel.setMinimumSize(QSize(0, 15))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.accountNolabel.setFont(font)

        self.verticalLayout_7.addWidget(self.accountNolabel)

        self.accountNumberlowerframe = QFrame(self.frame_6)
        self.accountNumberlowerframe.setObjectName(u"accountNumberlowerframe")
        sizePolicy1.setHeightForWidth(self.accountNumberlowerframe.sizePolicy().hasHeightForWidth())
        self.accountNumberlowerframe.setSizePolicy(sizePolicy1)
        self.accountNumberlowerframe.setMinimumSize(QSize(0, 15))
        self.accountNumberlowerframe.setFrameShape(QFrame.StyledPanel)
        self.accountNumberlowerframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.accountNumberlowerframe)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.accountNumberlabel = QLabel(self.accountNumberlowerframe)
        self.accountNumberlabel.setObjectName(u"accountNumberlabel")
        sizePolicy1.setHeightForWidth(self.accountNumberlabel.sizePolicy().hasHeightForWidth())
        self.accountNumberlabel.setSizePolicy(sizePolicy1)
        self.accountNumberlabel.setMinimumSize(QSize(0, 15))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        self.accountNumberlabel.setFont(font1)

        self.horizontalLayout_2.addWidget(self.accountNumberlabel)

        self.eyeButton = QPushButton(self.accountNumberlowerframe)
        self.eyeButton.setObjectName(u"eyeButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.eyeButton.sizePolicy().hasHeightForWidth())
        self.eyeButton.setSizePolicy(sizePolicy2)
        self.eyeButton.setMinimumSize(QSize(16, 16))
        self.eyeButton.setStyleSheet(u"border: none;")
        icon = QIcon()
        icon.addFile(u":/images/image/faEye.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.eyeButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.eyeButton)

        self.horizontalSpacer = QSpacerItem(40, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addWidget(self.accountNumberlowerframe)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 50)

        self.verticalLayout_5.addWidget(self.accountNumberframe)

        self.Dashboard_balance_expense_saving = QFrame(self.scrollAreaWidgetContents)
        self.Dashboard_balance_expense_saving.setObjectName(u"Dashboard_balance_expense_saving")
        sizePolicy1.setHeightForWidth(self.Dashboard_balance_expense_saving.sizePolicy().hasHeightForWidth())
        self.Dashboard_balance_expense_saving.setSizePolicy(sizePolicy1)
        self.Dashboard_balance_expense_saving.setMinimumSize(QSize(0, 251))
        self.Dashboard_balance_expense_saving.setFrameShape(QFrame.StyledPanel)
        self.Dashboard_balance_expense_saving.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.Dashboard_balance_expense_saving)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, 9, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.Dashboard_expense = QFrame(self.Dashboard_balance_expense_saving)
        self.Dashboard_expense.setObjectName(u"Dashboard_expense")
        self.Dashboard_expense.setStyleSheet(u"background-color: rgba(171, 52, 40, 51);\n"
"border-radius: 15px;")
        self.Dashboard_expense.setFrameShape(QFrame.StyledPanel)
        self.Dashboard_expense.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.Dashboard_expense)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(15, -1, -1, -1)
        self.d_expense_title = QLabel(self.Dashboard_expense)
        self.d_expense_title.setObjectName(u"d_expense_title")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        self.d_expense_title.setFont(font2)
        self.d_expense_title.setStyleSheet(u"background-color: none;\n"
"color: #B3625A;\n"
"")

        self.gridLayout_6.addWidget(self.d_expense_title, 0, 0, 1, 1)

        self.d_expense_amount = QLabel(self.Dashboard_expense)
        self.d_expense_amount.setObjectName(u"d_expense_amount")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(16)
        font3.setWeight(QFont.Black)
        self.d_expense_amount.setFont(font3)
        self.d_expense_amount.setStyleSheet(u"background-color: none;\n"
"color: #B3625A;\n"
"")
        self.d_expense_amount.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.d_expense_amount, 1, 0, 1, 1)

        self.d_expense_description = QLabel(self.Dashboard_expense)
        self.d_expense_description.setObjectName(u"d_expense_description")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(8)
        self.d_expense_description.setFont(font4)
        self.d_expense_description.setStyleSheet(u"background-color: none;\n"
"color: #B3625A;\n"
"")

        self.gridLayout_6.addWidget(self.d_expense_description, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.Dashboard_expense, 1, 0, 1, 1)

        self.Dashboard_saving = QFrame(self.Dashboard_balance_expense_saving)
        self.Dashboard_saving.setObjectName(u"Dashboard_saving")
        self.Dashboard_saving.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgba(79, 186, 116, 76.5);")
        self.Dashboard_saving.setFrameShape(QFrame.StyledPanel)
        self.Dashboard_saving.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.Dashboard_saving)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, -1, -1, -1)
        self.d_saving_title = QLabel(self.Dashboard_saving)
        self.d_saving_title.setObjectName(u"d_saving_title")
        self.d_saving_title.setFont(font2)
        self.d_saving_title.setStyleSheet(u"background-color: none;\n"
"color: #4FBA74;\n"
"")

        self.gridLayout.addWidget(self.d_saving_title, 0, 0, 1, 1)

        self.d_saving_amount = QLabel(self.Dashboard_saving)
        self.d_saving_amount.setObjectName(u"d_saving_amount")
        self.d_saving_amount.setFont(font3)
        self.d_saving_amount.setStyleSheet(u"background-color: none;\n"
"color: #4FBA74;\n"
"")
        self.d_saving_amount.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.d_saving_amount, 1, 0, 1, 1)

        self.d_saving_description = QLabel(self.Dashboard_saving)
        self.d_saving_description.setObjectName(u"d_saving_description")
        self.d_saving_description.setFont(font4)
        self.d_saving_description.setStyleSheet(u"background-color: none;\n"
"color: #4FBA74;\n"
"")

        self.gridLayout.addWidget(self.d_saving_description, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.Dashboard_saving, 1, 1, 1, 1)

        self.Dashboard_balance = QFrame(self.Dashboard_balance_expense_saving)
        self.Dashboard_balance.setObjectName(u"Dashboard_balance")
        self.Dashboard_balance.setMinimumSize(QSize(0, 0))
        self.Dashboard_balance.setMaximumSize(QSize(16777215, 126))
        self.Dashboard_balance.setStyleSheet(u".QFrame {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(31, 162, 255, 255), stop:1 rgba(126, 242, 157, 255));\n"
"border-radius: 15px;\n"
"}")
        self.Dashboard_balance.setFrameShape(QFrame.StyledPanel)
        self.Dashboard_balance.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.Dashboard_balance)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(15, 15, -1, -1)
        self.d_balance_amount = QLabel(self.Dashboard_balance)
        self.d_balance_amount.setObjectName(u"d_balance_amount")
        self.d_balance_amount.setFont(font3)
        self.d_balance_amount.setStyleSheet(u"background-color: none;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.d_balance_amount.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.d_balance_amount, 1, 0, 1, 1)

        self.d_balance_title = QLabel(self.Dashboard_balance)
        self.d_balance_title.setObjectName(u"d_balance_title")
        self.d_balance_title.setFont(font2)
        self.d_balance_title.setStyleSheet(u"background-color: none;\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.d_balance_title, 0, 0, 1, 1)

        self.d_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.d_verticalSpacer, 2, 0, 1, 1)

        self.gridLayout_7.setRowStretch(0, 1)
        self.gridLayout_7.setRowStretch(1, 7)
        self.gridLayout_7.setRowStretch(2, 1)

        self.gridLayout_3.addWidget(self.Dashboard_balance, 0, 0, 1, 2)


        self.verticalLayout_9.addLayout(self.gridLayout_3)


        self.verticalLayout_5.addWidget(self.Dashboard_balance_expense_saving)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.greenbar3_2 = QFrame(self.frame_5)
        self.greenbar3_2.setObjectName(u"greenbar3_2")
        self.greenbar3_2.setStyleSheet(u"background-color: rgb(79, 186, 116);")
        self.greenbar3_2.setFrameShape(QFrame.StyledPanel)
        self.greenbar3_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.greenbar3_2)

        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(16)
        font5.setBold(True)
        self.label_2.setFont(font5)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMinimumSize(QSize(16, 16))
        icon1 = QIcon()
        icon1.addFile(u":/images/image/info-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 50)

        self.verticalLayout_5.addWidget(self.frame_5)

        self.limitscrollArea = QScrollArea(self.scrollAreaWidgetContents)
        self.limitscrollArea.setObjectName(u"limitscrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.limitscrollArea.sizePolicy().hasHeightForWidth())
        self.limitscrollArea.setSizePolicy(sizePolicy3)
        self.limitscrollArea.setMinimumSize(QSize(0, 90))
        self.limitscrollArea.setStyleSheet(u"width: 1px;\n"
"height: 10px;")
        self.limitscrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.limitscrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.limitscrollArea.setWidgetResizable(True)
        self.limitscrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.limitscrollAreaWidgetContents = QWidget()
        self.limitscrollAreaWidgetContents.setObjectName(u"limitscrollAreaWidgetContents")
        self.limitscrollAreaWidgetContents.setGeometry(QRect(0, 0, 720, 81))
        self.horizontalLayout_7 = QHBoxLayout(self.limitscrollAreaWidgetContents)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, 0, 9, 0)
        self.foodlimitframe = QFrame(self.limitscrollAreaWidgetContents)
        self.foodlimitframe.setObjectName(u"foodlimitframe")
        sizePolicy2.setHeightForWidth(self.foodlimitframe.sizePolicy().hasHeightForWidth())
        self.foodlimitframe.setSizePolicy(sizePolicy2)
        self.foodlimitframe.setMinimumSize(QSize(79, 81))
        self.foodlimitframe.setLayoutDirection(Qt.LeftToRight)
        self.foodlimitframe.setStyleSheet(u"background-color: rgb(238, 238, 238);\n"
"border-radius: 5px;\n"
"")
        self.foodlimitframe.setFrameShape(QFrame.StyledPanel)
        self.foodlimitframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.foodlimitframe)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 9, -1, 9)
        self.foodlimiticon = QLabel(self.foodlimitframe)
        self.foodlimiticon.setObjectName(u"foodlimiticon")
        font6 = QFont()
        font6.setFamilies([u"Font Awesome 6 Free"])
        font6.setPointSize(24)
        font6.setBold(True)
        self.foodlimiticon.setFont(font6)
        self.foodlimiticon.setStyleSheet(u"color: rgb(137, 137, 137);")
        self.foodlimiticon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.foodlimiticon)

        self.foodlimitlabel = QLabel(self.foodlimitframe)
        self.foodlimitlabel.setObjectName(u"foodlimitlabel")
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setBold(True)
        self.foodlimitlabel.setFont(font7)
        self.foodlimitlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.foodlimitlabel)

        self.limitcurrency_1 = QLabel(self.foodlimitframe)
        self.limitcurrency_1.setObjectName(u"limitcurrency_1")
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(7)
        font8.setBold(True)
        self.limitcurrency_1.setFont(font8)
        self.limitcurrency_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.limitcurrency_1)


        self.horizontalLayout_7.addWidget(self.foodlimitframe)

        self.entertainmentlimitframe = QFrame(self.limitscrollAreaWidgetContents)
        self.entertainmentlimitframe.setObjectName(u"entertainmentlimitframe")
        sizePolicy2.setHeightForWidth(self.entertainmentlimitframe.sizePolicy().hasHeightForWidth())
        self.entertainmentlimitframe.setSizePolicy(sizePolicy2)
        self.entertainmentlimitframe.setMinimumSize(QSize(79, 81))
        self.entertainmentlimitframe.setLayoutDirection(Qt.LeftToRight)
        self.entertainmentlimitframe.setStyleSheet(u"background-color: rgb(238, 238, 238);\n"
"border-radius: 5px;\n"
"")
        self.entertainmentlimitframe.setFrameShape(QFrame.StyledPanel)
        self.entertainmentlimitframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.entertainmentlimitframe)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, 9, -1, 9)
        self.entertainmentlimiticon = QLabel(self.entertainmentlimitframe)
        self.entertainmentlimiticon.setObjectName(u"entertainmentlimiticon")
        self.entertainmentlimiticon.setFont(font6)
        self.entertainmentlimiticon.setStyleSheet(u"color: rgb(137, 137, 137);")
        self.entertainmentlimiticon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.entertainmentlimiticon)

        self.entertainmentlimitlabel = QLabel(self.entertainmentlimitframe)
        self.entertainmentlimitlabel.setObjectName(u"entertainmentlimitlabel")
        self.entertainmentlimitlabel.setFont(font7)
        self.entertainmentlimitlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.entertainmentlimitlabel)

        self.limitcurrency_2 = QLabel(self.entertainmentlimitframe)
        self.limitcurrency_2.setObjectName(u"limitcurrency_2")
        self.limitcurrency_2.setFont(font8)
        self.limitcurrency_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.limitcurrency_2)


        self.horizontalLayout_7.addWidget(self.entertainmentlimitframe)

        self.transportationlimitframe = QFrame(self.limitscrollAreaWidgetContents)
        self.transportationlimitframe.setObjectName(u"transportationlimitframe")
        sizePolicy2.setHeightForWidth(self.transportationlimitframe.sizePolicy().hasHeightForWidth())
        self.transportationlimitframe.setSizePolicy(sizePolicy2)
        self.transportationlimitframe.setMinimumSize(QSize(79, 81))
        self.transportationlimitframe.setLayoutDirection(Qt.LeftToRight)
        self.transportationlimitframe.setStyleSheet(u"background-color: rgb(238, 238, 238);\n"
"border-radius: 5px;\n"
"")
        self.transportationlimitframe.setFrameShape(QFrame.StyledPanel)
        self.transportationlimitframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.transportationlimitframe)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 9, -1, 9)
        self.transportationlimiticon = QLabel(self.transportationlimitframe)
        self.transportationlimiticon.setObjectName(u"transportationlimiticon")
        self.transportationlimiticon.setFont(font6)
        self.transportationlimiticon.setStyleSheet(u"color: rgb(137, 137, 137);")
        self.transportationlimiticon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.transportationlimiticon)

        self.transportationlimitlabel = QLabel(self.transportationlimitframe)
        self.transportationlimitlabel.setObjectName(u"transportationlimitlabel")
        self.transportationlimitlabel.setFont(font7)
        self.transportationlimitlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.transportationlimitlabel)

        self.limitcurrency_3 = QLabel(self.transportationlimitframe)
        self.limitcurrency_3.setObjectName(u"limitcurrency_3")
        self.limitcurrency_3.setFont(font8)
        self.limitcurrency_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.limitcurrency_3)


        self.horizontalLayout_7.addWidget(self.transportationlimitframe)

        self.returnlimitframe = QFrame(self.limitscrollAreaWidgetContents)
        self.returnlimitframe.setObjectName(u"returnlimitframe")
        sizePolicy2.setHeightForWidth(self.returnlimitframe.sizePolicy().hasHeightForWidth())
        self.returnlimitframe.setSizePolicy(sizePolicy2)
        self.returnlimitframe.setMinimumSize(QSize(79, 81))
        self.returnlimitframe.setLayoutDirection(Qt.LeftToRight)
        self.returnlimitframe.setStyleSheet(u"background-color: rgb(238, 238, 238);\n"
"border-radius: 5px;\n"
"")
        self.returnlimitframe.setFrameShape(QFrame.StyledPanel)
        self.returnlimitframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.returnlimitframe)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, 9, -1, 9)
        self.returnlimiticon = QLabel(self.returnlimitframe)
        self.returnlimiticon.setObjectName(u"returnlimiticon")
        self.returnlimiticon.setFont(font6)
        self.returnlimiticon.setStyleSheet(u"color: rgb(137, 137, 137);")
        self.returnlimiticon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.returnlimiticon)

        self.returnlimitlabel = QLabel(self.returnlimitframe)
        self.returnlimitlabel.setObjectName(u"returnlimitlabel")
        self.returnlimitlabel.setFont(font7)
        self.returnlimitlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.returnlimitlabel)

        self.limitcurrency_4 = QLabel(self.returnlimitframe)
        self.limitcurrency_4.setObjectName(u"limitcurrency_4")
        self.limitcurrency_4.setFont(font8)
        self.limitcurrency_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.limitcurrency_4)


        self.horizontalLayout_7.addWidget(self.returnlimitframe)

        self.lendlimitframe = QFrame(self.limitscrollAreaWidgetContents)
        self.lendlimitframe.setObjectName(u"lendlimitframe")
        sizePolicy2.setHeightForWidth(self.lendlimitframe.sizePolicy().hasHeightForWidth())
        self.lendlimitframe.setSizePolicy(sizePolicy2)
        self.lendlimitframe.setMinimumSize(QSize(79, 81))
        self.lendlimitframe.setLayoutDirection(Qt.LeftToRight)
        self.lendlimitframe.setStyleSheet(u"background-color: rgb(238, 238, 238);\n"
"border-radius: 5px;\n"
"")
        self.lendlimitframe.setFrameShape(QFrame.StyledPanel)
        self.lendlimitframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.lendlimitframe)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, 9, -1, 9)
        self.lendlimiticon = QLabel(self.lendlimitframe)
        self.lendlimiticon.setObjectName(u"lendlimiticon")
        self.lendlimiticon.setFont(font6)
        self.lendlimiticon.setStyleSheet(u"color: rgb(137, 137, 137);")
        self.lendlimiticon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.lendlimiticon)

        self.lendlimitlabel = QLabel(self.lendlimitframe)
        self.lendlimitlabel.setObjectName(u"lendlimitlabel")
        self.lendlimitlabel.setFont(font7)
        self.lendlimitlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.lendlimitlabel)

        self.limitcurrency_5 = QLabel(self.lendlimitframe)
        self.limitcurrency_5.setObjectName(u"limitcurrency_5")
        self.limitcurrency_5.setFont(font8)
        self.limitcurrency_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.limitcurrency_5)


        self.horizontalLayout_7.addWidget(self.lendlimitframe)

        self.healthcarelimitframe = QFrame(self.limitscrollAreaWidgetContents)
        self.healthcarelimitframe.setObjectName(u"healthcarelimitframe")
        sizePolicy2.setHeightForWidth(self.healthcarelimitframe.sizePolicy().hasHeightForWidth())
        self.healthcarelimitframe.setSizePolicy(sizePolicy2)
        self.healthcarelimitframe.setMinimumSize(QSize(79, 81))
        self.healthcarelimitframe.setLayoutDirection(Qt.LeftToRight)
        self.healthcarelimitframe.setStyleSheet(u"background-color: rgb(238, 238, 238);\n"
"border-radius: 5px;\n"
"")
        self.healthcarelimitframe.setFrameShape(QFrame.StyledPanel)
        self.healthcarelimitframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.healthcarelimitframe)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, 9, -1, 9)
        self.healthcarelimiticon = QLabel(self.healthcarelimitframe)
        self.healthcarelimiticon.setObjectName(u"healthcarelimiticon")
        self.healthcarelimiticon.setFont(font6)
        self.healthcarelimiticon.setStyleSheet(u"color: rgb(137, 137, 137);")
        self.healthcarelimiticon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.healthcarelimiticon)

        self.healthcarelimitlabel = QLabel(self.healthcarelimitframe)
        self.healthcarelimitlabel.setObjectName(u"healthcarelimitlabel")
        self.healthcarelimitlabel.setFont(font7)
        self.healthcarelimitlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.healthcarelimitlabel)

        self.limitcurrency_6 = QLabel(self.healthcarelimitframe)
        self.limitcurrency_6.setObjectName(u"limitcurrency_6")
        self.limitcurrency_6.setFont(font8)
        self.limitcurrency_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.limitcurrency_6)


        self.horizontalLayout_7.addWidget(self.healthcarelimitframe)

        self.educationlimitframe = QFrame(self.limitscrollAreaWidgetContents)
        self.educationlimitframe.setObjectName(u"educationlimitframe")
        sizePolicy2.setHeightForWidth(self.educationlimitframe.sizePolicy().hasHeightForWidth())
        self.educationlimitframe.setSizePolicy(sizePolicy2)
        self.educationlimitframe.setMinimumSize(QSize(79, 81))
        self.educationlimitframe.setLayoutDirection(Qt.LeftToRight)
        self.educationlimitframe.setStyleSheet(u"background-color: rgb(238, 238, 238);\n"
"border-radius: 5px;\n"
"")
        self.educationlimitframe.setFrameShape(QFrame.StyledPanel)
        self.educationlimitframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.educationlimitframe)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 9, -1, 9)
        self.educationlimiticon = QLabel(self.educationlimitframe)
        self.educationlimiticon.setObjectName(u"educationlimiticon")
        self.educationlimiticon.setFont(font6)
        self.educationlimiticon.setStyleSheet(u"color: rgb(137, 137, 137);")
        self.educationlimiticon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.educationlimiticon)

        self.educationlimitlabel = QLabel(self.educationlimitframe)
        self.educationlimitlabel.setObjectName(u"educationlimitlabel")
        self.educationlimitlabel.setFont(font7)
        self.educationlimitlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.educationlimitlabel)

        self.limitcurrency_7 = QLabel(self.educationlimitframe)
        self.limitcurrency_7.setObjectName(u"limitcurrency_7")
        self.limitcurrency_7.setFont(font8)
        self.limitcurrency_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.limitcurrency_7)


        self.horizontalLayout_7.addWidget(self.educationlimitframe)

        self.otherlimitframe = QFrame(self.limitscrollAreaWidgetContents)
        self.otherlimitframe.setObjectName(u"otherlimitframe")
        sizePolicy2.setHeightForWidth(self.otherlimitframe.sizePolicy().hasHeightForWidth())
        self.otherlimitframe.setSizePolicy(sizePolicy2)
        self.otherlimitframe.setMinimumSize(QSize(79, 81))
        self.otherlimitframe.setLayoutDirection(Qt.LeftToRight)
        self.otherlimitframe.setStyleSheet(u"background-color: rgb(238, 238, 238);\n"
"border-radius: 5px;\n"
"")
        self.otherlimitframe.setFrameShape(QFrame.StyledPanel)
        self.otherlimitframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.otherlimitframe)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, 9, -1, 9)
        self.otherlimiticon = QLabel(self.otherlimitframe)
        self.otherlimiticon.setObjectName(u"otherlimiticon")
        self.otherlimiticon.setFont(font6)
        self.otherlimiticon.setStyleSheet(u"color: rgb(137, 137, 137);")
        self.otherlimiticon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.otherlimiticon)

        self.otherlimitlabel = QLabel(self.otherlimitframe)
        self.otherlimitlabel.setObjectName(u"otherlimitlabel")
        self.otherlimitlabel.setFont(font7)
        self.otherlimitlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.otherlimitlabel)

        self.limitcurrency_8 = QLabel(self.otherlimitframe)
        self.limitcurrency_8.setObjectName(u"limitcurrency_8")
        self.limitcurrency_8.setFont(font8)
        self.limitcurrency_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.limitcurrency_8)


        self.horizontalLayout_7.addWidget(self.otherlimitframe)

        self.limitscrollArea.setWidget(self.limitscrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.limitscrollArea)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.greenbar3 = QFrame(self.frame_4)
        self.greenbar3.setObjectName(u"greenbar3")
        self.greenbar3.setStyleSheet(u"background-color: rgb(79, 186, 116);")
        self.greenbar3.setFrameShape(QFrame.StyledPanel)
        self.greenbar3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.greenbar3)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font5)

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 50)

        self.verticalLayout_5.addWidget(self.frame_4)

        self.featuresframe = QFrame(self.scrollAreaWidgetContents)
        self.featuresframe.setObjectName(u"featuresframe")
        sizePolicy1.setHeightForWidth(self.featuresframe.sizePolicy().hasHeightForWidth())
        self.featuresframe.setSizePolicy(sizePolicy1)
        self.featuresframe.setMinimumSize(QSize(0, 170))
        self.featuresframe.setFrameShape(QFrame.StyledPanel)
        self.featuresframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.featuresframe)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.ftransferframe = QFrame(self.featuresframe)
        self.ftransferframe.setObjectName(u"ftransferframe")
        self.ftransferframe.setFrameShape(QFrame.StyledPanel)
        self.ftransferframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.ftransferframe)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 1, 0, 0)
        self.ftransferButton = QPushButton(self.ftransferframe)
        self.ftransferButton.setObjectName(u"ftransferButton")
        self.ftransferButton.setMinimumSize(QSize(0, 0))
        icon2 = QIcon()
        icon2.addFile(u":/images/image/transfer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ftransferButton.setIcon(icon2)
        self.ftransferButton.setIconSize(QSize(42, 42))

        self.verticalLayout_8.addWidget(self.ftransferButton)

        self.ftransferlabel = QLabel(self.ftransferframe)
        self.ftransferlabel.setObjectName(u"ftransferlabel")
        font9 = QFont()
        font9.setFamilies([u"Arial"])
        font9.setPointSize(12)
        self.ftransferlabel.setFont(font9)
        self.ftransferlabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_8.addWidget(self.ftransferlabel)


        self.gridLayout_2.addWidget(self.ftransferframe, 0, 4, 1, 1)

        self.fbudgetplannerframe = QFrame(self.featuresframe)
        self.fbudgetplannerframe.setObjectName(u"fbudgetplannerframe")
        self.fbudgetplannerframe.setMinimumSize(QSize(0, 10))
        self.fbudgetplannerframe.setFrameShape(QFrame.StyledPanel)
        self.fbudgetplannerframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.fbudgetplannerframe)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.fbudgetplannerButton = QPushButton(self.fbudgetplannerframe)
        self.fbudgetplannerButton.setObjectName(u"fbudgetplannerButton")
        self.fbudgetplannerButton.setMinimumSize(QSize(0, 42))
        icon3 = QIcon()
        icon3.addFile(u":/images/image/budget-planner.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fbudgetplannerButton.setIcon(icon3)
        self.fbudgetplannerButton.setIconSize(QSize(42, 42))

        self.verticalLayout_11.addWidget(self.fbudgetplannerButton)

        self.fbudgetplannerlabel = QLabel(self.fbudgetplannerframe)
        self.fbudgetplannerlabel.setObjectName(u"fbudgetplannerlabel")
        self.fbudgetplannerlabel.setMinimumSize(QSize(0, 0))
        self.fbudgetplannerlabel.setFont(font9)
        self.fbudgetplannerlabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_11.addWidget(self.fbudgetplannerlabel)

        self.verticalLayout_11.setStretch(0, 1)

        self.gridLayout_2.addWidget(self.fbudgetplannerframe, 0, 6, 1, 1)

        self.faddbillsframe = QFrame(self.featuresframe)
        self.faddbillsframe.setObjectName(u"faddbillsframe")
        self.faddbillsframe.setFrameShape(QFrame.StyledPanel)
        self.faddbillsframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.faddbillsframe)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.faddbillsButton = QPushButton(self.faddbillsframe)
        self.faddbillsButton.setObjectName(u"faddbillsButton")
        icon4 = QIcon()
        icon4.addFile(u":/images/image/add-bills.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.faddbillsButton.setIcon(icon4)
        self.faddbillsButton.setIconSize(QSize(42, 42))

        self.verticalLayout_10.addWidget(self.faddbillsButton)

        self.faddbillslabel = QLabel(self.faddbillsframe)
        self.faddbillslabel.setObjectName(u"faddbillslabel")
        self.faddbillslabel.setFont(font9)
        self.faddbillslabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.faddbillslabel)


        self.gridLayout_2.addWidget(self.faddbillsframe, 0, 5, 1, 1)

        self.fsummaryframe = QFrame(self.featuresframe)
        self.fsummaryframe.setObjectName(u"fsummaryframe")
        self.fsummaryframe.setFrameShape(QFrame.StyledPanel)
        self.fsummaryframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.fsummaryframe)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.fsummaryButton = QPushButton(self.fsummaryframe)
        self.fsummaryButton.setObjectName(u"fsummaryButton")
        icon5 = QIcon()
        icon5.addFile(u":/images/image/summary.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fsummaryButton.setIcon(icon5)
        self.fsummaryButton.setIconSize(QSize(42, 42))

        self.verticalLayout_14.addWidget(self.fsummaryButton)

        self.fsummarylabel = QLabel(self.fsummaryframe)
        self.fsummarylabel.setObjectName(u"fsummarylabel")
        self.fsummarylabel.setFont(font9)
        self.fsummarylabel.setLineWidth(1)
        self.fsummarylabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.fsummarylabel)


        self.gridLayout_2.addWidget(self.fsummaryframe, 1, 4, 1, 1)

        self.fmyqrframe = QFrame(self.featuresframe)
        self.fmyqrframe.setObjectName(u"fmyqrframe")
        self.fmyqrframe.setFrameShape(QFrame.StyledPanel)
        self.fmyqrframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.fmyqrframe)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.fmyqrButton = QPushButton(self.fmyqrframe)
        self.fmyqrButton.setObjectName(u"fmyqrButton")
        icon6 = QIcon()
        icon6.addFile(u":/images/image/my-qr.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fmyqrButton.setIcon(icon6)
        self.fmyqrButton.setIconSize(QSize(42, 42))

        self.verticalLayout_16.addWidget(self.fmyqrButton)

        self.fmyqrlabel = QLabel(self.fmyqrframe)
        self.fmyqrlabel.setObjectName(u"fmyqrlabel")
        self.fmyqrlabel.setFont(font9)
        self.fmyqrlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.fmyqrlabel)


        self.gridLayout_2.addWidget(self.fmyqrframe, 1, 5, 1, 1)

        self.fhistoryframe = QFrame(self.featuresframe)
        self.fhistoryframe.setObjectName(u"fhistoryframe")
        self.fhistoryframe.setMinimumSize(QSize(0, 0))
        self.fhistoryframe.setFrameShape(QFrame.StyledPanel)
        self.fhistoryframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.fhistoryframe)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.fhistoryButton = QPushButton(self.fhistoryframe)
        self.fhistoryButton.setObjectName(u"fhistoryButton")
        icon7 = QIcon()
        icon7.addFile(u":/images/image/history-features.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fhistoryButton.setIcon(icon7)
        self.fhistoryButton.setIconSize(QSize(42, 42))

        self.verticalLayout_12.addWidget(self.fhistoryButton)

        self.fhistorylabel = QLabel(self.fhistoryframe)
        self.fhistorylabel.setObjectName(u"fhistorylabel")
        self.fhistorylabel.setFont(font9)
        self.fhistorylabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_12.addWidget(self.fhistorylabel)


        self.gridLayout_2.addWidget(self.fhistoryframe, 0, 7, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addWidget(self.featuresframe)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setMinimumSize(QSize(0, 50))
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_18.setContentsMargins(9, 9, 9, 9)
        self.greenbar3_5 = QFrame(self.frame_9)
        self.greenbar3_5.setObjectName(u"greenbar3_5")
        self.greenbar3_5.setStyleSheet(u"background-color: rgb(79, 186, 116);")
        self.greenbar3_5.setFrameShape(QFrame.StyledPanel)
        self.greenbar3_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_18.addWidget(self.greenbar3_5)

        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)

        self.horizontalLayout_18.addWidget(self.label_5)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 50)

        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 127))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_21.setSpacing(14)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(24, 0, 24, 0)
        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy4)
        self.frame_10.setMinimumSize(QSize(164, 0))
        self.frame_10.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(238, 238, 238);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        font10 = QFont()
        font10.setFamilies([u"Arial"])
        font10.setPointSize(11)
        font10.setBold(True)
        self.label_8.setFont(font10)

        self.verticalLayout_13.addWidget(self.label_8)

        self.monthtodateframe = QFrame(self.frame_10)
        self.monthtodateframe.setObjectName(u"monthtodateframe")
        self.monthtodateframe.setFrameShape(QFrame.StyledPanel)
        self.monthtodateframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.monthtodateframe)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.mtdArrowindicatorframe = QFrame(self.monthtodateframe)
        self.mtdArrowindicatorframe.setObjectName(u"mtdArrowindicatorframe")
        sizePolicy2.setHeightForWidth(self.mtdArrowindicatorframe.sizePolicy().hasHeightForWidth())
        self.mtdArrowindicatorframe.setSizePolicy(sizePolicy2)
        self.mtdArrowindicatorframe.setMinimumSize(QSize(18, 24))
        self.mtdArrowindicatorframe.setStyleSheet(u"background-image: url(:/images/image/arrow-none.svg);")
        self.mtdArrowindicatorframe.setFrameShape(QFrame.StyledPanel)
        self.mtdArrowindicatorframe.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_22.addWidget(self.mtdArrowindicatorframe)

        self.mtdPercentagelabel = QLabel(self.monthtodateframe)
        self.mtdPercentagelabel.setObjectName(u"mtdPercentagelabel")
        font11 = QFont()
        font11.setPointSize(16)
        self.mtdPercentagelabel.setFont(font11)
        self.mtdPercentagelabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.mtdPercentagelabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.mtdPercentagelabel)

        self.mtdPercentagevaluelabel = QLabel(self.monthtodateframe)
        self.mtdPercentagevaluelabel.setObjectName(u"mtdPercentagevaluelabel")
        self.mtdPercentagevaluelabel.setFont(font11)
        self.mtdPercentagevaluelabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.mtdPercentagevaluelabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.mtdPercentagevaluelabel)

        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(1, 3)
        self.horizontalLayout_22.setStretch(2, 1)

        self.verticalLayout_13.addWidget(self.monthtodateframe)

        self.label_11 = QLabel(self.frame_10)
        self.label_11.setObjectName(u"label_11")
        font12 = QFont()
        font12.setFamilies([u"Arial"])
        font12.setPointSize(10)
        self.label_11.setFont(font12)

        self.verticalLayout_13.addWidget(self.label_11)


        self.horizontalLayout_21.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy4.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy4)
        self.frame_11.setMinimumSize(QSize(164, 0))
        self.frame_11.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(238, 238, 238);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_11)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font10)

        self.verticalLayout_19.addWidget(self.label_9)

        self.totalforcastedcostframe = QFrame(self.frame_11)
        self.totalforcastedcostframe.setObjectName(u"totalforcastedcostframe")
        self.totalforcastedcostframe.setFrameShape(QFrame.StyledPanel)
        self.totalforcastedcostframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.totalforcastedcostframe)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 0, -1, 0)
        self.tfcArrowindicatorframe = QFrame(self.totalforcastedcostframe)
        self.tfcArrowindicatorframe.setObjectName(u"tfcArrowindicatorframe")
        sizePolicy2.setHeightForWidth(self.tfcArrowindicatorframe.sizePolicy().hasHeightForWidth())
        self.tfcArrowindicatorframe.setSizePolicy(sizePolicy2)
        self.tfcArrowindicatorframe.setMinimumSize(QSize(18, 24))
        self.tfcArrowindicatorframe.setStyleSheet(u"background-image: url(:/images/image/arrow-none.svg);")
        self.tfcArrowindicatorframe.setFrameShape(QFrame.StyledPanel)
        self.tfcArrowindicatorframe.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_23.addWidget(self.tfcArrowindicatorframe)

        self.tfcPerccentagevaluelabel = QLabel(self.totalforcastedcostframe)
        self.tfcPerccentagevaluelabel.setObjectName(u"tfcPerccentagevaluelabel")
        self.tfcPerccentagevaluelabel.setFont(font11)
        self.tfcPerccentagevaluelabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tfcPerccentagevaluelabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.tfcPerccentagevaluelabel)

        self.tfcPercentagelabel = QLabel(self.totalforcastedcostframe)
        self.tfcPercentagelabel.setObjectName(u"tfcPercentagelabel")
        self.tfcPercentagelabel.setFont(font11)
        self.tfcPercentagelabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tfcPercentagelabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.tfcPercentagelabel)

        self.horizontalLayout_23.setStretch(0, 1)
        self.horizontalLayout_23.setStretch(1, 3)
        self.horizontalLayout_23.setStretch(2, 1)

        self.verticalLayout_19.addWidget(self.totalforcastedcostframe)

        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font12)

        self.verticalLayout_19.addWidget(self.label_12)


        self.horizontalLayout_21.addWidget(self.frame_11)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.dashboardPage)
        self.transferPage = QWidget()
        self.transferPage.setObjectName(u"transferPage")
        self.verticalLayout_20 = QVBoxLayout(self.transferPage)
        self.verticalLayout_20.setSpacing(14)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 14)
        self.logoHeader_2 = QFrame(self.transferPage)
        self.logoHeader_2.setObjectName(u"logoHeader_2")
        self.logoHeader_2.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.logoHeader_2.sizePolicy().hasHeightForWidth())
        self.logoHeader_2.setSizePolicy(sizePolicy1)
        self.logoHeader_2.setMinimumSize(QSize(0, 110))
        self.logoHeader_2.setStyleSheet(u"background-image: url(:/images/image/sw_logo_section.svg);")
        self.logoHeader_2.setFrameShape(QFrame.StyledPanel)
        self.logoHeader_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_20.addWidget(self.logoHeader_2)

        self.transferbackframe = QFrame(self.transferPage)
        self.transferbackframe.setObjectName(u"transferbackframe")
        sizePolicy1.setHeightForWidth(self.transferbackframe.sizePolicy().hasHeightForWidth())
        self.transferbackframe.setSizePolicy(sizePolicy1)
        self.transferbackframe.setMinimumSize(QSize(0, 20))
        self.transferbackframe.setFrameShape(QFrame.StyledPanel)
        self.transferbackframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.transferbackframe)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(41, 0, 41, 0)
        self.transferbackButto = QPushButton(self.transferbackframe)
        self.transferbackButto.setObjectName(u"transferbackButto")
        sizePolicy2.setHeightForWidth(self.transferbackButto.sizePolicy().hasHeightForWidth())
        self.transferbackButto.setSizePolicy(sizePolicy2)
        self.transferbackButto.setMinimumSize(QSize(99, 20))
        self.transferbackButto.setStyleSheet(u"background-image: url(:/images/image/backtransfer.svg);")

        self.horizontalLayout_11.addWidget(self.transferbackButto)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)


        self.verticalLayout_20.addWidget(self.transferbackframe)

        self.frame_20 = QFrame(self.transferPage)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy1.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy1)
        self.frame_20.setStyleSheet(u"")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_20)
        self.verticalLayout_26.setSpacing(24)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(39, 0, 39, 0)
        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy1.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy1)
        self.frame_22.setMinimumSize(QSize(0, 20))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_3 = QLabel(self.frame_22)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_3)


        self.verticalLayout_26.addWidget(self.frame_22)

        self.qrcodeButton = QPushButton(self.frame_20)
        self.qrcodeButton.setObjectName(u"qrcodeButton")
        sizePolicy2.setHeightForWidth(self.qrcodeButton.sizePolicy().hasHeightForWidth())
        self.qrcodeButton.setSizePolicy(sizePolicy2)
        self.qrcodeButton.setMinimumSize(QSize(314, 63))
        self.qrcodeButton.setStyleSheet(u"background-image: url(:/images/image/qrcodeButton.svg);")

        self.verticalLayout_26.addWidget(self.qrcodeButton)

        self.pushButton_3 = QPushButton(self.frame_20)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setMinimumSize(QSize(314, 63))
        self.pushButton_3.setStyleSheet(u"background-image: url(:/images/image/directtransferButton.svg);")

        self.verticalLayout_26.addWidget(self.pushButton_3)

        self.line_2 = QFrame(self.frame_20)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_26.addWidget(self.line_2)


        self.verticalLayout_20.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.transferPage)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.verticalLayout_20.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.transferPage)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.content)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 16))
        self.footer.setStyleSheet(u"")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.footer)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(19, 23, 19, 23)
        self.menubar = QFrame(self.footer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(False)
        self.menubar.setStyleSheet(u"background-color: rgb(79, 186, 116);\n"
"border-radius: 25px;\n"
"")
        self.menubar.setFrameShape(QFrame.StyledPanel)
        self.menubar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.menubar)
        self.horizontalLayout.setSpacing(39)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(19, -1, 19, -1)
        self.graphButton = QPushButton(self.menubar)
        self.graphButton.setObjectName(u"graphButton")
        font13 = QFont()
        font13.setFamilies([u"Font Awesome 6 Free"])
        font13.setBold(True)
        self.graphButton.setFont(font13)
        self.graphButton.setStyleSheet(u"height:33px;\n"
"font-size: 24px;\n"
"color: white;\n"
"")

        self.horizontalLayout.addWidget(self.graphButton)

        self.historyButton = QPushButton(self.menubar)
        self.historyButton.setObjectName(u"historyButton")
        self.historyButton.setFont(font13)
        self.historyButton.setStyleSheet(u"height: 33px;\n"
"font-size: 24px;\n"
"color: white;")

        self.horizontalLayout.addWidget(self.historyButton)

        self.dashboardButton = QPushButton(self.menubar)
        self.dashboardButton.setObjectName(u"dashboardButton")
        self.dashboardButton.setFont(font13)
        self.dashboardButton.setStyleSheet(u"height: 33px;\n"
"font-size: 24px;\n"
"color: white;")

        self.horizontalLayout.addWidget(self.dashboardButton)

        self.budgetplannerButton = QPushButton(self.menubar)
        self.budgetplannerButton.setObjectName(u"budgetplannerButton")
        self.budgetplannerButton.setFont(font13)
        self.budgetplannerButton.setStyleSheet(u"height: 33px;\n"
"font-size: 24px;\n"
"color: white;")

        self.horizontalLayout.addWidget(self.budgetplannerButton)

        self.othersButton = QPushButton(self.menubar)
        self.othersButton.setObjectName(u"othersButton")
        self.othersButton.setFont(font13)
        self.othersButton.setStyleSheet(u"height: 33px;\n"
"font-size: 24px;\n"
"color: white;")

        self.horizontalLayout.addWidget(self.othersButton)


        self.verticalLayout_4.addWidget(self.menubar)


        self.verticalLayout_2.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.accountNolabel.setText(QCoreApplication.translate("MainWindow", u"Account No.", None))
        self.accountNumberlabel.setText(QCoreApplication.translate("MainWindow", u"xxx-x-xxxx-x", None))
        self.eyeButton.setText("")
        self.d_expense_title.setText(QCoreApplication.translate("MainWindow", u"Total Expense", None))
        self.d_expense_amount.setText(QCoreApplication.translate("MainWindow", u"0.00 THB", None))
        self.d_expense_description.setText(QCoreApplication.translate("MainWindow", u"Total expense of this month", None))
        self.d_saving_title.setText(QCoreApplication.translate("MainWindow", u"Total Saving", None))
        self.d_saving_amount.setText(QCoreApplication.translate("MainWindow", u"0.00 THB", None))
        self.d_saving_description.setText(QCoreApplication.translate("MainWindow", u"The accumulated savings\n"
"from every type of expense ", None))
        self.d_balance_amount.setText(QCoreApplication.translate("MainWindow", u"0.00 THB", None))
        self.d_balance_title.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Your limits today", None))
        self.pushButton.setText("")
        self.foodlimiticon.setText(QCoreApplication.translate("MainWindow", u"bowl-food", None))
        self.foodlimitlabel.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.limitcurrency_1.setText(QCoreApplication.translate("MainWindow", u"THB", None))
        self.entertainmentlimiticon.setText(QCoreApplication.translate("MainWindow", u"film", None))
        self.entertainmentlimitlabel.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.limitcurrency_2.setText(QCoreApplication.translate("MainWindow", u"THB", None))
        self.transportationlimiticon.setText(QCoreApplication.translate("MainWindow", u"car", None))
        self.transportationlimitlabel.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.limitcurrency_3.setText(QCoreApplication.translate("MainWindow", u"THB", None))
        self.returnlimiticon.setText(QCoreApplication.translate("MainWindow", u"person-walking-arrow-loop-left", None))
        self.returnlimitlabel.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.limitcurrency_4.setText(QCoreApplication.translate("MainWindow", u"THB", None))
        self.lendlimiticon.setText(QCoreApplication.translate("MainWindow", u"download", None))
        self.lendlimitlabel.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.limitcurrency_5.setText(QCoreApplication.translate("MainWindow", u"THB", None))
        self.healthcarelimiticon.setText(QCoreApplication.translate("MainWindow", u"heart-pulse", None))
        self.healthcarelimitlabel.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.limitcurrency_6.setText(QCoreApplication.translate("MainWindow", u"THB", None))
        self.educationlimiticon.setText(QCoreApplication.translate("MainWindow", u"building", None))
        self.educationlimitlabel.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.limitcurrency_7.setText(QCoreApplication.translate("MainWindow", u"THB", None))
        self.otherlimiticon.setText(QCoreApplication.translate("MainWindow", u"Question", None))
        self.otherlimitlabel.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.limitcurrency_8.setText(QCoreApplication.translate("MainWindow", u"THB", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Features", None))
        self.ftransferButton.setText("")
        self.ftransferlabel.setText(QCoreApplication.translate("MainWindow", u"Transfer", None))
        self.fbudgetplannerButton.setText("")
        self.fbudgetplannerlabel.setText(QCoreApplication.translate("MainWindow", u"Budget \n"
"Planner", None))
        self.faddbillsButton.setText("")
        self.faddbillslabel.setText(QCoreApplication.translate("MainWindow", u"Add Bills", None))
        self.fsummaryButton.setText("")
        self.fsummarylabel.setText(QCoreApplication.translate("MainWindow", u"Summary", None))
        self.fmyqrButton.setText("")
        self.fmyqrlabel.setText(QCoreApplication.translate("MainWindow", u"My QR", None))
        self.fhistoryButton.setText("")
        self.fhistorylabel.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cost Summary", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Month to date", None))
        self.mtdPercentagelabel.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.mtdPercentagevaluelabel.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"compared to last month \n"
"for same period", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Total forcasted cost", None))
        self.tfcPerccentagevaluelabel.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.tfcPercentagelabel.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"compared to last month \n"
"total cost", None))
        self.transferbackButto.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Choose your method", None))
        self.qrcodeButton.setText("")
        self.pushButton_3.setText("")
        self.graphButton.setText(QCoreApplication.translate("MainWindow", u"chart-line", None))
        self.historyButton.setText(QCoreApplication.translate("MainWindow", u"history", None))
        self.dashboardButton.setText(QCoreApplication.translate("MainWindow", u"house", None))
        self.budgetplannerButton.setText(QCoreApplication.translate("MainWindow", u"sack-dollar", None))
        self.othersButton.setText(QCoreApplication.translate("MainWindow", u"ellipsis", None))
    # retranslateUi

