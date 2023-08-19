# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui as qt
from widgets import (AuthorizingWidget, ResetPasswordWidget, RegistrationWidget,
                     EmployeesBirthdayList, PopupRemuinderWidget)
from functools import partial

def centrize_Widget(widget):
    qr = widget.frameGeometry()
    cp = qt.QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    widget.move(qr.topLeft())


def main():
    '''
    This is the GUI module where all of the program's elements come together in a pretty little tabbed window.
    '''
    app = qt.QApplication(sys.argv)

    authorizingWidget = AuthorizingWidget.Create()
    registrationWidget = RegistrationWidget.Create()
    resetPasswordWidget = ResetPasswordWidget.Create()
    employeesBirthdayList = EmployeesBirthdayList.Create()
    popupRemuinderWidget = PopupRemuinderWidget.Create()

    widgets = [authorizingWidget, registrationWidget, resetPasswordWidget, employeesBirthdayList, popupRemuinderWidget]

    for widget in widgets:
        centrize_Widget(widget)


    authorizingWidget.sign_up.clicked.connect(registrationWidget.show)
    authorizingWidget.forgot_password.mousePressEvent = resetPasswordWidget.show_myself
    authorizingWidget.sign_in.clicked.connect(authorizingWidget.close)
    authorizingWidget.sign_in.clicked.connect(employeesBirthdayList.show)
    authorizingWidget.sign_in.clicked.connect(popupRemuinderWidget.show)

    authorizingWidget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

def show(widget, **kwargs):
    widget.show()
