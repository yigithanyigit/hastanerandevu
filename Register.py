# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from database.modules import inserttable
from AppointmentWindow import Ui_Randevu

class RegisterUi(object):

    def register(self):
        inserttable("patients", int(self.lineEdit.text()), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(),
                    self.comboBox.currentText())
        self.Randevu = Ui_Randevu()
        self.window = QtWidgets.QMainWindow()
        self.Randevu.setupUi(self.window)
        self.window.show()
        # QtCore.QCoreApplication.instance().quit()

    def on_click(self):
      self.register()

    def setupUi(self, Register, id=None):
        Register.setObjectName("Register")
        Register.resize(289, 272)
        self.lineEdit = QtWidgets.QLineEdit(Register)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 113, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Register)
        self.label.setGeometry(QtCore.QRect(10, 20, 59, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Register)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 59, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Register)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 90, 113, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Register)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 59, 15))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Register)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 140, 113, 23))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Register)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 59, 15))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(Register)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 190, 113, 23))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(Register)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 59, 15))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(Register)
        self.comboBox.setGeometry(QtCore.QRect(10, 240, 111, 23))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.save = QtWidgets.QPushButton(Register)
        self.save.setGeometry(QtCore.QRect(160, 120, 91, 41))
        self.save.setObjectName("pushButton")



        self.save.clicked.connect(self.on_click)
        self.save.clicked.connect(Register.close)

        self.retranslateUi(Register, id)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register, id):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Form"))
        self.lineEdit.setText(_translate("Register", id))
        self.label.setText(_translate("Register", "TC"))
        self.label_2.setText(_translate("Register", "AD"))
        self.label_3.setText(_translate("Register", "SOYAD"))
        self.label_4.setText(_translate("Register", "ANA ADI"))
        self.label_5.setText(_translate("Register", "CİNSİYET"))
        self.comboBox.setItemText(0, _translate("Register", "Erkek"))
        self.comboBox.setItemText(1, _translate("Register", "Kadın"))
        self.save.setText(_translate("Register", "Kaydet"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QWidget()
    ui = RegisterUi()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())

