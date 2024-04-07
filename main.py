import sys
import os

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFrame, QTreeWidget, QTreeWidgetItem, QLineEdit, QLayoutItem, QLayout, QCheckBox, QFileDialog, QMessageBox, QDialog
from PySide6.QtCore import QSize, QRect, Qt, Slot, QTimer, Signal
from PySide6.QtGui import QFont, QFontDatabase, QMouseEvent, QImage, QPixmap
from mainwindow import Ui_MainWindow
from info import Ui_Dialog

from py_toggle import ToggleSwitch

from pathlib import Path

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont, ImageGrab

from obj.walletmanager import WalletManager
from obj.account import Account
from obj.roundprogressbar import roundProgressBar
from obj.WalletManagerObject import TransactionFrame, BillFrame, TransactionItem
from obj.transaction import Transaction

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

import pytesseract

import pickle

import hashlib
import cv2
import qrcode

import requests
import json

LIMIT_LABEL = ["housing", "food", "transport", "entertainment", "healthcare", "saving"]
TRANSFER_TYPE_LABEL = ["housing", "food", "transport", "entertainment", "healthcare", "saving", "return", "lend", "others"]
LOOK_UP_OBJ_NAME = ["LineEdit", "progressbar", "Button"]

cache_dir = Path(__file__).parent / "cache"
cache_dir.mkdir(parents=True, exist_ok=True)
USER_CACHE_FILE = cache_dir / "user_cache.pkl"

if USER_CACHE_FILE.exists():
    with open(USER_CACHE_FILE, "rb") as f:
        user_cache = pickle.load(f)
else:
    with open(USER_CACHE_FILE, "wb") as f:
        user_cache = ""
        pickle.dump(user_cache, f)

class InfoDialog(QDialog):
    def __init__(self, system):
        QDialog.__init__(self, None)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.system = system
        self.ui.pushButton.clicked.connect(self.submit)
        self.date = None
    
    def submit(self):
        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.manager = WalletManager()
        self.account_number_visibility = False
        self.calculated_limits = {}
        self.__salt = "rT8jllFhs7"
        self.transfer_type_selected = "others"
        self.current_date = datetime.now()
        # self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)
        self.detector = cv2.QRCodeDetector()
        self.pil_myQr = None
        self.page = {
            # stacked widget
            "dashboard": 0,
            "transfer": 1,
            "budgetplanner": 2,
            "directtransfer": 3,
            "history": 4,
            "scanqrcode": 5,
            "others": 6,
            "setting": 7,
            "myQRcode": 8,
            "parentalcontrol": 9,
            "graph": 10,
            "addbill": 11,
            "transactionInfo": 12,
            "captureReceipt": 13,
            # stacked widget 2
            "main": 0,
            "login": 1,
            "register": 2,
            "pin": 3,
        }
        

        # Add fonts in QFontDatabase before setting up the UI
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Font Awesome 6 Free-Solid-900.otf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-Black.ttf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-Bold.ttf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-ExtraBold.ttf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-ExtraLight.ttf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-Light.ttf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-Medium.ttf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-Regular.ttf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-SemiBold.ttf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-Thin.ttf").as_posix())
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        if user_cache == "":
            self.ui.stackedWidget_2.setCurrentIndex(self.page["login"])
        elif self.manager.check_accounts(user_cache):
            self.manager.set_account(user_cache)
            self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
            self.update_window()
            # set initial budget page
            self.setupBudget()
            self.setupOthersPage()
            # generate My QR code
            self.createMyQRcode()
            # setup parental control toggle
            self.pcToggleSetup()
            # setup graph page
            self.setupGraph()
        else:
            self.ui.stackedWidget_2.setCurrentIndex(self.page["login"])
        
        self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"])
        self.ui.frame_10.installEventFilter(self)
        
        # login page
        self.ui.loginButton.clicked.connect(self.handleLogin)
        self.ui.registerButton.clicked.connect(self.handleRegister)
        
        # show/hide account number
        self.ui.eyeButton.clicked.connect(self.handleAccountNumberVisibility)
        self.ui.eyeButtonDT.clicked.connect(self.handleAccountNumberVisibility)
        
        # buttons to change page
        self.ui.dashboardButton.clicked.connect(lambda: self.changePage("dashboard"))
        self.ui.ftransferButton.clicked.connect(lambda:self.changePage("transfer"))
        self.ui.fbudgetplannerButton.clicked.connect(lambda: self.changePage("budgetplanner"))
        self.ui.budgetplannerButton.clicked.connect(lambda: self.changePage("budgetplanner"))
        self.ui.redirectToRegisterButton.clicked.connect(lambda: self.changeState("register"))
        self.ui.redirectToLoginButton.clicked.connect(lambda: self.changeState("login"))
        self.ui.transferbackButton.clicked.connect(lambda: self.changePage("dashboard"))
        self.ui.navigateToDirectTransferButton.clicked.connect(lambda: self.changePage("directtransfer"))
        self.ui.navigateToDirectQrcodeButton.clicked.connect(self.handleNavigationToScanQRCode)
        self.ui.fhistoryButton.clicked.connect(lambda: self.changePage("history"))
        self.ui.historyButton.clicked.connect(lambda: self.changePage("history"))
        self.ui.othersButton.clicked.connect(lambda: self.changePage("others"))
        self.ui.setting_button.clicked.connect(lambda: self.changePage("setting"))
        self.ui.fmyqrButton.clicked.connect(lambda: self.changePage("myQRcode"))
        self.ui.parental_control_button.clicked.connect(lambda: self.changePage("parentalcontrol"))
        self.ui.faddbillsButton.clicked.connect(lambda: self.changePage("addbill"))
        self.ui.graphButton.clicked.connect(self.handleNavigationToGraph)
        self.ui.fsummaryButton.clicked.connect(self.handleNavigationToGraph)
        self.ui.add_bill_open_cameraButton.clicked.connect(self.handleNaviationToCaptureReceipt)
        self.ui.capturereceiptBackButton.clicked.connect(lambda: self.changePage("addbill"))
        self.ui.captureButton.clicked.connect(self.capture_image)
        self.ui.moreInfoButton.clicked.connect(self.show_info_dialog)
        self.ui.moreInfoButtonDT.clicked.connect(self.show_info_dialog)

        
        # back buttons
        self.ui.budgetBackButton.clicked.connect(lambda: self.changePage("dashboard"))
        self.ui.dicrectTransferBackButton.clicked.connect(lambda: self.changePage("transfer"))
        self.ui.historybackButton.clicked.connect(lambda: self.changePage("dashboard"))
        self.ui.othersBackButton.clicked.connect(lambda: self.changePage("dashboard"))
        self.ui.scanQRCodeBackButton.clicked.connect(lambda: self.changePage("transfer"))
        self.ui.settingBackButton.clicked.connect(lambda: self.changePage("others"))
        self.ui.transferbackButton.clicked.connect(lambda: self.changePage("dashboard"))
        self.ui.parentalControlBackButton.clicked.connect(lambda: self.changePage("setting"))
        self.ui.graphBackButton.clicked.connect(lambda: self.changePage("dashboard"))
        self.ui.addbillBackButton.clicked.connect(lambda: self.changePage("dashboard"))

        # Pin
        self.pin_labels = [self.ui.pin_1, self.ui.pin_2, self.ui.pin_3, self.ui.pin_4, self.ui.pin_5, self.ui.pin_6]
        self.ui.pin_num_0.clicked.connect(lambda: self.addNumberToPin("0"))
        self.ui.pin_num_1.clicked.connect(lambda: self.addNumberToPin("1"))
        self.ui.pin_num_2.clicked.connect(lambda: self.addNumberToPin("2"))
        self.ui.pin_num_3.clicked.connect(lambda: self.addNumberToPin("3"))
        self.ui.pin_num_4.clicked.connect(lambda: self.addNumberToPin("4"))
        self.ui.pin_num_5.clicked.connect(lambda: self.addNumberToPin("5"))
        self.ui.pin_num_6.clicked.connect(lambda: self.addNumberToPin("6"))
        self.ui.pin_num_7.clicked.connect(lambda: self.addNumberToPin("7"))
        self.ui.pin_num_8.clicked.connect(lambda: self.addNumberToPin("8"))
        self.ui.pin_num_9.clicked.connect(lambda: self.addNumberToPin("9"))
        self.ui.pin_delete.clicked.connect(self.deletePin)

        # handle page change
        self.ui.stackedWidget_2.currentChanged.connect(self.page_changed_handler_2)
        self.ui.stackedWidget.currentChanged.connect(self.page_changed_handler)

        # setup transfer confirm button
        self.ui.dt_confirmButton.clicked.connect(self.handleTransfer)
        
        # handle history type change
        self.ui.history_all_button.clicked.connect(lambda: self.update_history_page("all"))
        self.ui.history_expense_button.clicked.connect(lambda: self.update_history_page("expense"))
        self.ui.history_income_button.clicked.connect(lambda: self.update_history_page("income"))
        
        # handle logout
        self.ui.logout_button.clicked.connect(self.handleLogout)

        # setup my QR code page
        self.ui.saveMyQRcodeButton.clicked.connect(self.saveMyQRcode)

        # handle Radio button in graph page
        self.ui.dayradioButton.toggled.connect(self.updateGraph)
        self.ui.monthradioButton.toggled.connect(self.updateGraph)
        self.ui.yearradioButton.toggled.connect(self.updateGraph)
        self.ui.lineradioButton.toggled.connect(self.updateGraph)
        self.ui.barradioButton.toggled.connect(self.updateGraph)
        self.ui.allradioButton.toggled.connect(self.updateGraph)
        self.ui.incomeradioButton.toggled.connect(self.updateGraph)
        self.ui.expenseradioButton.toggled.connect(self.updateGraph)

        self.ui.dateEdit.dateChanged.connect(self.updateGraph)
        
        # handle add bill
        self.ui.add_single_billButton.clicked.connect(self.addSingleBill)
        self.ui.add_bill_choose_fileButton.clicked.connect(self.addBillFromFile)
        self.ui.finish_addbillButton.clicked.connect(self.finishAddBill)

