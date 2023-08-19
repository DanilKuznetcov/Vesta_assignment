# -*- coding: utf-8 -*-

from PyQt4 import QtGui as qt
from PyQt4 import QtCore as qt_core
from PyQt4.QtCore import Qt as qt_allignes

class Create(qt.QWidget):
    def __init__(self, parent=None):
        super(Create, self).__init__(parent)
        self.initUI()

    def put_objects_on_widget(self):
        # Scheme of layouts
        # ver_layout:
        #     user_layout (welcome_label   user_name)
        #     data_layout:
        #         buttons_layout
        #         table:
        #             ...

        self.ver_layout = qt.QVBoxLayout()

        self.user_layout = qt.QHBoxLayout()
        self.user_layout.addStretch(1)
        self.user_layout.addWidget(self.welcome_label,0, qt_allignes.AlignTop)
        self.user_layout.addWidget(self.user_name, 0, qt_allignes.AlignTop)
        self.ver_layout.addLayout(self.user_layout)

        self.data_layout = qt.QHBoxLayout()

        self.buttons_layout = qt.QGridLayout()
        for position, name in zip(self.alphabetic_positions, self.alphabetic_names):
            button = qt.QPushButton(name)
            self.buttons_layout.addWidget(button, *position)
        self.buttons_layout.addWidget(self.add, 10, 2)
        self.buttons_layout.addWidget(self.update, 11, 2)
        self.buttons_layout.addWidget(self.delete, 12, 2)
        self.data_layout.addLayout(self.buttons_layout, 0)

        self.data_layout.addWidget(self.table, 1)

        self.ver_layout.addLayout(self.data_layout)

        self.setLayout(self.ver_layout)

    def create_alphabetical_index(self):
        self.alphabetic_names = [i for i in u"АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯ"]

        self.alphabetic_positions = [(i, j) for i in range(10) for j in range(3)]
        #creation and placing in put_objects_on_widget

        self.add = qt.QPushButton(self)
        self.add.setText(u"Добавить")
        self.add.setStyleSheet("border-radius : 10; padding: 5px; border : 2px solid rgb(50,205,50); background-color: rgb(127,255,0)")

        self.update = qt.QPushButton(self)
        self.update.setText(u"Обновить")
        self.update.setStyleSheet("border-radius : 10; padding: 5px; border : 2px solid grey; background-color: rgb(169,169,169)")

        self.delete = qt.QPushButton(self)
        self.delete.setText(u"Удалить")
        self.delete.setStyleSheet("border-radius : 10; padding: 5px; border : 2px solid red; background-color: rgb(220,20,60)")

    def create_data_table(self, data):
        self.table = qt.QTableWidget()
        self.table.horizontalHeader().setResizeMode(qt.QHeaderView.Stretch)

        # initiate table
        self.table.setRowCount(len(data))
        self.table.setColumnCount(3)

        # set label
        self.table.setHorizontalHeaderLabels(qt_core.QString(u"Имя;Телефон;Дата рождения").split(";"))

        # set data
        for row in range(len(data)):
            for column in range(3):
                self.table.setItem(row, column, qt.QTableWidgetItem(data[row][column]))


    def initUI(self):
        self.resize(1000, 500)
        self.setWindowTitle(u'База дней рождений')

        self.welcome_label = qt.QLabel(u"Вы зашли как:")
        self.user_name = qt.QLabel(u"User")
        self.user_name.mousePressEvent = self.doSomething
        self.user_name.setStyleSheet("color: blue; text-decoration: underline;")

        self.create_alphabetical_index()
        example = [(u"Афанасьев Иван", u"+79215731342", u"4 июня 1995")]
        self.create_data_table(example)

        self.put_objects_on_widget()

    def doSomething(self, event):
        print 'Label click'

    def quitApp (self):
        pass
        # db.name().close()
        # sys.exit(0)
