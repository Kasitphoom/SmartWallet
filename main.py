import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFrame, QTreeWidget, QTreeWidgetItem, QLineEdit, QLayoutItem, QLayout, QCheckBox, QFileDialog
from PySide6.QtCore import QSize, QRect, Qt, Slot, QTimer
from PySide6.QtGui import QFont, QFontDatabase, QMouseEvent, QImage, QPixmap
from mainwindow import Ui_MainWindow

from py_toggle import ToggleSwitch

from pathlib import Path

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

from obj.walletmanager import WalletManager
from obj.account import Account
from obj.roundprogressbar import roundProgressBar
from obj.WalletManagerObject import TransactionFrame

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

import pickle

import hashlib
import cv2
import qrcode

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

class MainWindow(QMainWindow):
    def __init__(self, manager: WalletManager):
        super().__init__()
        self.manager = manager
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
            # stacked widget 2
            "main": 0,
            "login": 1,
            "register": 2
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
        elif manager.check_accounts(user_cache):
            self.manager.set_account(user_cache)
            self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
            self.update_window()
            # set initial budget page
            self.setupBudget()
            self.setupOthersPage()
            self.setupTransferPage()
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
        self.ui.dashboardButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"]))
        self.ui.ftransferButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["transfer"]))
        self.ui.fbudgetplannerButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["budgetplanner"]))
        self.ui.budgetplannerButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["budgetplanner"]))
        self.ui.redirectToRegisterButton.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(self.page["register"]))
        self.ui.redirectToLoginButton.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(self.page["login"]))
        self.ui.transferbackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"]))
        self.ui.navigateToDirectTransferButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["directtransfer"]))
        self.ui.navigateToDirectQrcodeButton.clicked.connect(self.handleNavigationToScanQRCode)
        self.ui.fhistoryButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["history"]))
        self.ui.historyButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["history"]))
        self.ui.othersButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["others"]))
        self.ui.setting_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["setting"]))
        self.ui.fmyqrButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["myQRcode"]))
        self.ui.parental_control_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["parentalcontrol"]))
        self.ui.graphButton.clicked.connect(self.handleNavigationToGraph)
        


        # back buttons
        self.ui.budgetBackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"]))
        self.ui.dicrectTransferBackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["transfer"]))
        self.ui.historybackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"]))
        self.ui.othersBackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"]))
        self.ui.scanQRCodeBackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["transfer"]))
        self.ui.settingBackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["others"]))
        self.ui.transferbackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"]))
        self.ui.parentalControlBackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["setting"]))


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
            
            self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
            self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"])
            self.update_window()
            self.setupBudget()
            self.setupTransferPage()
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
        self.toggle_edit_mode(True)

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
            progressbar.update_value(self.cal_used_monthly_limit_category(progressbar.get_category()))
            self.progressbars_label[progressbar.get_category()].setText(str(int(self.cal_used_monthly_limit_category(progressbar.get_category()) * 100)) + "%")

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
            if self.manager.handleTransfer(accountID, float(amount), self.transfer_type_selected):
                self.update_window()
                self.updateRoundProgressBars()
                self.ui.accountNumberLineEditDT.setText("")
                self.ui.amountToTransferLineEditDT.setText("")
                print("Transfer success")
                self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"])
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
            
            if history_type == "expense":
                if transaction.sender.getID() == self.manager.get_account_number():
                    self.ui.transaction_history_frame.layout().addWidget(TransactionFrame(self.ui.transaction_history_frame, transaction, self.manager.get_account_number()))
            elif history_type == "income":
                if transaction.recipient.getID() == self.manager.get_account_number():
                    self.ui.transaction_history_frame.layout().addWidget(TransactionFrame(self.ui.transaction_history_frame, transaction, self.manager.get_account_number()))
            else:
                self.ui.transaction_history_frame.layout().addWidget(TransactionFrame(self.ui.transaction_history_frame, transaction, self.manager.get_account_number()))
            print(transaction)
        self.ui.transaction_history_frame.layout().addStretch()

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
        self.parental_control_toggle.setObjectName("parentalControlToggle")
        # self.parental_control_toggle.setChecked(self.manager.getParentalControl())
        # self.parental_control_toggle.stateChanged.connect(self.toggleParentalControl)
        self.ui.pcPCMSwitchframe.layout().addWidget(self.parental_control_toggle)

        self.allow_over_budget_toggle = ToggleSwitch(width=64)
        self.allow_over_budget_toggle.setObjectName("allowOverBudgetToggle")
        # self.allow_over_budget_toggle.setChecked(self.manager.getAllowOverBudget())
        # self.allow_over_budget_toggle.stateChanged.connect(self.toggleAllowOverBudget)
        self.ui.pcAOBSwitchframe.layout().addWidget(self.allow_over_budget_toggle)

    def toggleParentalControl(self):
        pass

    def toggleAllowOverBudget(self):
        pass
    
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

    def handleNavigationToGraph(self):
        self.ui.stackedWidget.setCurrentIndex(self.page["graph"])
        self.updateGraph()

    def updateGraph(self):
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

        self.drawGraph(date, type, graph_type, history_type)

        #update total income and expense

        


        # for transaction in self.manager.getTransactionsHistory():
        #     print(transaction.date, transaction.time, transaction.amount)
            # if transaction.type == "expense":
            #     self.ui.total_expense_amount.setText(str(float(self.ui.total_expense_amount.text()) + transaction.amount))
            # elif transaction.type == "income":
            #     self.ui.total_income_amount.setText(str(float(self.ui.total_income_amount.text()) + transaction.amount))
        # get data within 
        # data = self.manager.getGraphData(date,type, history_type)
        # # update graph
        # self.updateGraphData(data, graph_type)

    def drawGraph(self, date, type, graph_type, history_type):
        data = self.manager.getGraphData(date, type)
        """ data = {
            "income": {income_date: income_amount},
            "expense": {expense_date: expense_amount}
        }
        """
        # Step 2: Prepare your data
        income_data = data["income"]
        expense_data = data["expense"]

        # Step 3: Extract x and y from both dictionaries
        x = list(income_data.keys())
        y1 = list(income_data.values())
        y2 = list(expense_data.values())

        # Step 4: Create a figure and axis object
        fig, ax = plt.subplots()

        # Step 5: Plot your data
        if (graph_type == "line"):
            if (history_type == "all"):
                ax.plot(x, y1, label='Income')
                ax.plot(x, y2, label='Expense')
            elif (history_type == "income"):
                ax.plot(x, y1, label='Income')
            elif (history_type == "expense"):
                ax.plot(x, y2, label='Expense')
        elif (graph_type == "bar"):
            ax.bar(x, y1, width=0.4, label='Income')
            ax.bar([i + 0.4 for i in range(len(x))], y2, width=0.4, label='Expense')

        # Step 6: Customize your plot
        ax.set_xlabel('Categories')
        ax.set_ylabel('Values')
        ax.set_title('Bar Graph Example')
        ax.legend(fontsize=9)

        ax.tick_params(axis='x', rotation=90)
        ax.tick_params(axis='both', labelsize=5)
        # Step 7: plot the graph in the graph view
        canvas = FigureCanvas(fig)
        layout = QVBoxLayout(self.ui.canvasframe)
        layout.addWidget(canvas)


        

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

# ================================== Event Handling & Helper Functions ==================================

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
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = WalletManager()
    main = MainWindow(manager)
    main.show()
    sys.exit(app.exec())