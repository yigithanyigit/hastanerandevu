# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AppointmentWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Randevu(object):
    def setupUi(self, Randevu):
        Randevu.setObjectName("Randevu")
        Randevu.resize(565, 460)
        Randevu.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        self.label = QtWidgets.QLabel(Randevu)
        self.label.setGeometry(QtCore.QRect(40, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Randevu)
        self.label_2.setGeometry(QtCore.QRect(150, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Randevu)
        self.comboBox.setGeometry(QtCore.QRect(30, 130, 181, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(Randevu)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(Randevu)
        self.calendarWidget.setGeometry(QtCore.QRect(260, 80, 271, 121))
        self.calendarWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        self.calendarWidget.setObjectName("calendarWidget")
        self.tableWidget = QtWidgets.QTableWidget(Randevu)
        self.tableWidget.setGeometry(QtCore.QRect(0, 230, 561, 191))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.pushButton = QtWidgets.QPushButton(Randevu)
        self.pushButton.setGeometry(QtCore.QRect(470, 430, 80, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Randevu)
        QtCore.QMetaObject.connectSlotsByName(Randevu)

    def retranslateUi(self, Randevu):
        _translate = QtCore.QCoreApplication.translate
        Randevu.setWindowTitle(_translate("Randevu", "Form"))
        self.label.setText(_translate("Randevu", "TextLabel"))
        self.label_2.setText(_translate("Randevu", "TextLabel"))
        self.label_3.setText(_translate("Randevu", "Bölüm Seçin"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Randevu", "Hekim"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Randevu", "En Erken Tarih"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Randevu", "Kurum Adı"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Randevu", "Klinik Adı"))
        self.pushButton.setText(_translate("Randevu", "Randevu Al"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Randevu = QtWidgets.QWidget()
    ui = Ui_Randevu()
    ui.setupUi(Randevu)
    Randevu.show()
    sys.exit(app.exec_())

