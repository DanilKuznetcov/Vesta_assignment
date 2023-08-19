# -*- coding: utf-8 -*-

from PyQt4 import QtGui as qt
from PyQt4.QtCore import Qt as qt_allignes
from PyQt4.QtCore import SIGNAL

class Create(qt.QWidget):
    def __init__(self, parent=None):
        super(Create, self).__init__(parent)
        self.initUI()
    def initUI(self):
        self.resize(200, 100)
        self.setWindowTitle(u'Восстановление пароля')

        self.maleEdit = qt.QLineEdit()
        self.maleEdit.setPlaceholderText(u"Адрес электронной почты")

        self.confirm = qt.QPushButton(self)
        self.confirm.setText(u"Сменить пароль")
        self.confirm.setStyleSheet("border-radius : 10; padding: 5px; border : 2px solid grey; background-color: rgb(169,169,169)")


        self.cancel = qt.QPushButton(self)
        self.cancel.setText(u"Отмена")
        self.cancel.setStyleSheet("border-radius : 10; padding: 5px; border : 2px solid red; background-color: rgb(220,20,60)")

        self.ver_Layout = qt.QVBoxLayout()

        self.ver_Layout.addWidget(self.maleEdit)

        self.buttons_Layout = qt.QHBoxLayout()
        self.buttons_Layout.addWidget(self.confirm)
        self.buttons_Layout.addWidget(self.cancel)
        self.ver_Layout.addLayout(self.buttons_Layout)

        self.setLayout(self.ver_Layout)

    def show_myself(self, event):
        self.show()
    def quitApp (self):
        pass
        # db.name().close()
        # sys.exit(0)