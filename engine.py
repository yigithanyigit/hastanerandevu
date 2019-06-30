import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import Main
from RegisterWindow import Register

class Engine(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = Main()


    def registerWindow(self):
        self.register = Register()
        # self.
        self.register.show()



# Debugging
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = Engine()
    sys.exit(app.exec())
