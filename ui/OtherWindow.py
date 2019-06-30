# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OtherWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OtherWindow(object):
    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 113, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 50, 113, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 80, 113, 23))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 110, 113, 23))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 140, 113, 23))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QWidget()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())

