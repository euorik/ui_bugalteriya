import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
from PySide6.QtCore import Qt
from login import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.login_is_successful = False
        self.ui.linepass.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.checkBox.toggled.connect(self.displayPasswordIfChecked)
        self.ui.btnClose.clicked.connect(self.pushButtonClick)

    def displayPasswordIfChecked(self, checked):
        if checked:
            self.ui.linepass.setEchoMode(
            QLineEdit.EchoMode.Normal)
        elif checked == False:
            self.ui.linepass.setEchoMode(
            QLineEdit.EchoMode.Password)

    def pushButtonClick(self):
        if self.login_is_successful == True:
            self.close()
        else:
            answer = QMessageBox.question(
                self, "Выйти из приложения?",
                "Вы уверены, что хотите выйти из приложения?",
                QMessageBox.StandardButton.No | \
                QMessageBox.StandardButton.Yes,
                QMessageBox.StandardButton.Yes)
            if answer == QMessageBox.StandardButton.Yes:
                self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())