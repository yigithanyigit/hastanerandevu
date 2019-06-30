import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QLabel, QDesktopWidget, QPushButton, QWidget
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot, QCoreApplication
from database.modules import query


class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.id = QLineEdit(self)
        self.label = QLabel(self)
        self.button = QPushButton(self)
        self.title = "Hastane Randevu Sistemi"
        self.width = 200
        self.height = 600
        self.top = 480
        self.left = 600
        self.initui()

    # Initiliaze Ui
    def initui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.height, self.width)

        # Center on screen
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

        # Create "TC" Textbox
        self.id.move(140, 70)
        self.id.resize(280, 40)

        # Create "TC" Label
        newfont = QtGui.QFont("Times", 15) # Font size and font change
        self.label.setFont(newfont)
        self.label.setText("TC")
        self.label.move(100, 70)
        self.label.resize(40, 40)

        # Create Button
        self.button.move(430, 70)
        self.button.resize(70,40)
        self.button.setFont(newfont)
        self.button.setText("Gönder")
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        if query(self.id.text()):
            raise ValueError
        else:
            return True


# Debugging
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = Main()
    sys.exit(app.exec())
