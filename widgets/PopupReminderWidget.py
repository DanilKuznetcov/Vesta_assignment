# -*- coding: utf-8 -*-

from PyQt4 import QtGui as qt
from PyQt4 import QtCore as qt_core
from Configurations import cursor
from datetime import date, timedelta

class Create(qt.QWidget):
    def __init__(self, parent=None):
        super(Create, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(700, 200)
        self.setWindowTitle(u'Напоминание')

        self.birthday_label = qt.QLabel(u"Именинники этой недели:")

        self.table = qt.QTableWidget()
        self.table.horizontalHeader().setResizeMode(qt.QHeaderView.Stretch)

        # initiate table
        today = date.today()
        delta = timedelta(days=7)
        weekLater = today + delta

        query = ("SELECT * FROM Employees WHERE (MONTH(Birthday) BETWEEN {} AND {})"
                 "and (DAY(Birthday) BETWEEN {} AND {});".
                 format(today.month, weekLater.month, today.day, weekLater.day))
        cursor.execute(query)
        data = cursor.fetchall()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(3)

        # set label
        self.table.setHorizontalHeaderLabels(qt_core.QString(u"Имя;Телефон;Дата рождения").split(";"))

        # set data
        for row in range(len(data)):
            self.table.setItem(row, 0, qt.QTableWidgetItem(data[row][1]))
            self.table.setItem(row, 1, qt.QTableWidgetItem(data[row][2]))
            self.table.setItem(row, 2, qt.QTableWidgetItem(data[row][3].strftime("%d/%m/%Y")))

        self.ver_layout = qt.QVBoxLayout()
        self.ver_layout.addWidget(self.birthday_label)
        self.ver_layout.addWidget(self.table, 1)
        self.setLayout(self.ver_layout)

