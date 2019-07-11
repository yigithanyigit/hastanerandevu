# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from database.modules import query, inserttable

class Randevu_Ui(object):

    def get_dates(self, date):
        # sqlDate = "SELECT * FROM Appointments WHERE (Tarih, Hekim_Adı) = (%s, %s)"
        sqlDate = "SELECT * FROM Appointments WHERE Tarih = %s"
        if len(str(date[1])) == 2:
            strdate = "%s-%s-0%s" % (date[0], date[1], date[2])
        elif len(str(date[2])) == 2:
            strdate = "%s-0%s-%s" % (date[0], date[1], date[2])
        else:
            strdate = "%s-0%s-0%s" % (date[0], date[1], date[2])
        result = query(strdate, sql=sqlDate, fetch=True)
        if result:
            for i in result:
                print(i)

    def on_click(self):
        table = "Appointments"
        sql = "INSERT INTO {} (Hekim_Adı, Tarih, Saat, Department, TC) VALUES (%s, %s, %s, %s, %s)".format(table)
        print(self.name, self.srname, self.id)
        self.date = self.calendarWidget.selectedDate()
        self.date = self.date.toString("yyyy-MM-dd")
        inserttable(self.comboBox_2.currentText(), self.date, self.comboBox_3.currentText(), self.comboBox.currentText(), self.id,  sql=sql)
        self.comboBoxDate()


    def comboBoxDepartments(self, translate):
        sqlDepartments = "SELECT * FROM Departments"
        result = query(sql=sqlDepartments, fetch=True)
        while result:
            c  = 0
            for i in result:

                i = i[0]
                # print(c, i)
                self.comboBox.insertItem(c, translate("Randevu", i))
                c += 1
            self.comboBoxDocs()
            self.comboBoxDate()
            break

    def comboBoxDocs(self):
        sqlDocs = "SELECT * FROM Docs"
        result = query(sql=sqlDocs, fetch=True)
        _translate = QtCore.QCoreApplication.translate
        c = self.comboBox.currentIndex()
        while result:
            a = 0
            # print(c)
            self.comboBox_2.clear()
            for i in result:
                i = i[0]
                # print(a, i, c)
                if a == c or a == c+1:
                    self.comboBox_2.insertItem(a, _translate("Randevu", i))
                a += 1
            break

    def comboBoxDate(self):
        self.comboBox_3.clear()
        self.date = self.calendarWidget.selectedDate()
        self.date = self.date.toString("yyyy-MM-dd")
        sqlDate = "SELECT * FROM Date_Time"
        result = query(sql=sqlDate, fetch=True)
        _translate = QtCore.QCoreApplication.translate
        sqlDocDates = "SELECT * FROM Appointments WHERE (Hekim_Adı, Tarih) = (%s, %s)"
        Doc_Name = self.comboBox_2.currentText()
        DocResult = query(Doc_Name, self.date ,sql=sqlDocDates, fetch=True)
        if DocResult:
            self.drawTreeView(DocResult, date=self.date)
            print(DocResult)
            a = list()
            for x in DocResult:
                x = x[2]
                x = (x,)
                a.append(x)
            for q in a:
                result.remove(q)
            for i, elem in enumerate(result):
                self.comboBox_3.insertItem(i, _translate("Randevu", elem[0]))
        else:
            self.drawTreeView(DocResult, date=self.date)
            while result:
                self.comboBox_3.clear()
                c = 0
                for i in result:
                    i = i[0]
                    self.comboBox_3.insertItem(c, _translate("Randevu", i))
                    c += 1
                break

    def drawTreeView(self, result, date):
        self.treeWidget.clear()
        self.calendarWidget.setMinimumDate(QtCore.QDate.currentDate())
        self.item = QtWidgets.QTreeWidgetItem()
        self.item = self.item.setText(1, date)
        print(self.item)
        self.treeWidget.insertTopLevelItem(0, self.item)



    def setupUi(self, Randevu, name, srname, id):
        Randevu.setObjectName("Randevu")
        Randevu.resize(565, 460)
        Randevu.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))


        # Center on Screen
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        Randevu.move((resolution.width() / 2) - (Randevu.frameSize().width() / 2),
                        (resolution.height() / 2) - (Randevu.frameSize().height() / 2))

        self.name = name
        self.srname = srname
        self.id = id
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
        self.pushButton = QtWidgets.QPushButton(Randevu)
        self.pushButton.setGeometry(QtCore.QRect(470, 430, 80, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(Randevu)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 190, 181, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.treeWidget = QtWidgets.QTreeWidget(Randevu)
        self.treeWidget.setGeometry(QtCore.QRect(30, 240, 241, 151))
        self.treeWidget.setObjectName("treeWidget")
        self.comboBox_3 = QtWidgets.QComboBox(Randevu)
        self.comboBox_3.setGeometry(QtCore.QRect(310, 240, 181, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_4 = QtWidgets.QLabel(Randevu)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Randevu)
        self.label_5.setGeometry(QtCore.QRect(310, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")


        self.retranslateUi(Randevu, self.name, self.srname)
        # self.calendarWidget.clicked['QDate'].connect(self.comboBox.update)
        self.calendarWidget.clicked['QDate'].connect(self.comboBoxDate)
        self.comboBox.currentIndexChanged.connect(self.comboBoxDocs)
        self.comboBox_2.currentIndexChanged.connect(self.comboBoxDate)
        self.pushButton.clicked.connect(self.on_click)
        QtCore.QMetaObject.connectSlotsByName(Randevu)

    def retranslateUi(self, Randevu, name, srname):
        _translate = QtCore.QCoreApplication.translate
        Randevu.setWindowTitle(_translate("Randevu", "Hastane Randevu Sistemi"))
        self.comboBoxDepartments(_translate)
        self.label.setText(_translate("Randevu", name))
        self.label_2.setText(_translate("Randevu", srname))
        self.label_3.setText(_translate("Randevu", "Bölüm Seçin"))
        # self.calendarWidget.setSelectedDate()
        self.pushButton.setText(_translate("Randevu", "Randevu Al"))
        self.treeWidget.headerItem().setText(0, _translate("Randevu", "En Erken Tarih"))
        self.label_4.setText(_translate("Randevu", "Hekim Seçin"))
        self.label_5.setText(_translate("Randevu", "Saat Seçin"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Randevu = QtWidgets.QWidget()
    ui = Randevu_Ui()
    ui.setupUi(Randevu)
    Randevu.show()
    sys.exit(app.exec_())

