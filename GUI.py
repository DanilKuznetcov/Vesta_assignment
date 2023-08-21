#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui as qt

import Configurations
from widgets import (AuthorizingWidget, ResetPasswordWidget, RegistrationWidget,
                     EmployeesBirthdayList, PopupReminderWidget, EmployeeWidget)
from Configurations import *

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
    employeesBirthdayListWidget = EmployeesBirthdayList.Create()
    popupReminderWidget = PopupReminderWidget.Create()
    employeeWidget = EmployeeWidget.Create()

    widgets = [authorizingWidget, registrationWidget, resetPasswordWidget, employeesBirthdayListWidget,
               popupReminderWidget, employeeWidget]
    for widget in widgets:
        centrize_Widget(widget)

    employeesBirthdayListWidget.authorizingWidget = authorizingWidget
    employeesBirthdayListWidget.employeeWidget = employeeWidget
    employeesBirthdayListWidget.add.clicked.connect(employeeWidget.show)

    employeeWidget.employeesBirthdayListWidget = employeesBirthdayListWidget

    authorizingWidget.employeesBirthdayListWidget = employeesBirthdayListWidget
    authorizingWidget.popupReminderWidget = popupReminderWidget
    authorizingWidget.sign_up.clicked.connect(registrationWidget.show)
    authorizingWidget.forgot_password.mousePressEvent = resetPasswordWidget.show_myself
    authorizingWidget.sign_in.clicked.connect(authorizingWidget.authorize)

    authorizingWidget.show()
    if Configurations.username != "" and Configurations.username != "":
        authorizingWidget.authorize(from_cnfg=True)
    sys.exit(app.exec_())




if __name__ == '__main__':
    main()
