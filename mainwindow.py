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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(False)
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
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 391, 751))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(14)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.logoHeader = QFrame(self.scrollAreaWidgetContents)
        self.logoHeader.setObjectName(u"logoHeader")
        self.logoHeader.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
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
        self.accountNumberframe.setMinimumSize(QSize(0, 40))
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
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

        self.horizontalSpacer = QSpacerItem(40, 15, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addWidget(self.accountNumberlowerframe)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 50)

        self.verticalLayout_5.addWidget(self.accountNumberframe)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setMinimumSize(QSize(0, 251))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, 9, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.frame_9 = QFrame(self.frame_10)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgba(171, 52, 40, 51);\n"
"border-radius: 15px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_9, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgba(79, 186, 116, 76.5);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_11, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.frame_10)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(31, 162, 255, 255), stop:1 rgba(126, 242, 157, 255));\n"
"border-radius: 15px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 2)


        self.verticalLayout_9.addLayout(self.gridLayout_3)


        self.verticalLayout_5.addWidget(self.frame_10)

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
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.label_2.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/images/image/info-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 50)

        self.verticalLayout_5.addWidget(self.frame_5)

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
        self.label.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 50)

        self.verticalLayout_5.addWidget(self.frame_4)

        self.featuresframe = QFrame(self.scrollAreaWidgetContents)
        self.featuresframe.setObjectName(u"featuresframe")
        sizePolicy1.setHeightForWidth(self.featuresframe.sizePolicy().hasHeightForWidth())
        self.featuresframe.setSizePolicy(sizePolicy1)
        self.featuresframe.setMinimumSize(QSize(0, 151))
        self.featuresframe.setFrameShape(QFrame.StyledPanel)
        self.featuresframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.featuresframe)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.fhistoryframe = QFrame(self.featuresframe)
        self.fhistoryframe.setObjectName(u"fhistoryframe")
        self.fhistoryframe.setFrameShape(QFrame.StyledPanel)
        self.fhistoryframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.fhistoryframe)
        self.verticalLayout_12.setSpacing(2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.fhistoryButton = QPushButton(self.fhistoryframe)
        self.fhistoryButton.setObjectName(u"fhistoryButton")
        icon2 = QIcon()
        icon2.addFile(u":/images/image/history-features.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fhistoryButton.setIcon(icon2)
        self.fhistoryButton.setIconSize(QSize(42, 42))

        self.verticalLayout_12.addWidget(self.fhistoryButton)

        self.fhistorylabel = QLabel(self.fhistoryframe)
        self.fhistorylabel.setObjectName(u"fhistorylabel")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        self.fhistorylabel.setFont(font3)
        self.fhistorylabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.fhistorylabel)


        self.gridLayout_2.addWidget(self.fhistoryframe, 0, 7, 1, 1)

        self.ftransferframe = QFrame(self.featuresframe)
        self.ftransferframe.setObjectName(u"ftransferframe")
        self.ftransferframe.setFrameShape(QFrame.StyledPanel)
        self.ftransferframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.ftransferframe)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.ftransferButton = QPushButton(self.ftransferframe)
        self.ftransferButton.setObjectName(u"ftransferButton")
        self.ftransferButton.setMinimumSize(QSize(0, 0))
        icon3 = QIcon()
        icon3.addFile(u":/images/image/transfer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ftransferButton.setIcon(icon3)
        self.ftransferButton.setIconSize(QSize(42, 42))

        self.verticalLayout_8.addWidget(self.ftransferButton)

        self.ftransferlabel = QLabel(self.ftransferframe)
        self.ftransferlabel.setObjectName(u"ftransferlabel")
        self.ftransferlabel.setFont(font3)
        self.ftransferlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.ftransferlabel)


        self.gridLayout_2.addWidget(self.ftransferframe, 0, 4, 1, 1)

        self.fbudgetplannerframe = QFrame(self.featuresframe)
        self.fbudgetplannerframe.setObjectName(u"fbudgetplannerframe")
        self.fbudgetplannerframe.setFrameShape(QFrame.StyledPanel)
        self.fbudgetplannerframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.fbudgetplannerframe)
        self.verticalLayout_11.setSpacing(2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.fbudgetplannerButton = QPushButton(self.fbudgetplannerframe)
        self.fbudgetplannerButton.setObjectName(u"fbudgetplannerButton")
        icon4 = QIcon()
        icon4.addFile(u":/images/image/budget-planner.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fbudgetplannerButton.setIcon(icon4)
        self.fbudgetplannerButton.setIconSize(QSize(42, 42))

        self.verticalLayout_11.addWidget(self.fbudgetplannerButton)

        self.fbudgetplannerlabel = QLabel(self.fbudgetplannerframe)
        self.fbudgetplannerlabel.setObjectName(u"fbudgetplannerlabel")
        self.fbudgetplannerlabel.setFont(font3)
        self.fbudgetplannerlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.fbudgetplannerlabel)


        self.gridLayout_2.addWidget(self.fbudgetplannerframe, 0, 6, 1, 1)

        self.faddbillsframe = QFrame(self.featuresframe)
        self.faddbillsframe.setObjectName(u"faddbillsframe")
        self.faddbillsframe.setFrameShape(QFrame.StyledPanel)
        self.faddbillsframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.faddbillsframe)
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.faddbillsButton = QPushButton(self.faddbillsframe)
        self.faddbillsButton.setObjectName(u"faddbillsButton")
        icon5 = QIcon()
        icon5.addFile(u":/images/image/add-bills.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.faddbillsButton.setIcon(icon5)
        self.faddbillsButton.setIconSize(QSize(42, 42))

        self.verticalLayout_10.addWidget(self.faddbillsButton)

        self.faddbillslabel = QLabel(self.faddbillsframe)
        self.faddbillslabel.setObjectName(u"faddbillslabel")
        self.faddbillslabel.setFont(font3)
        self.faddbillslabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.faddbillslabel)


        self.gridLayout_2.addWidget(self.faddbillsframe, 0, 5, 1, 1)

        self.fsummaryframe = QFrame(self.featuresframe)
        self.fsummaryframe.setObjectName(u"fsummaryframe")
        self.fsummaryframe.setFrameShape(QFrame.StyledPanel)
        self.fsummaryframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.fsummaryframe)
        self.verticalLayout_14.setSpacing(2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.fsummaryButton = QPushButton(self.fsummaryframe)
        self.fsummaryButton.setObjectName(u"fsummaryButton")
        icon6 = QIcon()
        icon6.addFile(u":/images/image/summary.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fsummaryButton.setIcon(icon6)
        self.fsummaryButton.setIconSize(QSize(42, 42))

        self.verticalLayout_14.addWidget(self.fsummaryButton)

        self.fsummarylabel = QLabel(self.fsummaryframe)
        self.fsummarylabel.setObjectName(u"fsummarylabel")
        self.fsummarylabel.setFont(font3)
        self.fsummarylabel.setLineWidth(1)
        self.fsummarylabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.fsummarylabel)


        self.gridLayout_2.addWidget(self.fsummaryframe, 1, 4, 1, 1)

        self.fmyqrframe = QFrame(self.featuresframe)
        self.fmyqrframe.setObjectName(u"fmyqrframe")
        self.fmyqrframe.setFrameShape(QFrame.StyledPanel)
        self.fmyqrframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.fmyqrframe)
        self.verticalLayout_16.setSpacing(2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.fmyqrButton = QPushButton(self.fmyqrframe)
        self.fmyqrButton.setObjectName(u"fmyqrButton")
        icon7 = QIcon()
        icon7.addFile(u":/images/image/my-qr.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fmyqrButton.setIcon(icon7)
        self.fmyqrButton.setIconSize(QSize(42, 42))

        self.verticalLayout_16.addWidget(self.fmyqrButton)

        self.fmyqrlabel = QLabel(self.fmyqrframe)
        self.fmyqrlabel.setObjectName(u"fmyqrlabel")
        self.fmyqrlabel.setFont(font3)
        self.fmyqrlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.fmyqrlabel)


        self.gridLayout_2.addWidget(self.fmyqrframe, 1, 5, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addWidget(self.featuresframe)

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
        font4 = QFont()
        font4.setFamilies([u"Font Awesome 6 Free Solid"])
        self.graphButton.setFont(font4)
        self.graphButton.setStyleSheet(u"height:33px;\n"
"font-size: 24px;\n"
"color: white;\n"
"")

        self.horizontalLayout.addWidget(self.graphButton)

        self.historyButton = QPushButton(self.menubar)
        self.historyButton.setObjectName(u"historyButton")
        self.historyButton.setFont(font4)
        self.historyButton.setStyleSheet(u"height: 33px;\n"
"font-size: 24px;\n"
"color: white;")

        self.horizontalLayout.addWidget(self.historyButton)

        self.dashboardButton = QPushButton(self.menubar)
        self.dashboardButton.setObjectName(u"dashboardButton")
        font5 = QFont()
        font5.setFamilies([u"Font Awesome 6 Free Solid"])
        font5.setBold(True)
        self.dashboardButton.setFont(font5)
        self.dashboardButton.setStyleSheet(u"height: 33px;\n"
"font-size: 24px;\n"
"color: white;")

        self.horizontalLayout.addWidget(self.dashboardButton)

        self.budgetplannerButton = QPushButton(self.menubar)
        self.budgetplannerButton.setObjectName(u"budgetplannerButton")
        self.budgetplannerButton.setFont(font5)
        self.budgetplannerButton.setStyleSheet(u"height: 33px;\n"
"font-size: 24px;\n"
"color: white;")

        self.horizontalLayout.addWidget(self.budgetplannerButton)

        self.othersButton = QPushButton(self.menubar)
        self.othersButton.setObjectName(u"othersButton")
        self.othersButton.setFont(font5)
        self.othersButton.setStyleSheet(u"height: 33px;\n"
"font-size: 24px;\n"
"color: white;")

        self.horizontalLayout.addWidget(self.othersButton)


        self.verticalLayout_4.addWidget(self.menubar)


        self.verticalLayout_2.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.accountNolabel.setText(QCoreApplication.translate("MainWindow", u"Account No.", None))
        self.accountNumberlabel.setText(QCoreApplication.translate("MainWindow", u"xxx-x-xxxx-x", None))
        self.eyeButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Your limits today", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Features", None))
        self.fhistoryButton.setText("")
        self.fhistorylabel.setText(QCoreApplication.translate("MainWindow", u"History", None))
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
        self.graphButton.setText(QCoreApplication.translate("MainWindow", u"chart-line", None))
        self.historyButton.setText(QCoreApplication.translate("MainWindow", u"history", None))
        self.dashboardButton.setText(QCoreApplication.translate("MainWindow", u"house", None))
        self.budgetplannerButton.setText(QCoreApplication.translate("MainWindow", u"sack-dollar", None))
        self.othersButton.setText(QCoreApplication.translate("MainWindow", u"ellipsis", None))
    # retranslateUi

