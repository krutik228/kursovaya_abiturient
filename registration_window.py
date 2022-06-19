# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from clickableLabel import ClickableLabel


class Ui_RegistrationWindow(object):

    def __init__(self, connection):
        self.connection = connection

    def setupUi(self, RegistrationWindow):
        RegistrationWindow.setObjectName("RegistrationWindow")
        RegistrationWindow.resize(500, 350)
        RegistrationWindow.setStyleSheet("background: rgb(191, 191, 191)")
        self.centralwidget = QtWidgets.QWidget(RegistrationWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.sign_label = QtWidgets.QLabel(self.centralwidget)
        self.sign_label.setGeometry(QtCore.QRect(280, 210, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.sign_label.setFont(font)
        self.sign_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sign_label.setObjectName("reg_btn_2")
        self.sign_label.clicked.connect(self.sign_label)

        self.registration_btn = QtWidgets.QPushButton(self.centralwidget)
        self.registration_btn.setGeometry(QtCore.QRect(102, 150, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)

        self.registration_btn.setFont(font)
        self.registration_btn.setStyleSheet("font: 63 8pt \"Segoe UI Semibold\" ")
        self.registration_btn.setObjectName("registration_btn")
        self.registration_btn.clicked.connect(self.registration)

        self.reg_login_line = QtWidgets.QLineEdit(self.centralwidget)
        self.reg_login_line.setGeometry(QtCore.QRect(130, 60, 250, 30))
        self.reg_login_line.setObjectName("reg_login_line")
        self.reg_pass_line = QtWidgets.QLineEdit(self.centralwidget)
        self.reg_pass_line.setGeometry(QtCore.QRect(130, 110, 250, 30))
        self.reg_pass_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reg_pass_line.setObjectName("reg_pass_line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 210, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        RegistrationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegistrationWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrationWindow)

    def retranslateUi(self, RegistrationWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistrationWindow.setWindowTitle(_translate("RegistrationWindow", "Окно регистрации"))
        self.sign_label.setText(_translate("RegistrationWindow", "Войти"))
        self.registration_btn.setText(_translate("RegistrationWindow", "Регистрация"))
        self.label_2.setText(_translate("RegistrationWindow", "Уже есть аккаунт?"))


    def registration(self):
        reg_login = self.reg_login_line.text()
        reg_password = self.reg_pass_line.text()

        with self.connection.cursor() as cursor:
            try:
                if cursor.execute(f"select login from user where login='{reg_login}'"):
                    print('The user is already registered')
                    self.show_message(text='The user is already registered', title='Registration')
                else:
                    cursor.execute(f"insert into user(login, pass) values('{reg_login}','{reg_password}')")
                    self.show_message(text="Registration completed successfully",
                                      title="Registration")

                    self.connection.commit()
                    print("successfully")
            except Exception as ex:
                print(ex)

    def sign(self):
        print("assf")


    def show_message(self, text, title):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        msg.exec_()
