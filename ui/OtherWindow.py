# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OtherWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.MainWindow import Ui_MainWindow

class Ui_OtherWindow(object):
    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(289, 272)
        self.lineEdit = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 113, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(OtherWindow)
        self.label.setGeometry(QtCore.QRect(10, 20, 59, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(OtherWindow)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 59, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 90, 113, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(OtherWindow)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 59, 15))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 140, 113, 23))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(OtherWindow)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 59, 15))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 190, 113, 23))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(OtherWindow)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 59, 15))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(OtherWindow)
        self.comboBox.setGeometry(QtCore.QRect(10, 240, 111, 23))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(OtherWindow)
        self.pushButton.setGeometry(QtCore.QRect(160, 120, 91, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "Form"))
        self.lineEdit.setText(_translate(Ui_MainWindow.id_return()))
        self.label.setText(_translate("OtherWindow", "TC"))
        self.label_2.setText(_translate("OtherWindow", "AD"))
        self.label_3.setText(_translate("OtherWindow", "SOYAD"))
        self.label_4.setText(_translate("OtherWindow", "ANA ADI"))
        self.label_5.setText(_translate("OtherWindow", "CİNSİYET"))
        self.comboBox.setItemText(0, _translate("OtherWindow", "Erkek"))
        self.comboBox.setItemText(1, _translate("OtherWindow", "Kadın"))
        self.pushButton.setText(_translate("OtherWindow", "Kaydet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QWidget()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())