# ================================== Login and Registration Handling ==================================

    def handleLogin(self):
        email = self.ui.loginEmailLineEdit.text()
        password = self.ui.loginPasswordLineEdit.text() + self.__salt
        
        hash_object = hashlib.sha256(password.encode())
        password = hash_object.hexdigest()
        
        account = self.manager.login_account(email, password)
        
        if account:
            # save to cache
            with open(USER_CACHE_FILE, "wb") as f:
                user_cache = account.getID()
                self.manager.set_account(user_cache)
                pickle.dump(user_cache, f)
            if not self.manager.getPin():
                self.nagivateToPin("Create your PIN")
                self.ui.pinLineEdit.textChanged.connect(self.handlePinRegister)
            else:
                self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
                self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"])
                self.update_window()
                self.setupBudget()
                self.setupOthersPage()
                self.createMyQRcode()
        else:
            self.ui.loginError.setText("Invalid email or password")

    def handleRegister(self):
        fullname = self.ui.registerFullNameENLineEdit.text()
        email = self.ui.registerEmailLineEdit.text()
        password = self.ui.registerPasswordLineEdit.text() + self.__salt
        confirm_password = self.ui.registerConfirmPasswordLineEdit.text() + self.__salt
        
        if password != confirm_password:
            self.ui.registerConfirmPasswordError.setText("Password does not match")
            return
        
        hash_object = hashlib.sha256(password.encode())
        password = hash_object.hexdigest()
        
        self.manager.register_account(fullname, email, password)
        self.ui.stackedWidget_2.setCurrentIndex(self.page["login"])

    def handlePinRegister(self):
        if len(self.ui.pinLineEdit.text()) <= 6 and len(self.ui.pinLineEdit.text()) > 0:
            self.pin_labels[len(self.ui.pinLineEdit.text())-1].setStyleSheet("background-image: url(:/images/image/pin_dot.svg); background-repeat: no-repeat;")
        if len(self.ui.pinLineEdit.text()) == 6:
            pin = self.ui.pinLineEdit.text() + self.__salt
            hash_object = hashlib.sha256(pin.encode())
            pin = hash_object.hexdigest()
            self.manager.setPin(pin)
            self.ui.pinLineEdit.textChanged.disconnect()
            self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
            self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"])
            self.update_window()
            self.setupBudget()
            self.setupOthersPage()
            self.createMyQRcode()
        

