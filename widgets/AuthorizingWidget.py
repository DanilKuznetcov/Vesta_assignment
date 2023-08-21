# -*- coding: utf-8 -*-

from PyQt4 import QtGui as qt
from PyQt4.QtCore import Qt as qt_allignes
import Configurations
from Configurations import cursor
import os

class Create(qt.QWidget):
    def __init__(self, parent=None):
        super(Create, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(300, 200)
        self.setWindowTitle(u'Авторизация')

        self.nameEdit = qt.QLineEdit()
        self.nameEdit.setPlaceholderText(u"Имя пользователя")

        self.passwordEdit = qt.QLineEdit()
        self.passwordEdit.setEchoMode(qt.QLineEdit.Password)
        self.passwordEdit.setPlaceholderText(u"Пароль")

        self.sign_in = qt.QPushButton(self)
        self.sign_in.setText(u"Войти")
        self.sign_in.setStyleSheet("border-radius : 10; padding: 5px; border : 2px solid rgb(50,205,50); background-color: rgb(127,255,0)")

        self.sign_up = qt.QPushButton(self)
        self.sign_up.setText(u"Регистрация")
        self.sign_up.resize(100,32)
        self.sign_up.setStyleSheet("border-radius : 10; padding: 5px; border : 2px solid grey; background-color: rgb(169,169,169)")

        self.cancel = qt.QPushButton(self)
        self.cancel.setText(u"Отмена")
        self.cancel.setStyleSheet("border-radius : 10; padding: 5px; border : 2px solid red; background-color: rgb(220,20,60)")
        self.cancel.clicked.connect(self.close)

        self.rememberMeChecker = qt.QCheckBox(u"Запомнить меня")
        self.show_password = qt.QCheckBox(u"Показать пароль")
        self.show_password.stateChanged.connect(self.changePasswordVisibility)

        self.forgot_password = qt.QLabel(u"Забыли пароль?")
        self.forgot_password.setStyleSheet("color: blue; text-decoration: underline; vertical-align: middle;")


        self.ver_Layout = qt.QVBoxLayout()

        self.ver_Layout.addWidget(self.nameEdit)
        self.ver_Layout.addWidget(self.passwordEdit)

        self.buttons_Layout = qt.QHBoxLayout()
        self.buttons_Layout.addWidget(self.sign_in)
        self.buttons_Layout.addWidget(self.sign_up)
        self.buttons_Layout.addWidget(self.cancel)
        self.ver_Layout.addLayout(self.buttons_Layout)

        self.ver_Layout.addWidget(self.rememberMeChecker, 0, qt_allignes.AlignCenter)
        self.ver_Layout.addWidget(self.show_password, 0, qt_allignes.AlignCenter)

        self.ver_Layout.addWidget(self.forgot_password, 0, qt_allignes.AlignCenter)

        self.setLayout(self.ver_Layout)

    def checkCredentials(self, user, password):
        cursor.execute("select count(*) from User where Name=\"{}\" and Password=\"{}\";".format(user, password))
        response = cursor.fetchall()
        if response[0][0] >= 1:
            return True
        else:
            return False

    employeesBirthdayListWidget, popupReminderWidget = object, object
    def authorize(self, from_cnfg=False):
        # at the first authorization (if pressed remember me) - creds will be saved in Configuration.py
        if from_cnfg == True:
            user = Configurations.username
            password = Configurations.password
        else:
            user = self.nameEdit.text()
            password = self.passwordEdit.text()

        if self.checkCredentials(user, password):
            if self.rememberMeChecker.isChecked():
                with open("Configurations.py", "r+") as f:
                    lines = f.readlines()
                    lines[-2] = u"username = u\"{}\"\n".format(user)
                    lines[-1] = u"password = u\"{}\"".format(password)
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
            self.close()
            self.employeesBirthdayListWidget.user_name.setText(user)
            self.employeesBirthdayListWidget.show()
            self.popupReminderWidget.show()
        else:
            popup = qt.QMessageBox(qt.QMessageBox.Critical,
                                      u"Ошибка авторизации",
                                      u"Пользователь с такими данными не найден",
                                      qt.QMessageBox.Ok,
                                      self)
            popup.show()

    def changePasswordVisibility(self):
        if self.show_password.isChecked():
            self.passwordEdit.setEchoMode(qt.QLineEdit.Normal)
        else:
            self.passwordEdit.setEchoMode(qt.QLineEdit.Password)