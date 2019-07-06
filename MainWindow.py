# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Register import RegisterUi
from database.modules import query
from AppointmentWindow import Randevu_Ui


class MainWindowUi(object):

    # Open new window
    def openWindow(self):
        self.var = self.lineEdit.text()
        self.window = QtWidgets.QMainWindow()
        self.ui = RegisterUi()
        self.ui.setupUi(self.window, self.var)
        # MainWindow.hide()
        self.window.show()

    # Triggers openWindow
    def on_click(self):
        if query(self.lineEdit.text()) == True:
            self.Randevu = Randevu_Ui()
            self.window = QtWidgets.QMainWindow()
            self.Randevu.setupUi(self.window)
            self.window.show()
        else:
            self.openWindow()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 80)

        # Center on Screen
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        MainWindow.move((resolution.width() / 2) - (MainWindow.frameSize().width() / 2),
                        (resolution.height() / 2) - (MainWindow.frameSize().height() / 2))

        # Define Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Creates Button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 30, 80, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.on_click)

        # Creates Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 24, 59, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # Creates LineEdit
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 161, 23))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Retranstales ui
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hastane Randevu Sistemi"))
        self.pushButton.setText(_translate("MainWindow", "Gönder"))
        self.label.setText(_translate("MainWindow", "TC"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUi()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