# ================================== Dashboard ==================================

    def update_window(self):
        self.ui.d_balance_amount.setText(self.manager.get_balance() + " THB")
        
        # set text as this format XXX-X-1234-X
        self.ui.accountNumberlabel.setText(self.manager.get_account_number_non_visible())
        self.ui.accountNumberlabelDT.setText(self.manager.get_account_number_non_visible())
        
        # set balance
        self.ui.d_balance_amount.setText(self.manager.get_balance() + " THB")
        
        self.update_daily_limit()
        self.update_total_month_expense()
        
        # set transfer balance and budget amount
        self.ui.dt_balance_amount.setText(self.manager.get_balance() + " THB")
        
        # update month to date expense (from 1st of the month to today compare with 1st of last month to the same date as today)
        self.update_month_to_date_expense()
        
        # update history page
        self.update_history_page()
        
        self.update_total_savings()
        self.setupTransferPage()

    def update_daily_limit(self):
        # Update daily limit for each category and set the color of the limit frame and icon.
        # house limit
        housing_limit = self.manager.calculate_daily_limit("housing")
        max_housing_limit = self.manager.get_max_daily_limit("housing")
        
        
        self.ui.housinglimitlabel.setText(f"{housing_limit:,.2f}")
        self.ui.housinglimiticon.setStyleSheet(f"color: {'#B3625A' if housing_limit < max_housing_limit * 0.25 else '#F49E4C' if housing_limit < max_housing_limit * 0.50 else '#4FBA74'}")
        self.ui.housinglimitframe.setStyleSheet(self.style_sheet_color_limit("housing"))
        
        # food limit
        food_limit = self.manager.calculate_daily_limit("food")
        max_food_limit = self.manager.get_max_daily_limit("food")
        
        self.ui.foodlimitlabel.setText(f"{food_limit:,.2f}")
        self.ui.foodlimitframe.setStyleSheet(self.style_sheet_color_limit("food"))
        self.ui.foodlimiticon.setStyleSheet(f"color: {'#B3625A' if food_limit < max_food_limit * 0.25 else '#F49E4C' if food_limit < max_food_limit * 0.50 else '#4FBA74'}")
        
        # transport limit
        transport_limit = self.manager.calculate_daily_limit("transport")
        max_transport_limit = self.manager.get_max_daily_limit("transport")
        
        self.ui.transportationlimitlabel.setText(f"{transport_limit:,.2f}")
        self.ui.transportationlimitframe.setStyleSheet(self.style_sheet_color_limit("transport"))
        self.ui.transportationlimiticon.setStyleSheet(f"color: {'#B3625A' if transport_limit < max_transport_limit * 0.25 else '#F49E4C' if transport_limit < max_transport_limit * 0.50 else '#4FBA74'}")
        
        # entertainment limit
        entertainment_limit = self.manager.calculate_daily_limit("entertainment")
        max_entertainment_limit = self.manager.get_max_daily_limit("entertainment")
        
        self.ui.entertainmentlimitlabel.setText(f"{entertainment_limit:,.2f}")
        self.ui.entertainmentlimitframe.setStyleSheet(self.style_sheet_color_limit("entertainment"))
        self.ui.entertainmentlimiticon.setStyleSheet(f"color: {'#B3625A' if entertainment_limit < max_entertainment_limit * 0.25 else '#F49E4C' if entertainment_limit < max_entertainment_limit * 0.50 else '#4FBA74'}")
        
        # healthcare limit
        healthcare_limit = self.manager.calculate_daily_limit("healthcare")
        max_healthcare_limit = self.manager.get_max_daily_limit("healthcare")
        
        self.ui.healthcarelimitlabel.setText(f"{healthcare_limit:,.2f}")
        self.ui.healthcarelimitframe.setStyleSheet(self.style_sheet_color_limit("healthcare"))
        self.ui.healthcarelimiticon.setStyleSheet(f"color: {'#B3625A' if healthcare_limit < max_healthcare_limit * 0.25 else '#F49E4C' if healthcare_limit < max_healthcare_limit * 0.50 else '#4FBA74'}")
        
        # other limit
        other_limit = self.manager.calculate_daily_limit("others")
        max_other_limit = self.manager.get_max_daily_limit("others")
        
        self.ui.otherlimitlabel.setText(f"{other_limit:,.2f}")
        self.ui.otherlimitframe.setStyleSheet(self.style_sheet_color_limit("others"))
        self.ui.otherlimiticon.setStyleSheet(f"color: {'#B3625A' if other_limit < max_other_limit * 0.25 else '#F49E4C' if other_limit < max_other_limit * 0.50 else '#4FBA74'}")

    def update_total_month_expense(self):
        self.ui.d_expense_amount.setText(f"{self.manager.get_total_expense_of_this_month():,.2f} THB")

    def update_month_to_date_expense(self):
        this_month_expense = self.manager.get_total_expense_of_this_month()
        last_month_expense = self.manager.get_total_expense_period(datetime(self.current_date.year, self.current_date.month - 1, 1), datetime(self.current_date.year, self.current_date.month-1, self.current_date.day))
        percentage = this_month_expense / 1 if last_month_expense == 0 else last_month_expense * 100
        
        self.ui.mtdPercentagevaluelabel.setText(f"{percentage: .2f}")
        self.ui.mtdArrowindicator.setText("arrow-up" if this_month_expense > last_month_expense else "arrow-down")
        self.ui.monthtodateframe.setStyleSheet(f"QLabel {{ color: {'#B3625A' if this_month_expense > last_month_expense else '#4FBA74'} }}")

    def handleAccountNumberVisibility(self):
        self.account_number_visibility = not self.account_number_visibility
        if self.account_number_visibility:
            self.ui.accountNumberlabel.setText(self.manager.get_account_number_visible())
            self.ui.accountNumberlabelDT.setText(self.manager.get_account_number_visible())
        else:
            self.ui.accountNumberlabel.setText(self.manager.get_account_number_non_visible())
            self.ui.accountNumberlabelDT.setText(self.manager.get_account_number_non_visible())

    def style_sheet_color_limit(self, category):
        limit = self.manager.calculate_daily_limit(category)
        daily_limit = self.manager.get_max_daily_limit(category)
        qss = f"""
        QFrame {{
            background-color: {'rgba(171, 52, 40, 51)' if limit < daily_limit * 0.25 else 'rgb(255, 244, 234)' if limit < daily_limit * 0.50 else 'rgba(40, 171, 52, 51)'};
            border-radius: 5px;
        }}
        QLabel {{
            background-color: transparent;
            color: {'#B3625A' if limit < daily_limit * 0.25 else '#F49E4C' if limit < daily_limit * 0.50 else '#4FBA74'};
        }}
        """
        return qss
    
    def update_total_savings(self):
        self.ui.d_saving_amount.setText(f"{self.manager.get_total_income_of_this_month():,.2f} THB")

