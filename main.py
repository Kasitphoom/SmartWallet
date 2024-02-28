import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFrame, QTreeWidget, QTreeWidgetItem
from PySide6.QtCore import QSize, QRect, Qt
from PySide6.QtGui import QFont, QFontDatabase, QMouseEvent
from mainwindow import Ui_MainWindow

from pathlib import Path

from obj.walletmanager import WalletManager
from obj.account import Account

import pickle

import hashlib

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
        self.page = {
            # stacked widget
            "dashboard": 0,
            "transfer": 1,
            "budgetplanner": 2,
            # stacked widget 2
            "main": 0,
            "login": 1,
            "register": 2
        }
        

        # Add fonts in QFontDatabase before setting up the UI
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Font Awesome 6 Free-Solid-900.otf").as_posix())
        QFontDatabase.addApplicationFont(Path.joinpath(Path(__file__).parent, "otfs/Montserrat-VariableFont_wght.ttf").as_posix())
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        if user_cache == "":
            self.ui.stackedWidget_2.setCurrentIndex(self.page["login"])
        elif manager.check_accounts(user_cache):
            self.manager.set_account(user_cache)
            self.ui.stackedWidget_2.setCurrentIndex(self.page["main"])
            self.update_window()
        else:
            self.ui.stackedWidget_2.setCurrentIndex(self.page["login"])
        
        self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"])
        self.ui.frame_10.installEventFilter(self)
        
        # login page
        self.ui.loginButton.clicked.connect(self.handleLogin)
        self.ui.registerButton.clicked.connect(self.handleRegister)
        
        # show/hide account number
        self.ui.eyeButton.clicked.connect(self.handleAccountNumberVisibility)
        
        # buttons to change page
        self.ui.dashboardButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"]))
        self.ui.ftransferButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["transfer"]))
        self.ui.fbudgetplannerButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["budgetplanner"]))
        self.ui.budgetplannerButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["budgetplanner"]))
        self.ui.redirectToRegisterButton.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(self.page["register"]))
        self.ui.redirectToLoginButton.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(self.page["login"]))

        # handle page change
        self.ui.stackedWidget_2.currentChanged.connect(self.page_changed_handler) 

        # set initial budget page
        self.limit_ui = {
            "housing": self.ui.planHousingLineEdit,
            "food": self.ui.planFoodLineEdit,
            "transport": self.ui.planTransportLineEdit,
            "entertainment": self.ui.planEntertainmentLineEdit,
            "healthcare": self.ui.planHealthcareLineEdit,
            "others": self.ui.planMiscellaneousLineEdit,
            "saving": self.ui.planSavingLineEdit,
        }
        self.update_limit_labels()
        self.ui.planEditButton.clicked.connect(self.enable_limits_edit)
        for ui in self.limit_ui.values():
            ui.textChanged.connect(self.update_total_limit)


        
    def handleLogin(self):
        email = self.ui.loginEmailLineEdit.text()
        password = self.ui.loginPasswordLineEdit.text() + self.__salt
        
        hash_object = hashlib.sha256(password.encode())
        password = hash_object.hexdigest()
        
        print(password)
        
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
        else:
            self.ui.loginError.setText("Invalid email or password")
            print("Invalid email or password")

    def handleRegister(self):
        fullname = self.ui.registerFullNameENLineEdit.text()
        email = self.ui.registerEmailLineEdit.text()
        password = self.ui.registerPasswordLineEdit.text() + self.__salt
        confirm_password = self.ui.registerConfirmPasswordLineEdit.text() + self.__salt
        
        if password != confirm_password:
            print("Password does not match")
            self.ui.registerConfirmPasswordError.setText("Password does not match")
            return
        
        hash_object = hashlib.sha256(password.encode())
        password = hash_object.hexdigest()
        
        self.manager.register_account(fullname, email, password)
        self.ui.stackedWidget_2.setCurrentIndex(self.page["login"])

    def update_window(self):
        self.ui.d_balance_amount.setText(self.manager.get_balance() + " THB")
        
        # set text as this format XXX-X-1234-X
        self.ui.accountNumberlabel.setText(self.manager.get_account_number_non_visible())
        
        # set balance
        self.ui.d_balance_amount.setText(self.manager.get_balance() + " THB")
        
        self.update_daily_limit()
        self.update_total_month_expense()

    def eventFilter(self, obj, event):
        if type(event) == QMouseEvent and obj == self.ui.frame_12 and event.button() == Qt.MouseButton.LeftButton:
            self.customPressEvent(event)
            return True
        return super().eventFilter(obj, event)

    def customPressEvent(self, event):
        print("Frame clicked!")
    
    def handleAccountNumberVisibility(self):
        self.account_number_visibility = not self.account_number_visibility
        if self.account_number_visibility:
            self.ui.accountNumberlabel.setText(self.manager.get_account_number_visible())
        else:
            self.ui.accountNumberlabel.setText(self.manager.get_account_number_non_visible())
            
    def style_sheet_color_limit(self, category):
        limit = self.manager.calculate_daily_limit(category)
        daily_limit = self.manager.get_max_daily_limit(category)
        qss = f"""
        QFrame {{
            background-color: {'rgba(171, 52, 40, 51)' if limit < daily_limit * 0.25 else 'rgba(171, 52, 40, 51)' if limit < daily_limit * 0.50 else 'rgba(40, 171, 52, 51)'};
            border-radius: 5px;
        }}
        QLabel {{
            background-color: transparent;
            color: {'#B3625A' if limit < daily_limit * 0.25 else '#F49E4C' if limit < daily_limit * 0.50 else '#4FBA74'};
        }}
        """
        return qss
    
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

    def page_changed_handler(self):
        if self.ui.loginError.text() != "":
            self.ui.loginError.setText("")
        if self.ui.registerConfirmPasswordError.text() != "":
            self.ui.registerConfirmPasswordError.setText("")

    def update_limit_labels(self):
        self.limits = self.manager.get_limits()
        self.ui.averageIncomeLineEdit.setText(str(float(self.manager.get_average_income())))
        # set line edit texts of limits
        for limit, ui in self.limit_ui.items():
            ui.setText(str(self.limits[limit]))
        self.ui.planTotalLineEdit.setText(str(sum(self.limits.values())))

    def enable_limits_edit(self):
        # enable editing
        for ui in self.limit_ui.values():
            ui.setReadOnly(False)
        self.ui.averageIncomeLineEdit.setReadOnly(False)
        # change to save button
        self.ui.planEditButton.setText("Save")
        self.ui.planEditButton.setStyleSheet("background-color: #4FBA74; color: white;")
        self.ui.planEditButton.clicked.connect(self.save_limits_setting)

    def save_limits_setting(self):
        if self.check_total_limit():
            # disable editing
            for ui in self.limit_ui.values():
                ui.setReadOnly(True)
            self.ui.averageIncomeLineEdit.setReadOnly(True)
            # change to edit button
            self.ui.planEditButton.setText("Edit")
            self.ui.planEditButton.setStyleSheet("background-color: #FFF4EA; color: #F49E4C;")
            self.ui.planEditButton.clicked.connect(self.enable_limits_edit)
            # save limits
            self.limits_temp = {}
            for limit_name, ui in self.limit_ui.items():
                self.limits_temp[limit_name] = float(ui.text()) / 100
            self.manager.save_limits_and_income(self.limits_temp, float(self.ui.averageIncomeLineEdit.text()))
            self.update_limit_labels()
            self.ui.planTotalErrorLabel.setText("")
        else:
            print("Total limit is not 100%")
            self.ui.planTotalErrorLabel.setText("Total limit is not 100%")

    def update_total_limit(self):
        self.ui.planTotalLineEdit.setText(str(sum([float(ui.text()) for ui in self.limit_ui.values()])))

    def check_total_limit(self):
        return float(self.ui.planTotalLineEdit.text()) == 100.0




        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = WalletManager()
    main = MainWindow(manager)
    main.show()
    sys.exit(app.exec())