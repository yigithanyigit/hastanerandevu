import sys
import mysql.connector
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QMessageBox, QLabel, \
    QComboBox, QApplication
from database.modules import database

##########################################
sql = "INSERT INTO {} (TC, AD, SOYAD, ANA_ADI, CİNSİYET) VALUES (%s, %s, %s, %s, %s)".format("patients")


def get(var):
    list = []
    while True:
        for x in var:
            list.append(x)
        return list


class Register(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Hastane Randevu Sistemi'
        self.left = 600
        self.top = 600
        self.width = 600
        self.height = 600
        self.mydb = database()
        self.mycursor = self.mydb.cursor()
        self.initui()

    def initui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.text = QLabel(self)
        self.text.setText("TC")
        self.text.move(20, 0)
        self.id = QLineEdit(self)
        self.id.move(20, 30)
        self.id.resize(280, 40)

        # Create textbox
        self.text = QLabel(self)
        self.text.setText("AD")
        self.text.move(20, 70)
        self.name = QLineEdit(self)
        self.name.move(20, 100)
        self.name.resize(280, 40)

        # Create textbox
        self.text = QLabel(self)
        self.text.setText("SOYAD")
        self.text.move(20, 140)
        self.srname = QLineEdit(self)
        self.srname.move(20, 170)
        self.srname.resize(280, 40)

        # Create textbox
        self.text = QLabel(self)
        self.text.setText("ANA ADI")
        self.text.move(20, 210)
        self.mamaname = QLineEdit(self)
        self.mamaname.move(20, 240)
        self.mamaname.resize(280, 40)

        # Create textbox
        self.text = QLabel(self)
        self.text.setText("CİNSİYET")
        self.text.move(20, 280)
        self.cinsiyet = QComboBox(self)
        # self.file = open("Departments.txt", "r")
        self.cinsiyet.addItems(["Erkek", "Kadın"])
        self.cinsiyet.move(20, 310)
        self.cinsiyet.resize(280, 30)

        # # Create a button in the window
        self.button = QPushButton('Kaydet', self)
        self.button.move(20, 350)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        val = (int(self.id.text()), self.name.text(), self.srname.text(), self.mamaname.text(), self.cinsiyet.currentText())
        print(self.id.text())
        if QMessageBox.question(self, 'Hastane Randevu Sistemi', "Hastayı Kaydetmek istediğinize emin misiniz?",
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            self.mydb.cursor().execute(sql, val)
            self.mydb.commit()
            print(self.mycursor.rowcount, "Kayıt Girildi")
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    print(__name__)
    ex = Register()
    sys.exit(app.exec_())