# ================================== Budget Planner ==================================

    def setupBudget(self):
        self.limit_ui = self.get_all_children_in_frame_and_map_to_strings(self.ui.planYourBudgetFrame, QLineEdit, LIMIT_LABEL)
        self.set_line_edits_read_only()
        self.update_limit_labels()
        self.ui.planEditButton.clicked.connect(self.enable_limits_edit)
        for ui in self.limit_ui.values():
            ui.textChanged.connect(self.update_total_limit)
        self.setupRoundProgressBars()

    def update_limit_labels(self):
        self.limits = self.manager.get_limits()
        self.ui.averageIncomeLineEdit.setText(str(float(self.manager.get_average_income())))
        # set line edit texts of limits
        for limit, ui in self.limit_ui.items():
            ui.setText(str(self.limits[limit] * 100))
        self.ui.planTotalLineEdit.setText(str(sum(self.limits.values()) * 100))
        if self.limits["saving"] == 0:
            self.ui.budgetAmountLabel.setText(str(float(self.manager.get_average_income())))
        else:
            self.ui.budgetAmountLabel.setText(str(float(self.manager.get_average_income()) - (float(self.manager.get_average_income()) * self.limits["saving"] / 100)))

    def set_line_edits_read_only(self):
        for ui in self.limit_ui.values():
            ui.setReadOnly(True)
        self.ui.averageIncomeLineEdit.setReadOnly(True)

    def toggle_edit_mode(self, enable_editing):
        # Toggle editing mode for all limit UI elements
        for ui in self.limit_ui.values():
            ui.setReadOnly(not enable_editing)
        self.ui.averageIncomeLineEdit.setReadOnly(not enable_editing)

        # Change button text and style
        if enable_editing:
            self.ui.planEditButton.setText("Save")
            self.ui.planEditButton.setStyleSheet("background-color: #4FBA74; color: white;")
            self.ui.planEditButton.clicked.disconnect()
            self.ui.planEditButton.clicked.connect(self.save_limits_setting)
        else:
            self.ui.planEditButton.setText("Edit")
            self.ui.planEditButton.setStyleSheet("background-color: #FFF4EA; color: #F49E4C;")
            self.ui.planEditButton.clicked.disconnect()
            self.ui.planEditButton.clicked.connect(self.enable_limits_edit)

    def enable_limits_edit(self):
        if self.manager.getParentalControl():
            self.nagivateToPin("Enter your Parental PIN")
            self.ui.pinLineEdit.textChanged.connect(self.handleEditBudgetPinPC)
        else:
            self.toggle_edit_mode(True)

    def handleEditBudgetPinPC(self):
        if len(self.ui.pinLineEdit.text()) <= 6 and len(self.ui.pinLineEdit.text()) > 0:
            self.pin_labels[len(self.ui.pinLineEdit.text())-1].setStyleSheet("background-image: url(:/images/image/pin_dot.svg); background-repeat: no-repeat;")
        if len(self.ui.pinLineEdit.text()) == 6:
            pin = self.ui.pinLineEdit.text() + self.__salt
            hash_object = hashlib.sha256(pin.encode())
            pin = hash_object.hexdigest()
            if self.manager.checkPin(pin):
                self.ui.pinLineEdit.textChanged.disconnect()
                self.toggle_edit_mode(True)
                self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
            else:
                self.ui.pinErrorLabel.setText("Incorrect pin")
                self.resetPIN()

    def save_limits_setting(self):
        if self.check_total_limit():
            # Disable editing
            self.toggle_edit_mode(False)
            
            # Save limits
            self.limits_temp = {limit_name: float(ui.text()) / 100 for limit_name, ui in self.limit_ui.items()}
            self.manager.save_limits_and_income(self.limits_temp, float(self.ui.averageIncomeLineEdit.text()))
            self.update_limit_labels()
            self.update_window()
            self.updateRoundProgressBars()
            self.ui.planTotalErrorLabel.setText("")
        else:
            self.ui.planTotalErrorLabel.setText("Total limit is not 100%")

    def update_total_limit(self):
        self.ui.planTotalLineEdit.setText(str(sum([float(ui.text()) for ui in self.limit_ui.values()])))

    def check_total_limit(self):
        return float(self.ui.planTotalLineEdit.text()) == 100.0
    
    def setupRoundProgressBars(self):     
        self.roundprogressbars = []
        self.progressbars_container = self.get_all_children_in_frame_and_map_to_strings(self.ui.plan_budget_all_progresses, QFrame, LIMIT_LABEL)
        self.progressbars_label = self.get_all_children_in_frame_and_map_to_strings(self.ui.plan_budget_all_progresses, QLabel, LIMIT_LABEL)
        for category, ui in self.progressbars_container.items():
            self.roundprogressbar = roundProgressBar(self, category)
            self.roundprogressbar.setObjectName(category + "ProgressBar")
            
            item = ui.layout().itemAt(0)
            if item:
                item.widget().deleteLater()
            
            ui.layout().addWidget(self.roundprogressbar)
            self.roundprogressbar.update_value(self.check_if_limit_is_zero(self.roundprogressbar, category))
            self.progressbars_label[category].setText(str(int(self.cal_used_monthly_limit_category(category) * 100)) + "%")
            self.roundprogressbars.append(self.roundprogressbar)

    def updateRoundProgressBars(self):
        for progressbar in self.roundprogressbars:
            self.check_if_limit_is_zero(progressbar, progressbar.get_category())
            use_monthly_limit = self.cal_used_monthly_limit_category(progressbar.get_category())
            progressbar.update_value(use_monthly_limit)
            self.progressbars_label[progressbar.get_category()].setText(str(int(use_monthly_limit * 100)) + "%")

    def check_if_limit_is_zero(self, progressbar, category):
        percent_in_fraction = self.cal_used_monthly_limit_category(category)
        if percent_in_fraction == 0:
            progressbar.set_gray_color(True)
        else:
            progressbar.set_gray_color(False)
        return percent_in_fraction

    def cal_used_monthly_limit_category(self, category):
        if self.manager.get_max_monthly_limit(category) == 0:
            return 0
        return round(self.manager.calculate_monthly_limit(category)/self.manager.get_max_monthly_limit(category), 2)

