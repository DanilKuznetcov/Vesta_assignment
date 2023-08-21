# -*- coding: utf-8 -*-

from PyQt4 import QtGui as qt
from Configurations import cursor, connection
import datetime

class Create(qt.QWidget):
    def __init__(self, parent=None):
        super(Create, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(400, 150)
        self.setWindowTitle(u'Добавление сотрудника')

        self.nameEdit = qt.QLineEdit()
        self.nameEdit.setPlaceholderText(u"Имя сотрудника")
        self.phoneEdit = qt.QLineEdit()
        self.phoneEdit.setPlaceholderText(u"Телефон")
        self.birthdayLabel = qt.QLabel(u"Дата рождения:")
        self.calendar = qt.QDateEdit()
        self.calendar.setDisplayFormat("dd/MM/yyyy")
        self.calendar.setCalendarPopup(True)

        self.confirm = qt.QPushButton(self)
        self.confirm.setText(u"Сохранить")
        self.confirm.setStyleSheet("border-radius : 10; padding: 5px; border : 2px solid rgb(50,205,50); background-color: rgb(127,255,0)")
        self.confirm.clicked.connect(self.add)

        self.cancel = qt.QPushButton(self)
        self.cancel.setText(u"Отмена")
        self.cancel.setStyleSheet("border-radius : 10; padding: 5px; border : 2px solid red; background-color: rgb(220,20,60)")
        self.cancel.clicked.connect(self.clearEdits)
        self.cancel.clicked.connect(self.close)

        self.ver_Layout = qt.QVBoxLayout()

        self.ver_Layout.addWidget(self.nameEdit)
        self.ver_Layout.addWidget(self.phoneEdit)

        self.birthday_Layout = qt.QHBoxLayout()
        self.birthday_Layout.addWidget(self.birthdayLabel)
        self.birthday_Layout.addWidget(self.calendar)
        self.ver_Layout.addLayout(self.birthday_Layout)


        self.buttons_Layout = qt.QHBoxLayout()
        self.buttons_Layout.addWidget(self.confirm)
        self.buttons_Layout.addWidget(self.cancel)
        self.ver_Layout.addLayout(self.buttons_Layout)

        self.setLayout(self.ver_Layout)

    employeesBirthdayListWidget = object
    def clearEdits(self):
        self.nameEdit.setText("")
        self.phoneEdit.setText("")
        self.calendar.setDate(datetime.datetime.strptime('01/01/2000', '%d/%m/%Y').date())
        self.isUpdate=False

    isUpdate = False
    oldData = []
    def add(self):
        # self.employeesBirthdayListWidget.removeRow()
        user = unicode(self.nameEdit.text()).encode('utf-8')
        phone = unicode(self.phoneEdit.text()).encode('utf-8')
        birthday = unicode(self.calendar.text()).encode('utf-8')
        cursor.execute("select count(*) from Employees where Name=\"{}\" and Phone=\"{}\" and Birthday=str_to_date('{}', '%d/%m/%Y');"
                       .format(user, phone, birthday))
        response = cursor.fetchall()

        if response[0][0] != 0:
            popup = qt.QMessageBox(qt.QMessageBox.Critical,
                                   u"Ошибка данных",
                                   u"Такой работник уже есть в базе",
                                   qt.QMessageBox.Ok,
                                   self)
            popup.show()
        else:
            if self.isUpdate:
                cursor.execute("Update Employees "
                               "set Name=\"{}\", Phone=\"{}\", Birthday=str_to_date('{}', '%d/%m/%Y')"
                               "where Name=\"{}\" and Phone=\"{}\" and Birthday=str_to_date('{}', '%d/%m/%Y');"
                               .format(user, phone, birthday,
                                       unicode(self.oldData[0]).encode('utf-8'),
                                       unicode(self.oldData[1]).encode('utf-8'),
                                       unicode(self.oldData[2]).encode('utf-8')))
                self.isUpdate=False
            else:
                cursor.execute("INSERT INTO Employees (Name,Phone,Birthday) VALUES (\"{}\", \"{}\", str_to_date('{}', '%d/%m/%Y'));"
                           .format(user, phone, birthday))
            connection.commit()
            self.employeesBirthdayListWidget.setDataTable(None, True)
            self.clearEdits()
            self.close()