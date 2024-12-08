# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import style_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 731)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.app_ui = QFrame(self.centralwidget)
        self.app_ui.setObjectName(u"app_ui")
        self.app_ui.setGeometry(QRect(80, 10, 550, 700))
        self.app_ui.setStyleSheet(u"QFrame#app_ui{\n"
"	border-image: url(:/image/image/droblex.png);\n"
"	border-radius: 18px;\n"
"	border-color: rgb(255, 255, 127);\n"
"}")
        self.app_ui.setFrameShape(QFrame.Shape.StyledPanel)
        self.app_ui.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.app_ui)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(16, 657, 520, 30))
        font = QFont()
        font.setFamilies([u"SimSun"])
        font.setPointSize(14)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.label_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3.setTextFormat(Qt.TextFormat.PlainText)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame = QFrame(self.app_ui)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(150, 250, 250, 170))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Sitka"])
        font1.setPointSize(8)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.linelogin = QLineEdit(self.frame)
        self.linelogin.setObjectName(u"linelogin")
        font2 = QFont()
        font2.setPointSize(8)
        self.linelogin.setFont(font2)
        self.linelogin.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.linelogin)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setFamilies([u"Sitka"])
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.linepass = QLineEdit(self.frame)
        self.linepass.setObjectName(u"linepass")
        self.linepass.setFont(font2)
        self.linepass.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.linepass)

        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font3)

        self.verticalLayout.addWidget(self.checkBox)

        self.pushLogin = QPushButton(self.frame)
        self.pushLogin.setObjectName(u"pushLogin")
        self.pushLogin.setFont(font1)

        self.verticalLayout.addWidget(self.pushLogin)

        self.label_4 = QLabel(self.app_ui)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(15, 12, 480, 30))
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.label_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4.setTextFormat(Qt.TextFormat.PlainText)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnClose = QPushButton(self.app_ui)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setGeometry(QRect(497, 11, 42, 32))
        icon = QIcon(QIcon.fromTheme(u"window-close"))
        self.btnClose.setIcon(icon)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Welcome to the author's project Yanezh Vecnikar!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushLogin.setText(QCoreApplication.translate("MainWindow", u"\u0412\u041e\u0419\u0422\u0418", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u0430\u0448\u043d\u044f\u044f \u0411\u0443\u0433\u0430\u043b\u0442\u0435\u0440\u0438\u044f", None))
        self.btnClose.setText("")
    # retranslateUi

