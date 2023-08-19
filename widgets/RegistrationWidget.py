# -*- coding: utf-8 -*-

from PyQt4 import QtGui as qt
from PyQt4.QtCore import Qt as qt_allignes

class Create(qt.QWidget):
    def __init__(self, parent=None):
        super(Create, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(300, 200)
        self.setWindowTitle(u'Регистрация')

        self.name_edit = qt.QLineEdit()
        self.name_edit.setPlaceholderText(u"Имя пользователя")
        self.password_edit = qt.QLineEdit()
        self.password_edit.setPlaceholderText(u"Пароль")
        self.repeat_password_edit = qt.QLineEdit()
        self.repeat_password_edit.setPlaceholderText(u"Повторите пароль")
        self.birthday_label = qt.QLabel(u"Дата рождения:")
        self.calendar = qt.QDateEdit()
        self.calendar.setDisplayFormat("dd.MM.yyyy")
        self.calendar.setCalendarPopup(True)

        self.confirm = qt.QPushButton(self)
        self.confirm.setText(u"Ок")
        self.confirm.setStyleSheet("border-radius : 10; padding: 5px; border : 2px solid rgb(50,205,50); background-color: rgb(127,255,0)")

        self.cancel = qt.QPushButton(self)
        self.cancel.setText(u"Отмена")
        self.cancel.setStyleSheet("border-radius : 10; padding: 5px; border : 2px solid red; background-color: rgb(220,20,60)")

        self.ver_Layout = qt.QVBoxLayout()

        self.ver_Layout.addWidget(self.name_edit)
        self.ver_Layout.addWidget(self.password_edit)
        self.ver_Layout.addWidget(self.repeat_password_edit)

        self.birthday_Layout = qt.QHBoxLayout()
        self.birthday_Layout.addWidget(self.birthday_label)
        self.birthday_Layout.addWidget(self.calendar)
        self.ver_Layout.addLayout(self.birthday_Layout)


        self.buttons_Layout = qt.QHBoxLayout()
        self.buttons_Layout.addWidget(self.confirm)
        self.buttons_Layout.addWidget(self.cancel)
        self.ver_Layout.addLayout(self.buttons_Layout)

        self.setLayout(self.ver_Layout)


    def quitApp (self):
        pass
        # db.name().close()
        # sys.exit(0)