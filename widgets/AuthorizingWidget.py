# -*- coding: utf-8 -*-

from PyQt4 import QtGui as qt
from PyQt4.QtCore import Qt as qt_allignes
import RegistrationWidget, ResetPasswordWidget

class Create(qt.QWidget):
    def __init__(self, parent=None):
        super(Create, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(400, 200)
        self.setWindowTitle(u'Окно авторизации')

        self.nameEdit = qt.QLineEdit()
        self.nameEdit.setPlaceholderText(u"Имя пользователя")
        self.password_edit = qt.QLineEdit()
        self.password_edit.setPlaceholderText(u"Пароль")

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

        self.remembeer_checker = qt.QCheckBox(u"Запомнить меня")
        self.show_password = qt.QCheckBox(u"Показать пароль")

        self.forgot_password = qt.QLabel(u"Забыли пароль?")
        # self.forgot_password.mousePressEvent = self.doSomething
        self.forgot_password.setStyleSheet("color: blue; text-decoration: underline; vertical-align: middle;")


        self.ver_Layout = qt.QVBoxLayout()

        self.ver_Layout.addWidget(self.nameEdit)
        self.ver_Layout.addWidget(self.password_edit)

        self.buttons_Layout = qt.QHBoxLayout()
        self.buttons_Layout.addWidget(self.sign_in)
        self.buttons_Layout.addWidget(self.sign_up)
        self.buttons_Layout.addWidget(self.cancel)
        self.ver_Layout.addLayout(self.buttons_Layout)

        self.ver_Layout.addWidget(self.remembeer_checker, 0, qt_allignes.AlignCenter)
        self.ver_Layout.addWidget(self.show_password, 0, qt_allignes.AlignCenter)

        self.ver_Layout.addWidget(self.forgot_password, 0, qt_allignes.AlignCenter)

        self.setLayout(self.ver_Layout)

    # def doSomething(self, event):
    #     self.show()

    def authorizing(self):
        self.close()


    def quitApp (self):
        pass
        # db.name().close()
        # sys.exit(0)

    # def quitApp (self):
    #     pass
    #     # db.name().close()
    #     # sys.exit(0)
    #
