

# ui_pycalculator.py defines GUI design of PyCalculator with PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(241, 421)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Calculator Window Icon
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))


        # it shows the logs of calculation
        self.label_process = QtWidgets.QLabel(self.centralwidget)
        self.label_process.setGeometry(QtCore.QRect(0, 0, 241, 59))
        self.label_process.setStyleSheet(
            "QLabel { qproperty-alignment: \'AlignVCenter | AlignRight\'; color: grey; border: 1px solid gray; background-color: rgb(255, 255, 153);\n}"
            "\n"
            "")
        self.label_process.setObjectName("label_process")

        # cancel button
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(0, 60, 61, 61))
        self.btn_cancel.setStyleSheet(
            " QPushButton { background-color: rgb(153, 0, 0); color: white; border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.btn_cancel.setObjectName("btn_cancel")
        #self.btn_equals.setStyleSheet("QPushButton { background-color: #34C0D7; color: white; border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0CADB7, stop: 1 #34C0D7); }")


        # Input window label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(62, 60, 178, 59))
        self.label.setStyleSheet("QLabel { qproperty-alignment: \'AlignVCenter | AlignRight\'; border: 1px solid gray; font: 600 16pt; background-color : white;\n}"
"\n"
"")
        self.label.setObjectName("label")


        # clear button
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(0, 120, 61, 61))
        self.btn_clear.setStyleSheet(" QPushButton { background-color: rgb(160, 160, 160); border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.btn_clear.setObjectName("btn_clear")

        # button '+/-'
        self.btn_plusMinus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plusMinus.setGeometry(QtCore.QRect(60, 120, 61, 61))
        self.btn_plusMinus.setStyleSheet(" QPushButton { background-color: rgb(215, 215, 215); border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.btn_plusMinus.setObjectName("btn_plusMinus")

        # Amend Typo (from porcent to percent)
        # button '%' (percentage)
        self.btn_percent = QtWidgets.QPushButton(self.centralwidget)
        self.btn_percent.setGeometry(QtCore.QRect(120, 120, 61, 61))
        self.btn_percent.setStyleSheet(" QPushButton { background-color: rgb(215, 215, 215); border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.btn_percent.setObjectName("btn_porcent")

        # button '/' (divide)
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divide.setGeometry(QtCore.QRect(180, 120, 61, 61))
        self.btn_divide.setStyleSheet("QPushButton { background-color: #34C0D7; color: white; border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0CADB7, stop: 1 #34C0D7); }")
        self.btn_divide.setObjectName("btn_divide")

        # button '*' (multiply)
        self.btn_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multiply.setGeometry(QtCore.QRect(180, 180, 61, 61))
        self.btn_multiply.setStyleSheet("QPushButton { background-color: #34C0D7; color: white; border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0CADB7, stop: 1 #34C0D7); }")
        self.btn_multiply.setObjectName("btn_multiply")

        # button 7
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 180, 61, 61))
        self.btn_7.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_7.setObjectName("btn_7")

        # button 9
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(120, 180, 61, 61))
        self.btn_9.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_9.setObjectName("btn_9")

        # button 8
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(60, 180, 61, 61))
        self.btn_8.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_8.setObjectName("btn_8")

        # button 2
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(60, 300, 61, 61))
        self.btn_2.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_2.setObjectName("btn_2")

        # button '-'
        self.btn_subtract = QtWidgets.QPushButton(self.centralwidget)
        self.btn_subtract.setGeometry(QtCore.QRect(180, 240, 61, 61))
        self.btn_subtract.setStyleSheet("QPushButton { background-color: #34C0D7; color: white; border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0CADB7, stop: 1 #34C0D7); }")
        self.btn_subtract.setObjectName("btn_subtract")

        # button 1
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 300, 61, 61))
        self.btn_1.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_1.setObjectName("btn_1")

        # button 3
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(120, 300, 61, 61))
        self.btn_3.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_3.setObjectName("btn_3")

        # button 4
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 240, 61, 61))
        self.btn_4.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_4.setObjectName("btn_4")

        # button 6
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(120, 240, 61, 61))
        self.btn_6.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_6.setObjectName("btn_6")

        # button '+'
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(180, 300, 61, 61))
        self.btn_add.setStyleSheet("QPushButton { background-color: #34C0D7; color: white; border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0CADB7, stop: 1 #34C0D7); }")
        self.btn_add.setObjectName("btn_add")

        # button 5
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(60, 240, 61, 61))
        self.btn_5.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_5.setObjectName("btn_5")

        # button '='
        self.btn_equals = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equals.setGeometry(QtCore.QRect(180, 360, 61, 61))
        self.btn_equals.setStyleSheet("QPushButton { background-color: #34C0D7; color: white; border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0CADB7, stop: 1 #34C0D7); }")
        self.btn_equals.setObjectName("btn_equals")

        # button 0
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 360, 121, 61))
        self.btn_0.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_0.setObjectName("btn_0")

        # button '.'
        self.btn_decimal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decimal.setGeometry(QtCore.QRect(120, 360, 61, 61))
        self.btn_decimal.setStyleSheet(" QPushButton { background-color: rgb(215, 215, 215); border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.btn_decimal.setObjectName("btn_decimal")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pycalculator"))
        self.label.setText(_translate("MainWindow", "0"))
        self.label_process.setText(_translate("MainWindow", "Calculation Log"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))
        self.btn_clear.setText(_translate("MainWindow", "Clear"))
        self.btn_plusMinus.setText(_translate("MainWindow", "+/-"))
        self.btn_percent.setText(_translate("MainWindow", "%"))
        self.btn_divide.setText(_translate("MainWindow", "÷"))
        self.btn_multiply.setText(_translate("MainWindow", "x"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_subtract.setText(_translate("MainWindow", "-"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_equals.setText(_translate("MainWindow", "="))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_decimal.setText(_translate("MainWindow", "."))
