from PySide6.QtWidgets import QApplication, QMessageBox

class Notification:
    def __init__(self, exceeded_limit, limit_type, allow_over_limit=True):
        self.exceeded_limit = exceeded_limit
        self.limit_type = limit_type
        self.allow_over_limit = allow_over_limit

    def show_notification(self):
        if self.allow_over_limit:
            return self.show_choice()
        else:
            return self.show_warning()
        
    def show_warning(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Limit Exceeded")
        msg.setText(f"The {self.limit_type} limit has been exceeded by {self.exceeded_limit}.")
        msg.exec_()
    
    def show_choice(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Limit Exceeded")
        msg.setText(f"The {self.limit_type} limit has been exceeded by {self.exceeded_limit}.")
        msg.setInformativeText("Would you like to proceed?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        ret = msg.exec_()
        return ret == QMessageBox.Ok
        
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)

#     # Example usage:
#     notification = Notification(10, "food")
#     notification.show_notification()

#     sys.exit(app.exec_())
