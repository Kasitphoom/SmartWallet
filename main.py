import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFrame, QTreeWidget, QTreeWidgetItem, QLineEdit, QLayoutItem, QLayout
from PySide6.QtCore import QSize, QRect, Qt, Slot, QTimer
from PySide6.QtGui import QFont, QFontDatabase, QMouseEvent, QImage, QPixmap
from mainwindow import Ui_MainWindow

from pathlib import Path

from obj.walletmanager import WalletManager
from obj.account import Account
from obj.roundprogressbar import roundProgressBar

import pickle

import hashlib
import cv2

LIMIT_LABEL = ["housing", "food", "transport", "entertainment", "healthcare", "saving"]
TRANSFER_TYPE_LABEL = ["housing", "food", "transport", "entertainment", "healthcare", "saving", "return", "lend", "others"]
LOOK_UP_OBJ_NAME = ["LineEdit", "progressbar"]

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
        # self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)
        self.detector = cv2.QRCodeDetector()
        self.page = {
            # stacked widget
            "dashboard": 0,
            "transfer": 1,
            "budgetplanner": 2,
            "directtransfer": 3,
            "history": 4,
            "scanqrcode": 5,
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
        self.ui.transferbackButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["dashboard"]))
        self.ui.navigateToDirectTransferButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(self.page["directtransfer"]))
        self.ui.navigateToDirectQrcodeButton.clicked.connect(self.handleNavigationToScanQRCode)
        
        # handle page change
        self.ui.stackedWidget_2.currentChanged.connect(self.page_changed_handler_2)
        self.ui.stackedWidget.currentChanged.connect(self.page_changed_handler)
        
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

    def update_limit_labels(self):
        self.limits = self.manager.get_limits()
        self.ui.averageIncomeLineEdit.setText(str(float(self.manager.get_average_income())))
        # set line edit texts of limits
        for limit, ui in self.limit_ui.items():
            ui.setText(str(self.limits[limit]))
        self.ui.planTotalLineEdit.setText(str(sum(self.limits.values())))
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
    
    def setupBudget(self):
        self.limit_ui = self.get_all_children_in_frame_and_map_to_strings(self.ui.planYourBudgetFrame, QLineEdit, LIMIT_LABEL)
        self.set_line_edits_read_only()
        self.update_limit_labels()
        self.ui.planEditButton.clicked.connect(self.enable_limits_edit)
        for ui in self.limit_ui.values():
            ui.textChanged.connect(self.update_total_limit)
        self.setupRoundProgressBars()

    def setupRoundProgressBars(self):
        self.roundprogressbars = []
        self.progressbars_container = self.get_all_children_in_frame_and_map_to_strings(self.ui.plan_budget_all_progresses, QFrame, LIMIT_LABEL)
        self.progressbars_label = self.get_all_children_in_frame_and_map_to_strings(self.ui.plan_budget_all_progresses, QLabel, LIMIT_LABEL)
        for category, ui in self.progressbars_container.items():
            self.roundprogressbar = roundProgressBar(self, category)
            self.roundprogressbar.setObjectName(category + "ProgressBar")
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
        
    def handleNavigationToScanQRCode(self):
        self.ui.stackedWidget.setCurrentIndex(self.page["scanqrcode"])
        self.start_camera_feed()

    def start_camera_feed(self):
        # Open the default camera (index 0)
        self.capture = cv2.VideoCapture(0)
        # Set the width of the captured frame to 1200 pixels
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1250)
        # Start a timer that triggers the update_camera_feed method at regular intervals
        self.camera_timer = QTimer(self)
        self.camera_timer.timeout.connect(self.update_camera_feed)
        # Start the timer with a timeout value of 50 millisecond (adjust as needed)
        self.camera_timer.start(50)

    @Slot()
    def update_camera_feed(self):
        # Read a frame from the camera
        ret, frame = self.capture.read()
        # Check if the frame was captured successfully
        if not ret:
            print("Failed to capture frame")
            return

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

        # Crop the frame to remove the excess part (adjust as needed)
        crop_rect = QRect(550, 0, self.ui.camera_label.width(), self.ui.camera_label.height())
        cropped_frame = frame[crop_rect.y():crop_rect.y() + crop_rect.height(), crop_rect.x():crop_rect.x() + crop_rect.width()].copy()

        # Convert the OpenCV frame to QImage
        height, width, _ = cropped_frame.shape
        qimg = QImage(cropped_frame.data, width, height, cropped_frame.strides[0], QImage.Format_BGR888)

        # Convert QImage to QPixmap for displaying
        pixmap = QPixmap.fromImage(qimg)

        # Update the QLabel with the new QPixmap
        self.ui.camera_label.setPixmap(pixmap)

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



        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = WalletManager()
    main = MainWindow(manager)
    main.show()
    sys.exit(app.exec())