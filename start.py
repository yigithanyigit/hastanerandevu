import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QTextBrowser, QComboBox, QScrollArea
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import Qt
import mysql.connector

##########################################
sql = "INSERT INTO patients (TC, AD, SOYAD, ANA_ADI, CİNSİYET) VALUES (%s, %s, %s, %s, %s)"


def get(var):
    list = []
    while True:
        for x in var:
            list.append(x)
        return list

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Hastane Randevu Sistemi'
        self.left = 600
        self.top = 600
        self.width = 600
        self.height = 600
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="password",
            database="hospt"
)
        self.mycursor = self.mydb.cursor()
        # self.mycursor.execute("CREATE DATABASE mydatabase")
        # self.mycursor.execute("SHOW DATABASES")
        # for x in self.mycursor:
        #     print(x)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.text = QLabel(self)
        self.text.setText("TC")
        self.text.move(20,0)
        self.id = QLineEdit(self)
        self.id.move(20, 30)
        self.id.resize(280, 40)

        # Create textbox
        self.text = QLabel(self)
        self.text.setText("AD")
        self.text.move(20,70)
        self.name = QLineEdit(self)
        self.name.move(20, 100)
        self.name.resize(280, 40)

        # Create textbox
        self.text = QLabel(self)
        self.text.setText("SOYAD")
        self.text.move(20,140)
        self.srname = QLineEdit(self)
        self.srname.move(20, 170)
        self.srname.resize(280, 40)

        # Create textbox
        self.text = QLabel(self)
        self.text.setText("ANA ADI")
        self.text.move(20,210)
        self.mamaname = QLineEdit(self)
        self.mamaname.move(20, 240)
        self.mamaname.resize(280, 40)

        # Create textbox
        self.text = QLabel(self)
        self.text.setText("CİNSİYET")
        self.text.move(20,280)
        self.cinsiyet = QComboBox(self)
        # self.file = open("hastane-bölüm.txt", "r")
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
        if QMessageBox.question(self, 'Hastane Randevu Sistemi', "Hastayı Kaydetmek istediğinize emin misiniz?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            print(self.mycursor.rowcount, "Kayıt Girildi")
        else:
            pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())