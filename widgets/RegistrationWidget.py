# -*- coding: utf-8 -*-

from PyQt4 import QtGui as qt
from Configurations import cursor, connection

class Create(qt.QWidget):
    def __init__(self, parent=None):
        super(Create, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(400, 250)
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
        self.confirm.clicked.connect(self.registrate)

        self.cancel = qt.QPushButton(self)
        self.cancel.setText(u"Отмена")
        self.cancel.setStyleSheet("border-radius : 10; padding: 5px; border : 2px solid red; background-color: rgb(220,20,60)")
        self.cancel.clicked.connect(self.close)

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

    def registrate(self):
        user = self.name_edit.text()
        password = self.password_edit.text()
        repeat_password = self.repeat_password_edit.text()
        date = str(self.calendar.text())
        if (password != repeat_password):
            popup = qt.QMessageBox(qt.QMessageBox.Critical,
                                   u"Ошибка регистрации",
                                   u"Пароли не совпадают",
                                   qt.QMessageBox.Ok,
                                   self)
            popup.show()
        else:
            cursor.execute("INSERT INTO User (Name,Password,Mail) VALUES (\"{}\", \"{}\", Null);".format(user, password))
            connection.commit()
            popup = qt.QMessageBox(qt.QMessageBox.Information,
                                   u"Успешно",
                                   u"Пользователь успешно создан!",
                                   qt.QMessageBox.Ok,
                                   self)
            popup.show()
            self.close()



    def quitApp (self):
        pass