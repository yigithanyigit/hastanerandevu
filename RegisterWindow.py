import sys
from PyQt5.QtCore import pyqtSlot, QMetaObject
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QMessageBox, QLabel, \
    QComboBox, QApplication, QDesktopWidget, QWidget
from database.modules import inserttable
from database.database_connection import database


# def lister(var):
#     list = []
#     while True:
#         for x in var:
#             list.append(x)
#         return list


class Register(QWidget):

    def __init__(self):
        super().__init__()
        self.button = QPushButton('Kaydet', self)
        self.cinsiyet = QComboBox(self)
        self.text = QLabel(self)
        self.mamaname = QLineEdit(self)
        self.srname = QLineEdit(self)
        self.name = QLineEdit(self)
        self.id = QLineEdit(self)
        self.title = 'Hastane Randevu Sistemi'
        self.left = 600
        self.top = 600
        self.width = 450
        self.height = 400
        self.mydb = database()
        self.mycursor = self.mydb.cursor()

    def initui(self, RegisterWindow):
        RegisterWindow.setObjectName("MainWindow")
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.height, self.width)

        # Center on screen
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

        # Create textbox
        self.text = QLabel(self)
        self.text.setText("TC")
        self.text.move(20, 0)
        self.id.move(20, 30)
        self.id.resize(280, 40)

        # Create textbox
        self.text = QLabel(self)
        self.text.setText("AD")
        self.text.move(20, 70)
        self.name.move(20, 100)
        self.name.resize(280, 40)

        # Create textbox
        self.text = QLabel(self)
        self.text.setText("SOYAD")
        self.text.move(20, 140)
        self.srname.move(20, 170)
        self.srname.resize(280, 40)

        # Create textbox
        self.text = QLabel(self)
        self.text.setText("ANA ADI")
        self.text.move(20, 210)
        self.mamaname.move(20, 240)
        self.mamaname.resize(280, 40)

        # Create textbox
        self.text = QLabel(self)
        self.text.setText("CİNSİYET")
        self.text.move(20, 280)
        # self.file = open("Departments.txt", "r")
        self.cinsiyet.addItems(["Erkek", "Kadın"])
        self.cinsiyet.move(20, 310)
        self.cinsiyet.resize(280, 30)

        # # Create a button in the window
        self.button.move(20, 350)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        #self.show()

    @pyqtSlot()
    def on_click(self):
        if QMessageBox.question(self, 'Hastane Randevu Sistemi', "Hastayı Kaydetmek istediğinize emin misiniz?",
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            inserttable("patients", int(self.id.text()), self.name.text(), self.srname.text(), self.mamaname.text(),
                        self.cinsiyet.currentText())
            # Create Appointment window and comment out
            self.id.setText("")
            self.name.setText("")
            self.srname.setText("")
            self.mamaname.setText("")

        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Register()
    sys.exit(app.exec_())
