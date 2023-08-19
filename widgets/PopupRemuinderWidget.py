# -*- coding: utf-8 -*-

from PyQt4 import QtGui as qt
from PyQt4 import QtCore as qt_core

class Create(qt.QWidget):
    def __init__(self, parent=None):
        super(Create, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(500, 200)
        self.setWindowTitle(u'Напоминание')

        self.birthday_label = qt.QLabel(u"Именинники этой недели:")

        self.table = qt.QTableWidget()
        self.table.horizontalHeader().setResizeMode(qt.QHeaderView.Stretch)

        # initiate table
        data = [(u"Афанасьев Иван", u"+79215731342", u"4 июня 1995")]
        self.table.setRowCount(len(data))
        self.table.setColumnCount(3)

        # set label
        self.table.setHorizontalHeaderLabels(qt_core.QString(u"Имя;Телефон;Дата рождения").split(";"))

        # set data
        for row in range(len(data)):
            for column in range(3):
                self.table.setItem(row, column, qt.QTableWidgetItem(data[row][column]))

        self.ver_layout = qt.QVBoxLayout()
        self.ver_layout.addWidget(self.birthday_label)
        self.ver_layout.addWidget(self.table, 1)
        self.setLayout(self.ver_layout)