# ================================== Direct Transfer ==================================

    def setupTransferPage(self):
        self.selectable_transfer_type = self.get_all_children_in_frame_and_map_to_strings(self.ui.transfertypeframe, QPushButton, TRANSFER_TYPE_LABEL)
        for transfer_type, ui in self.selectable_transfer_type.items():
            ui.clicked.connect(lambda checked=False, transfer_type=transfer_type: self.update_type_selected(transfer_type))
        self.update_type_selected(self.transfer_type_selected)

    def update_type_selected(self, category):
        for transfer_type, ui in self.selectable_transfer_type.items():
            if transfer_type == category:
                self.transfer_type_selected = category
                ui.setStyleSheet("color: #F49E4C")
            else:
                ui.setStyleSheet("color: #C7C7C7")
        
        self.ui.dt_expense_amount.setText(f"{self.manager.calculate_daily_limit(category):,.2f} THB" if not category in ["return", "lend"] else "INF THB" if category == "return" else "-INF THB")

    def handleTransfer(self):
        accountID = self.ui.accountNumberLineEditDT.text()
        amount = self.ui.amountToTransferLineEditDT.text()
        accountIsValid = self.manager.accountNumberIsValid(accountID)
        amountIsValid = self.amountIsValid(amount)
        if not accountIsValid:
            self.ui.accountNumberTransferErrorLabel.setText("Account number is invalid")
        if accountIsValid and amountIsValid:
            self.ui.accountNumberTransferErrorLabel.setText("")
            transaction, transactionID = self.manager.handleTransfer(accountID, float(amount), self.transfer_type_selected)
            print(transaction, transactionID)
            if transaction: # if not over limit and not over balance
                self.nagivateToPin("Enter your PIN")
                self.ui.pinLineEdit.textChanged.connect(lambda: self.handlePinTransfer(accountID, float(amount), transaction, transactionID))
        self.update_window()
        
    def amountIsValid(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                self.ui.amountTransferErrorLabel.setText("")
                return True
            else:
                self.ui.amountTransferErrorLabel.setText("Amount must be greater than 0")
                return False
        except ValueError:
            self.ui.amountTransferErrorLabel.setText("Invalid amount")
            return False
        
    def nagivateToPin(self, message="Enter your PIN"): 
        self.ui.pinLabel.setText(message)
        self.ui.stackedWidget_2.setCurrentIndex(self.page["pin"])
        self.ui.pinErrorLabel.setText("")
        self.resetPIN()

    def handlePinTransfer(self, accountID, amount, transaction, transactionID):
        if len(self.ui.pinLineEdit.text()) <= 6 and len(self.ui.pinLineEdit.text()) > 0:
            self.pin_labels[len(self.ui.pinLineEdit.text())-1].setStyleSheet("background-image: url(:/images/image/pin_dot.svg); background-repeat: no-repeat;")

        if len(self.ui.pinLineEdit.text()) == 6:
            pin = self.ui.pinLineEdit.text() + self.__salt
            hash_object = hashlib.sha256(pin.encode())
            pin = hash_object.hexdigest()
            if self.manager.checkPin(pin):
                self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
                self.transfer(accountID, amount, transaction, transactionID)
                self.ui.pinLineEdit.textChanged.disconnect()
            else:
                self.ui.pinErrorLabel.setText("Incorrect pin")
                self.resetPIN()

    def addNumberToPin(self, num):
        self.ui.pinLineEdit.setText(self.ui.pinLineEdit.text() + num)

    def deletePin(self):
        if len(self.ui.pinLineEdit.text()) > 0:
            self.pin_labels[len(self.ui.pinLineEdit.text())-1].setStyleSheet("background-image: url(:/images/image/pin_no_dot.svg); background-repeat: no-repeat;")
            self.ui.pinLineEdit.setText(self.ui.pinLineEdit.text()[:-1])

    def resetPIN(self):
        self.ui.pinLineEdit.setText("")
        for i in range(6):
            self.pin_labels[i].setStyleSheet("background-image: url(:/images/image/pin_no_dot.svg); background-repeat: no-repeat;")
    def transfer(self, accountID, amount, transaction, transactionID):
        self.manager.transfer(accountID, float(amount), transaction, transactionID)
        self.update_window()
        self.updateRoundProgressBars()
        self.ui.accountNumberLineEditDT.setText("")
        self.ui.amountToTransferLineEditDT.setText("")
        print("Transfer success")
        self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"])


# ================================== History page ==================================
    
    def update_history_page(self, history_type="all"):
        for i in reversed(range(self.ui.transaction_history_frame.layout().count())):
            item = self.ui.transaction_history_frame.layout().itemAt(i)
            if item.widget():
                item.widget().deleteLater()
            elif item.spacerItem():
                self.ui.transaction_history_frame.layout().takeAt(i)
        
        old_date = None
        for transaction in self.manager.getTransactionsHistory():
            transaction_date = transaction.date.strftime("%d/%m/%Y")
            
            if old_date == None or old_date.strftime("%d/%m/%Y") != transaction_date:
                old_date = transaction.date
                date_label = QLabel(self.ui.transaction_history_frame)
                date_label.setObjectName(transaction_date)
                date_label.setText(transaction_date)
                date_label.setStyleSheet("color: #A1A5AD; font-size: 16px; font-weight: bold; font-family: Montserrat;")
                self.ui.transaction_history_frame.layout().addWidget(date_label)
            
            transaction_element = TransactionFrame(self.ui.transaction_history_frame, transaction, self.manager.get_account_number())
            transaction_element.clicked.connect(self.handleTransactionDetail)
            
            if history_type == "expense":
                if self.manager.isSelfExpense(transaction):
                    self.ui.transaction_history_frame.layout().addWidget(transaction_element)
            elif history_type == "income":
                if not self.manager.isSelfExpense(transaction):
                    self.ui.transaction_history_frame.layout().addWidget(transaction_element)
            else:
                self.ui.transaction_history_frame.layout().addWidget(transaction_element)
            print(transaction)
        self.ui.transaction_history_frame.layout().addStretch()
    
    @Slot(Transaction)
    def handleTransactionDetail(self, transaction: Transaction):
        self.ui.stackedWidget.setCurrentIndex(self.page["transactionInfo"])
        self.ui.sender_label.setText(transaction.sender.getName())
        self.ui.reciever_label.setText(transaction.recipient.getName())
        self.ui.date_time_label.setText(transaction.date.strftime("%d/%m/%Y %H:%M:%S"))
        self.ui.transaction_type_label.setText(transaction.__class__.__name__.upper())
        self.ui.total_amount_label.setText(f"{transaction.amount:,.2f}")
        self.ui.spend_limit_label.setText(f"{transaction.spendlimit:,.2f}")
        self.ui.saved_amount_label.setText(f"{transaction.saved:,.2f}")
        self.ui.spend_amount_label.setText(f"{transaction.spend:,.2f}")
        
        for i in reversed(range(self.ui.transactionDetailframe.layout().count())):
            item = self.ui.transactionDetailframe.layout().itemAt(i)
            if item.widget():
                item.widget().deleteLater()
            elif item.spacerItem():
                self.ui.transactionDetailframe.layout().takeAt(i)
        
        for item in transaction.itemList:
            item_frame = TransactionItem(self.ui.transactionDetailframe, item)
            self.ui.transactionDetailframe.layout().addWidget(item_frame)

#=================================== My QR Code ==================================
            
    def createMyQRcode(self):
        AccountID = self.manager.get_account_number()
        myQRcode = qrcode.make(AccountID)
        pil_myQr = myQRcode.get_image()
        self.pil_myQr = self.add_infomation_to_myQRcode(myQRcode, "Owner: "+self.manager.getName()+"\nAccount ID: "+ self.manager.get_account_number_non_visible())
        pixmap = pil_myQr.toqpixmap()
        self.ui.myQRcodeLabel.setPixmap(pixmap)

    def saveMyQRcode(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("Image files (*.png, *.jpg, *.jpeg, *.xpm, *.bmp)")
        file_dialog.setDefaultSuffix("png")
        file_dialog.setWindowTitle("Save My QR Code")
        file_dialog.selectFile("MyQRCode.png")
        file_dialog.setDirectory(str(Path.home()))

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            self.pil_myQr.save(file_path, "PNG")


    def add_infomation_to_myQRcode(self, qr_code_image, additional_info):
        # Create a new image with the QR code and additional information
        new_image = Image.new('RGB', (max(qr_code_image.size[0], 200), qr_code_image.size[1] + 50), color="#4FBA74")
        new_image.paste(qr_code_image, (0, 0))

        # Draw additional information below the QR code
        draw = ImageDraw.Draw(new_image)
        font = ImageFont.truetype("otfs/Montserrat-Regular.ttf", 16)

        # Get the bounding box of the text
        text_bbox = draw.textbbox(((new_image.width - qr_code_image.size[0]) // 2, qr_code_image.size[1]),additional_info, font=font)

        # Draw the text using the bounding box
        draw.text(text_bbox[:2], additional_info, font=font, fill='White')

        return new_image


# ================================== Parental Control ==================================
        
    def pcToggleSetup(self):
        item = self.ui.pcPCMSwitchframe.layout().itemAt(2)
        if item:
            item.widget().deleteLater()
        
        self.parental_control_toggle = ToggleSwitch(width=64)
        self.ui.pcPCMSwitchframe.layout().addWidget(self.parental_control_toggle)
        self.parental_control_toggle.setObjectName("parentalControlToggle")
        self.parental_control_toggle.setChecked(self.manager.getParentalControl())
        self.parental_control_toggle.stateChanged.connect(self.toggleParentalControl)
        # print("at main", self.parental_control_toggle.width(), self.parental_control_toggle.height(), self.parental_control_toggle.parentWidget().width(), self.parental_control_toggle.parentWidget().height())

        self.allow_over_budget_toggle = ToggleSwitch(width=64)
        self.allow_over_budget_toggle.setObjectName("allowOverBudgetToggle")
        self.allow_over_budget_toggle.setEnabled(not self.manager.getParentalControl())
        self.allow_over_budget_toggle.setChecked(self.manager.getAllowOverBudget())
        self.allow_over_budget_toggle.stateChanged.connect(self.toggleAllowOverBudget)
        self.ui.pcAOBSwitchframe.layout().addWidget(self.allow_over_budget_toggle)

    def toggleParentalControl(self): # disable or enable the button
        if self.manager.getParentalControl():
            self.nagivateToPin("Enter your Parental PIN")
            self.ui.pinLineEdit.textChanged.connect(self.handlePinPC)
        else:
            self.nagivateToPin("Create your Parental PIN")
            self.ui.pinLineEdit.textChanged.connect(self.handleCreatePinPC)

    def toggleAllowOverBudget(self):
        self.manager.toggleAllowOverBudget()

    def handlePinPC(self):
        if len(self.ui.pinLineEdit.text()) <= 6 and len(self.ui.pinLineEdit.text()) > 0:
            self.pin_labels[len(self.ui.pinLineEdit.text())-1].setStyleSheet("background-image: url(:/images/image/pin_dot.svg); background-repeat: no-repeat;")
        if len(self.ui.pinLineEdit.text()) == 6:
            pin = self.ui.pinLineEdit.text() + self.__salt
            hash_object = hashlib.sha256(pin.encode())
            pin = hash_object.hexdigest()
            if self.manager.checkPinPC(pin):
                self.ui.pinLineEdit.textChanged.disconnect()
                self.manager.toggleParentalControl()
                self.allow_over_budget_toggle.setEnabled(not self.manager.getParentalControl())
                self.allow_over_budget_toggle.setChecked(False)
                self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
            else:
                self.ui.pinErrorLabel.setText("Incorrect pin")
                self.resetPIN()

    def handleCreatePinPC(self):
        if len(self.ui.pinLineEdit.text()) <= 6 and len(self.ui.pinLineEdit.text()) > 0:
            self.pin_labels[len(self.ui.pinLineEdit.text())-1].setStyleSheet("background-image: url(:/images/image/pin_dot.svg); background-repeat: no-repeat;")
        if len(self.ui.pinLineEdit.text()) == 6:
            pin = self.ui.pinLineEdit.text() + self.__salt
            hash_object = hashlib.sha256(pin.encode())
            pin = hash_object.hexdigest()
            self.manager.setPinPC(pin)
            self.ui.pinLineEdit.textChanged.disconnect()
            # toggle the parental control
            self.manager.toggleParentalControl()
            self.allow_over_budget_toggle.setEnabled(not self.manager.getParentalControl())
            self.allow_over_budget_toggle.setChecked(False)
            self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
    
# ================================== Graph ==================================
    
    def setupGraph(self):
        #set date to today
        self.ui.dateEdit.setDate(self.current_date)
        # default check all radio button

        self.ui.dayradioButton.setChecked(True)
        self.ui.monthradioButton.setChecked(False)
        self.ui.yearradioButton.setChecked(False)

        self.ui.lineradioButton.setChecked(True)
        self.ui.barradioButton.setChecked(False)

        self.ui.allradioButton.setChecked(True)
        self.ui.incomeradioButton.setChecked(False)
        self.ui.expenseradioButton.setChecked(False)

        self.ui.total_expense_amount.setText("0")
        self.ui.total_income_amount.setText("0")
        self.ui.overall_amount.setText("0")

        # add layout to canvasframe
        self.ui.canvasframe.setLayout(QVBoxLayout(self.ui.canvasframe))
        self.ax, self.fig = plt.subplots()
        

    def handleNavigationToGraph(self):
        self.ui.stackedWidget.setCurrentIndex(self.page["graph"])
        self.updateGraph()

    def radio_button_state_changed(self):
        sender = self.sender()  # Get the radio button that triggered the signal
        if sender.isChecked():
            self.updateGraph()

    def updateGraph(self):
        # Check remove canvas from layout
        for i in reversed(range(self.ui.canvasframe.layout().count())):
            item = self.ui.canvasframe.layout().itemAt(i)
            if item.widget():
                item.widget().deleteLater()
            elif item.spacerItem():
                self.ui.canvasframe.layout().takeAt(i)
        
        #get date
        # self.ui.graphview.clear()
        date = self.ui.dateEdit.date()
        # get type
        type = ""
        if self.ui.dayradioButton.isChecked():
            type = "day"
        elif self.ui.monthradioButton.isChecked():
            type = "month"
        elif self.ui.yearradioButton.isChecked():
            type = "year"
        # get graph type
        graph_type = ""
        if self.ui.lineradioButton.isChecked():
            graph_type = "line"
        elif self.ui.barradioButton.isChecked():
            graph_type = "bar"
        # get history type
        history_type = ""
        if self.ui.allradioButton.isChecked():
            history_type = "all"
        elif self.ui.incomeradioButton.isChecked():
            history_type = "income"
        elif self.ui.expenseradioButton.isChecked():
            history_type = "expense"

        data = self.drawGraph(date, type, graph_type, history_type)
        self.updateSummary(data)

    def updateSummary(self, data):
        self.ui.total_expense_amount.setText(f"{data['total_expense']:,.2f}")
        self.ui.total_income_amount.setText(f"{data['total_income']:,.2f}")
        self.ui.overall_amount.setText(f"{data['total_income'] - data['total_expense']:,.2f}")
        if data['total_income'] - data['total_expense'] < 0:
            self.ui.overall_amount.setStyleSheet("color: #B3625A")
            self.ui.overall_THBlabel.setStyleSheet("color: #B3625A")
        else:
            self.ui.overall_amount.setStyleSheet("color: #4FBA74")
            self.ui.overall_THBlabel.setStyleSheet("color: #4FBA74")

    def drawGraph(self, date, type, graph_type, history_type):
        self.ax.clear()
        self.fig.clear()
        data = self.manager.getGraphData(date, type)
        """ data = {
            "income": {income_date: income_amount},
            "expense": {expense_date: expense_amount}
            "total_income": total_income,
            "total_expense": total_expense,
        }
        """
        
        income_data = data["income"]
        expense_data = data["expense"]

        # Extract x and y from both dictionaries
        x = list(income_data.keys())
        y1 = list(income_data.values())
        y2 = list(expense_data.values())

        # Create a figure and axis object
        self.fig, self.ax = plt.subplots()

        # Plot your data
        if graph_type == "line":
            if history_type == "all":
                self.ax.plot(x, y1, label='Income', color="green")
                self.ax.plot(x, y2, label='Expense', color="red")
            elif history_type == "income":
                self.ax.plot(x, y1, label='Income', color="green")
            elif history_type == "expense":
                self.ax.plot(x, y2, label='Expense', color="red")
        if graph_type == "bar":
            if history_type == "all":
                self.ax.bar(x, y1, width=0.4, label='Income', color="green")
                self.ax.bar([i + 0.4 for i in range(len(x))], y2, width=0.4, label='Expense', color="red")
            elif history_type == "income":
                self.ax.bar(x, y1, width=0.4, label='Income', color="green")
            elif history_type == "expense":
                self.ax.bar(x, y2, width=0.4, label='Income', color="red")

        #Customize plot
        self.ax.set_ylabel('Baht', fontsize=9)
        self.ax.legend(fontsize=9)
        self.ax.set_ylim(0)
        self.ax.set_title(f'Summary: {history_type}', fontsize=9)
        
        self.ax.tick_params(axis='x', rotation=90)
        self.ax.tick_params(axis='both', labelsize=5)
        # plot the graph in the graph view
        canvas = FigureCanvas(self.fig)
        # add the canvas to the layout
        self.ui.canvasframe.layout().addWidget(canvas)
        return data


# ================================== Others ==================================

    def setupOthersPage(self):
        self.ui.others_name_label.setText(self.manager.getName())
        self.ui.others_email_label.setText(self.manager.getEmail())
        


# ================================== Camera ==================================

    def start_camera_feed(self):
        # Open the default camera (index 0)
        self.capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        ret, frame = self.capture.read()
        if not ret:
            self.capture = cv2.VideoCapture(0)
        # Set the width of the captured frame to 1200 pixels
        # self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.ui.camera_label.width())
        # Start a timer that triggers the update_camera_feed method at regular intervals
        self.camera_timer = QTimer(self)
        self.camera_timer.timeout.connect(self.update_camera_feed)
        # Start the timer with a timeout value of 50 millisecond (adjust as needed)
        self.camera_timer.start(30)

    @Slot()
    def update_camera_feed(self):
        # Read a frame from the camera
        ret, frame = self.capture.read()
        # Check if the frame was captured successfully
        if not ret:
            print("Failed to capture frame")
            return
        
        frame = self.scale_image_by_height(frame, self.ui.camera_label.height())
        frame = self.center_crop(frame, (self.ui.camera_label.width(), self.ui.camera_label.height()))
        
        # Detect a QR code from the frame
        accountID, bbox, _ = self.detector.detectAndDecode(frame)
        # Check if a QR code is detected
        if accountID:
            # Perform any actions you want with the detected QR code data
            print("QR Code detected:", accountID)
            # Disconnect the timer signal, release the camera, and handle the detected QR code
            self.camera_timer.timeout.disconnect()
            self.capture.release()
            self.handleRedirectFromScanQRCodeToDirectTransfer(accountID)
            return
        # Check if the current page is not the page where QR code scanning is expected
        elif self.ui.stackedWidget.currentIndex() != self.page["scanqrcode"]:
            # Disconnect the timer signal and release the camera
            self.camera_timer.timeout.disconnect()
            self.capture.release()
            return

        # Convert the OpenCV frame to QImage
        height, width, _ = frame.shape
        # Create a deep copy of the frame to ensure continuous memory
        frame_copy = frame.copy()
        qimg = QImage(frame_copy.data, width, height, frame_copy.strides[0], QImage.Format_BGR888)

        # Convert QImage to QPixmap for displaying
        pixmap = QPixmap.fromImage(qimg)

        # Update the QLabel with the new QPixmap
        self.ui.camera_label.setPixmap(pixmap)
    
    def center_crop(self, img, dim):
        """Returns center cropped image
        Args:
        img: image to be center cropped
        dim: dimensions (width, height) to be cropped
        """
        width, height = img.shape[1], img.shape[0]

        # process crop width and height for max available dimension
        crop_width = dim[0] if dim[0]<img.shape[1] else img.shape[1]
        crop_height = dim[1] if dim[1]<img.shape[0] else img.shape[0] 
        mid_x, mid_y = int(width/2), int(height/2)
        cw2, ch2 = int(crop_width/2), int(crop_height/2) 
        crop_img = img[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]
        return crop_img

    def scale_image_by_height(self, img, height, factor=1):
        """Returns resize image by scale factor.
        This helps to retain resolution ratio while resizing.
        Args:
        img: image to be scaled
        factor: scale factor to resize
        """
        ratio = img.shape[1] / img.shape[0]
        return cv2.resize(img, (int(height * ratio * factor), height * factor))
    
    def update_frame(self):
        ret, frame = self.camera.read()
        if ret:

            frame = self.scale_image_by_height(frame, self.ui.camera_label_4.height())
            frame = self.center_crop(frame, (self.ui.camera_label_4.width(), self.ui.camera_label_4.height()))
            # Convert OpenCV frame to QImage
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # Rezise the QImage to fit the QLabel dimensions
            if w != self.ui.camera_label_4.width() or h != self.ui.camera_label_4.height():
                qt_image = qt_image.scaled(self.ui.camera_label_4.width(), self.ui.camera_label_4.height())

            # Update QLabel with the QImage
            self.ui.camera_label_4.setPixmap(QPixmap.fromImage(qt_image))

    def capture_image(self):
        ret, frame = self.camera.read()
        if ret:
            # Save the captured frame
            cv2.imwrite("captured_image.jpg", frame)
            print("Image captured.")
            # Release the camera and stop the timer
            self.camera.release()
            self.timer.stop()
            
            #get the imgae path absolute path
            img_path = os.path.abspath("captured_image.jpg")
            self.file_selected(img_path)
            
            # Delete the captured image
            os.remove(img_path)
            # Navigate to the page where the captured image will be displayed
            self.ui.stackedWidget.setCurrentIndex(self.page["addbill"])

    def closeEvent(self, event):
        # Release the camera when closing the application
        self.camera.release()
        event.accept()

    
# ================================== Add Bill ==================================

    def addSingleBill(self, name='', amount=0):
        self.ui.single_bill_frame.layout().addWidget(BillFrame(self.ui.single_bill_frame, name, amount))
    
    def addBillFromFile(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Image files (*.png *.jpg *.jpeg *.xpm *.bmp)")
        file_dialog.setWindowTitle("Select Image")
        file_dialog.fileSelected.connect(self.file_selected)
        file_dialog.exec()

    def file_selected(self, file_path):
        # Display the selected file path
        # img = Image.open(file_path)
        # text = pytesseract.image_to_string(img, lang='eng+tha')
        # print(text)
        url = "https://ocr.asprise.com/api/v1/receipt"
        res = requests.post(
            url,
            data={    
                'api_key': 'TEST',
                'recognizer': 'auto',
                'ref_no': 'oct_python_123'
            },
            files={
                'file': open(file_path, 'rb')
            }
        )
        data = res.json()
        # with open ("test.json", "r") as f:
        #     data = json.load(f)
            
        for data in data['receipts']:
            for item in data['items']:
                self.addSingleBill(item['description'], float(item['amount']))

    def finishAddBill(self):
        billName = self.ui.billName.text()
        
        items = []
        total = 0
        for item in self.ui.single_bill_frame.children():
            if isinstance(item, BillFrame):
                items.append(item.getValues())
                total += float(item.getValues()[1])
        
        if self.manager.addBill(items, total, billName):
            self.changePage("dashboard")
            self.update_window()
            for item in self.ui.single_bill_frame.children():
                if isinstance(item, BillFrame):
                    item.deleteLater()
            self.ui.billName.setText("")
        else:
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setWindowTitle("Warning")
            warning.setText("Something Went wrong")
            warning.exec()
                
    def handleNaviationToCaptureReceipt(self):
        self.changePage("captureReceipt")
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)
        
        self.camera = cv2.VideoCapture(0)
    

# ================================== Event Handling & Helper Functions ==================================
    def changePage(self, pageIndex):
        self.ui.stackedWidget.setCurrentIndex(self.page[pageIndex])
    
    def changeState(self, state):
        self.ui.stackedWidget_2.setCurrentIndex(self.page[state])

    def eventFilter(self, obj, event):
        if type(event) == QMouseEvent and obj == self.ui.frame_12 and event.button() == Qt.MouseButton.LeftButton:
            self.customPressEvent(event)
            return True
        return super().eventFilter(obj, event)

    def customPressEvent(self, event):
        print("Frame clicked!")
    
    def page_changed_handler(self):
            if self.ui.accountNumberLineEditDT != "":
                self.ui.accountNumberLineEditDT.setText("")
                self.ui.accountNumberLineEditDT.setReadOnly(False)
            if self.ui.stackedWidget.currentIndex() == self.page["budgetplanner"]:
                for progress_bar in self.roundprogressbars:
                    progress_bar.animate_from_zero()

    def page_changed_handler_2(self):
        if self.ui.loginError.text() != "":
            self.ui.loginError.setText("")
        if self.ui.registerConfirmPasswordError.text() != "":
            self.ui.registerConfirmPasswordError.setText("")
   
    def handleNavigationToScanQRCode(self):
        self.ui.stackedWidget.setCurrentIndex(self.page["scanqrcode"])
        self.start_camera_feed()

    def handleRedirectFromScanQRCodeToDirectTransfer(self, accountID):
        self.ui.stackedWidget.setCurrentIndex(self.page["directtransfer"])
        self.ui.accountNumberLineEditDT.setReadOnly(True)
        self.ui.accountNumberLineEditDT.setText(accountID)

    def get_all_child_type_in_frame(self, frame, QType):
        line_edits = []

        def traverse_children(widget):
            for child in widget.children():
                if type(child) == QType and any(name in child.objectName() for name in LOOK_UP_OBJ_NAME):
                    line_edits.append(child)
                elif isinstance(child, (QWidget, QLayout)):
                    traverse_children(child)
                elif isinstance(child, QLayoutItem):
                    item_widget = child.widget()
                    if item_widget:
                        traverse_children(item_widget)

        traverse_children(frame)
        return line_edits
    
    def map_child_to_string(self, line_edits, child_name):
        limit_ui_mapping = {}

        for obj in line_edits:
            obj_name = obj.objectName().lower()
            if "miscellaneous" in obj_name:
                limit_ui_mapping["others"] = obj
            else:
                for name in child_name:  # Use a copy of child_name to allow removal during iteration
                    if name in obj_name:
                        limit_ui_mapping[name] = obj
                        # child_name_copy.remove(name)  # Remove the matched item from child_name
                        break

        return limit_ui_mapping
    
    def get_all_children_in_frame_and_map_to_strings(self, frame, QType, child_name):
        line_edits = self.get_all_child_type_in_frame(frame, QType)
        return self.map_child_to_string(line_edits, child_name)
    
    def handleLogout(self):
        with open(USER_CACHE_FILE, "wb") as f:
            user_cache = ""
            pickle.dump(user_cache, f)
        self.ui.stackedWidget_2.setCurrentIndex(self.page["login"])
    
    def show_info_dialog(self):
        self.info_dialog = InfoDialog(self)
        self.info_dialog.show()
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())