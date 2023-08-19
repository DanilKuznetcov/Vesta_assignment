from PyQt4 import QtGui, QtCore
import sys

class BASEGUICLS(QtGui.QDialog):
    def __init__(self,parent=None):
        super(BASEGUICLS, self).__init__(parent)
        self.gridLayout = QtGui.QGridLayout()
        self.title1=QtGui.QLabel('Hello')
        self.title2=QtGui.QLabel('bye')
        abutton=QtGui.QPushButton('Click me')
        self.gridLayout.addWidget(self.title1,1,5)
        self.gridLayout.addWidget(abutton,3,5)
        self.setLayout(self.gridLayout)
        abutton.clicked.connect(self.myfunc)

    def myfunc(self):
        self.gridLayout.removeWidget(self.title1)
        self.title1.deleteLater()
        self.gridLayout.addWidget(self.title2,1,5)


def main():
    app = QtGui.QApplication(sys.argv)

    ex = QtGui.QWidget()
    ex.show()
    ex2 = QtGui.QWidget()
    ex2.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()