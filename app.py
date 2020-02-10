from PyQt5 import QtCore, QtGui, QtWidgets
import images
import sys 
import util
import json 

locations = None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 431)
        MainWindow.setMaximumSize(QtCore.QSize(646, 431))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/windowIcon/Home-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(80, 20, 483, 28))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(19)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.locationLbl = QtWidgets.QLabel(self.centralwidget)
        self.locationLbl.setGeometry(QtCore.QRect(210, 90, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.locationLbl.setFont(font)
        self.locationLbl.setObjectName("locationLbl")
        self.location = QtWidgets.QComboBox(self.centralwidget)
        self.location.setGeometry(QtCore.QRect(320, 100, 151, 21))
        self.location.setObjectName("location")

        global locations

        with open("columns.json",'r') as f:
            cols = json.load(f)['data_columns']
            locations = cols[4:]

        for i in range(0,len(locations)):
            self.location.addItem("")

        self.bhlLbl = QtWidgets.QLabel(self.centralwidget)
        self.bhlLbl.setGeometry(QtCore.QRect(240, 150, 71, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bhlLbl.setFont(font)
        self.bhlLbl.setObjectName("bhlLbl")
        self.bhk = QtWidgets.QComboBox(self.centralwidget)
        self.bhk.setGeometry(QtCore.QRect(320, 160, 81, 21))
        self.bhk.setObjectName("bhk")
        self.bhk.addItem("")
        self.bhk.addItem("")
        self.bhk.addItem("")
        self.bhk.addItem("")
        self.bhk.addItem("")
        self.bhk.addItem("")
        self.bhk.addItem("")
        self.bhk.addItem("")


        self.totalSizeLbl = QtWidgets.QLabel(self.centralwidget)
        self.totalSizeLbl.setGeometry(QtCore.QRect(200, 120, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.totalSizeLbl.setFont(font)
        self.totalSizeLbl.setObjectName("totalSizeLbl")
        self.bath = QtWidgets.QComboBox(self.centralwidget)
        self.bath.setGeometry(QtCore.QRect(320, 190, 81, 21))
        self.bath.setObjectName("bath")
        self.bath.addItem("")
        self.bath.addItem("")
        self.bath.addItem("")
        self.bath.addItem("")
        self.bath.addItem("")
        self.bath.addItem("")
        self.bath.addItem("")
        self.bath.addItem("")



        self.bhlLbl_2 = QtWidgets.QLabel(self.centralwidget)
        self.bhlLbl_2.setGeometry(QtCore.QRect(170, 180, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bhlLbl_2.setFont(font)
        self.bhlLbl_2.setObjectName("bhlLbl_2")
        self.balcony = QtWidgets.QComboBox(self.centralwidget)
        self.balcony.setGeometry(QtCore.QRect(320, 220, 81, 21))
        self.balcony.setObjectName("balcony")
        self.balcony.addItem("")
        self.balcony.addItem("")
        self.balcony.addItem("")
        self.balcony.addItem("")
        self.balcony.addItem("")
        self.balcony.addItem("")
        self.balcony.addItem("")
        self.balcony.addItem("")
        self.balcony.addItem("")


        self.bhlLbl_3 = QtWidgets.QLabel(self.centralwidget)
        self.bhlLbl_3.setGeometry(QtCore.QRect(190, 210, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bhlLbl_3.setFont(font)
        self.bhlLbl_3.setObjectName("bhlLbl_3")


        self.estimateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.estimateBtn.setGeometry(QtCore.QRect(250, 280, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.estimateBtn.setFont(font)
        self.estimateBtn.setObjectName("estimateBtn")
        self.estimateBtn.clicked.connect(self.estimate)

        self.bgImage = QtWidgets.QLabel(self.centralwidget)
        self.bgImage.setGeometry(QtCore.QRect(-110, -30, 841, 571))
        self.bgImage.setText("")
        self.bgImage.setPixmap(QtGui.QPixmap(":/bgImage/cityscape-clipart-flat-art-2.png"))
        self.bgImage.setScaledContents(True)
        self.bgImage.setObjectName("bgImage")



        self.totalSize = QtWidgets.QLineEdit(self.centralwidget)
        self.totalSize.setGeometry(QtCore.QRect(320, 130, 151, 21))
        self.totalSize.setObjectName("totalSize")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(120, 360, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.predictedPrice = QtWidgets.QLabel(self.centralwidget)
        self.predictedPrice.setGeometry(QtCore.QRect(350, 360, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.predictedPrice.setFont(font)
        self.predictedPrice.setScaledContents(True)
        self.predictedPrice.setWordWrap(True)
        self.predictedPrice.setObjectName("predictedPrice")
        self.bgImage.raise_()
        self.title.raise_()
        self.locationLbl.raise_()
        self.location.raise_()
        self.bhlLbl.raise_()
        self.bhk.raise_()
        self.totalSizeLbl.raise_()
        self.bath.raise_()
        self.bhlLbl_2.raise_()
        self.balcony.raise_()
        self.bhlLbl_3.raise_()
        self.estimateBtn.raise_()
        self.totalSize.raise_()
        self.label1.raise_()
        self.predictedPrice.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bangalore House Price Estimation"))
        self.title.setText(_translate("MainWindow", "BANGALORE HOUSE PRICE ESTIMATOR"))

        
        self.locationLbl.setText(_translate("MainWindow", "SELECT LOCATION:"))        
        for i in range(0,len(locations)):
            self.location.setItemText(i, _translate("MainWindow", locations[i]))                    

        self.bhlLbl.setText(_translate("MainWindow", "SIZE (BHK):"))
        self.bhk.setItemText(0, _translate("MainWindow", "1"))
        self.bhk.setItemText(1, _translate("MainWindow", "2"))
        self.bhk.setItemText(2, _translate("MainWindow", "3"))
        self.bhk.setItemText(3, _translate("MainWindow", "4"))
        self.bhk.setItemText(4, _translate("MainWindow", "5"))
        self.bhk.setItemText(5, _translate("MainWindow", "6"))
        self.bhk.setItemText(6, _translate("MainWindow", "7"))
        self.bhk.setItemText(7, _translate("MainWindow", "8"))


        self.totalSizeLbl.setText(_translate("MainWindow", "TOTAL SIZE (in sqft):"))
        self.bath.setItemText(0, _translate("MainWindow", "1"))
        self.bath.setItemText(1, _translate("MainWindow", "2"))
        self.bath.setItemText(2, _translate("MainWindow", "3"))
        self.bath.setItemText(3, _translate("MainWindow", "4"))
        self.bath.setItemText(4, _translate("MainWindow", "5"))
        self.bath.setItemText(5, _translate("MainWindow", "6"))
        self.bath.setItemText(6, _translate("MainWindow", "7"))
        self.bath.setItemText(7, _translate("MainWindow", "8"))

        self.bhlLbl_2.setText(_translate("MainWindow", "NUMBER OF BATHROOMS:"))
        self.balcony.setItemText(0, _translate("MainWindow", "0"))
        self.balcony.setItemText(1, _translate("MainWindow", "1"))
        self.balcony.setItemText(2, _translate("MainWindow", "2"))
        self.balcony.setItemText(3, _translate("MainWindow", "3"))
        self.balcony.setItemText(4, _translate("MainWindow", "4"))
        self.balcony.setItemText(5, _translate("MainWindow", "5"))
        self.balcony.setItemText(6, _translate("MainWindow", "6"))
        self.balcony.setItemText(7, _translate("MainWindow", "7"))
        self.balcony.setItemText(8, _translate("MainWindow", "8"))


        self.bhlLbl_3.setText(_translate("MainWindow", "NUMBER OF BALCONY:"))
        self.estimateBtn.setText(_translate("MainWindow", "ESTIMATE"))
        self.label1.setText(_translate("MainWindow", "Estimated Price (Rs) in Lakhs:"))
        self.predictedPrice.setText(_translate("MainWindow", "00.00"))
    
    def estimate(self):        
        try:
            loc = self.location.currentText()
            size = int(self.totalSize.text())
            bhk = int(self.bhk.currentText())
            bath = int(self.bath.currentText())
            balcony = int(self.balcony.currentText())
            util.load_tools()        
            price = util.predict_prices(loc,size,bath,balcony,bhk)
            print("LOCATION:",loc,", BHK:",bhk,", TOTAL SIZE:",size,", BATHROOMS:",bath,", BALCONY:", balcony)
            print("Estimated Price:", price)
            self.predictedPrice.setText(str(price))
        except:
            msgError = QtWidgets.QMessageBox()
            msgError.setIcon(QtWidgets.QMessageBox.Critical)
            msgError.setWindowTitle("Error")
            msgError.setText("Oops!! Error")
            msgError.exec_() 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
