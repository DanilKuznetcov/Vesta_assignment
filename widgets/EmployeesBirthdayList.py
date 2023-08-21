# -*- coding: utf-8 -*-

from PyQt4 import QtGui as qt
from PyQt4 import QtCore as qt_core
from PyQt4.QtCore import Qt as qt_allignes
from Configurations import cursor, connection
import datetime

class Create(qt.QWidget):
    def __init__(self, parent=None):
        super(Create, self).__init__(parent)
        self.initUI()

    def put_objects_on_widget(self):
        # Scheme of layouts
        # ver_layout:
        #     user_layout (welcome_label   user_name)
        #     data_layout:
        #         vert_non_stretcher:
        #           buttons_layout
        #         table:
        #             ...

        self.ver_layout = qt.QVBoxLayout()

        self.user_layout = qt.QHBoxLayout()
        self.user_layout.addStretch(1)
        self.user_layout.addWidget(self.welcome_label,0, qt_allignes.AlignTop)
        self.user_layout.addWidget(self.user_name, 0, qt_allignes.AlignTop)
        self.ver_layout.addLayout(self.user_layout)

        self.data_layout = qt.QHBoxLayout()

        self.vert_non_stretcher = qt.QVBoxLayout()
        self.buttons_layout = qt.QGridLayout()
        for button, position in zip(self.alphabetic_buttons, self.alphabetic_positions):
            self.buttons_layout.addWidget(button, *position)
        self.buttons_layout.addWidget(self.getFullList, 10, 0, 1, 3)
        self.buttons_layout.addWidget(self.add, 11, 2)
        self.buttons_layout.addWidget(self.update, 12, 2)
        self.buttons_layout.addWidget(self.removeButton, 13, 2)
        self.vert_non_stretcher.addLayout(self.buttons_layout, 0)
        self.data_layout.addLayout(self.vert_non_stretcher, 0)
        self.data_layout.addWidget(self.table)

        self.ver_layout.addLayout(self.data_layout)

        self.setLayout(self.ver_layout)

    employeeWidget = object
    def create_alphabetical_and_buttons(self):
        self.alphabetic_names = [i for i in u"АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯ"]
        self.alphabetic_positions = [(i, j) for i in range(10) for j in range(3)]
        self.alphabetic_buttons = []
        for name in self.alphabetic_names:
            button = qt.QPushButton(name)
            button.setObjectName(name)
            button.clicked.connect(self.selectByLetter)
            self.alphabetic_buttons.append(button)
        # for button in self.alphabetic_buttons:

        self.getFullList = qt.QPushButton(self)
        self.getFullList.setText(u"Показать полный список")
        self.getFullList.clicked.connect(lambda: self.setDataTable(None, True))

        self.add = qt.QPushButton(self)
        self.add.setText(u"Добавить")
        self.add.setStyleSheet("border-radius : 10; padding: 5px; border : 2px solid rgb(50,205,50); background-color: rgb(127,255,0)")


        self.update = qt.QPushButton(self)
        self.update.setText(u"Изменить")
        self.update.setStyleSheet("border-radius : 10; padding: 5px; border : 2px solid grey; background-color: rgb(169,169,169)")
        self.update.clicked.connect(self.updateDBfromTable)

        self.removeButton = qt.QPushButton(self)
        self.removeButton.setText(u"Удалить")
        self.removeButton.setStyleSheet("border-radius : 10; padding: 5px; border : 2px solid red; background-color: rgb(220,20,60)")
        self.removeButton.clicked.connect(self.removeRow)
    def selectByLetter(self):
        sending_button = self.sender()
        name = unicode(sending_button.objectName()).encode('utf-8')
        cursor.execute("select * from Employees where Name Like \"{}%\";"
                       .format(name))
        response = cursor.fetchall()
        self.setDataTable(response)


    def createDataTable(self):
        self.table = qt.QTableWidget()
        self.table.horizontalHeader().setResizeMode(qt.QHeaderView.Stretch)

        # initiate table
        self.table.setRowCount(1)
        self.table.setColumnCount(3)

        # set label
        self.table.setHorizontalHeaderLabels(qt_core.QString(u"Имя;Телефон;Дата рождения").split(";"))

        self.setDataTable(None, True)

    def setDataTable(self, data, setFullList=False):
        if setFullList:
            cursor.execute("select * from Employees order by Name;")
            data = cursor.fetchall()

        self.table.setRowCount(len(data))
        for row in range(len(data)):
            self.table.setItem(row, 0, qt.QTableWidgetItem(data[row][1]))
            self.table.setItem(row, 1, qt.QTableWidgetItem(data[row][2]))
            self.table.setItem(row, 2, qt.QTableWidgetItem(data[row][3].strftime("%d/%m/%Y")))

    def updateDBfromTable(self):
        row = self.table.currentRow()
        if row == -1:
            popup = qt.QMessageBox(qt.QMessageBox.Critical,
                                   u"Ошибка",
                                   u"Необходимо выбрать данные",
                                   qt.QMessageBox.Ok,
                                   self)
            popup.show()
            return
        name = self.table.item(row, 0).text()
        phone = self.table.item(row, 1).text()
        birthdayStr = self.table.item(row, 2).text()
        birthdayDate = datetime.datetime.strptime(str(birthdayStr), '%d/%m/%Y').date()
        self.employeeWidget.nameEdit.setText(name)
        self.employeeWidget.phoneEdit.setText(phone)
        self.employeeWidget.calendar.setDate(birthdayDate)
        self.employeeWidget.isUpdate = True
        self.employeeWidget.oldData = [name, phone, birthdayStr]
        self.employeeWidget.show()

    def removeRow(self):
        row = self.table.currentRow()
        if row==-1:
            popup = qt.QMessageBox(qt.QMessageBox.Critical,
                                   u"Ошибка",
                                   u"Необходимо выбрать",
                                   qt.QMessageBox.Ok,
                                   self)
            popup.show()
            return
        name = unicode(self.table.item(row, 0).text()).encode("utf-8")
        phone = unicode(self.table.item(row, 1).text()).encode("utf-8")
        birthday = unicode(self.table.item(row, 2).text()).encode("utf-8")
        cursor.execute("delete from Employees where Name=\"{}\" and Phone=\"{}\" and Birthday=str_to_date('{}', '%d/%m/%Y');"
                       .format(name, phone, birthday))
        connection.commit()
        self.setDataTable(None, True)



    def initUI(self):
        self.resize(1000, 500)
        self.setWindowTitle(u'База дней рождений')

        self.welcome_label = qt.QLabel(u"Вы зашли как:")
        self.user_name = qt.QLabel()
        self.user_name.mousePressEvent = self.logOut
        self.user_name.setStyleSheet("color: blue; text-decoration: underline;")

        self.createDataTable()
        self.create_alphabetical_and_buttons()

        self.put_objects_on_widget()

    employeesBirthdayListWidget = object
    def logOut(self, event):
        reply = qt.QMessageBox.question(self, u"Выход",
                                           u"Сменить пользователя?", qt.QMessageBox.Yes |
                                           qt.QMessageBox.No, qt.QMessageBox.No)

        if reply == qt.QMessageBox.Yes:
            with open("Configurations.py", "r+") as f:
                lines = f.readlines()
                lines[-2] = "username = \"\"\n"
                lines[-1] = "password = \"\""
                f.seek(0)
                f.writelines(lines)
                f.truncate()
            self.close()
            self.authorizingWidget.show()
