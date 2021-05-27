# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(241, 421)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 과정표시해주는 윈도우창 설정
        self.label_process = QtWidgets.QLabel(self.centralwidget)
        self.label_process.setGeometry(QtCore.QRect(0, 0, 241, 59))
        self.label_process.setStyleSheet(
            "QLabel { qproperty-alignment: \'AlignVCenter | AlignRight\'; border: 1px solid gray; background-color: rgb(153, 204, 255);\n}"
            "\n"
            "")
        self.label_process.setObjectName("label_process")

        # 취소버튼
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(0, 60, 61, 61))
        self.btn_cancel.setStyleSheet(
            " QPushButton { background-color: rgb(153, 0, 0); color: white; border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.btn_cancel.setObjectName("btn_cancel")
        #self.btn_equals.setStyleSheet("QPushButton { background-color: #34C0D7; color: white; border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0CADB7, stop: 1 #34C0D7); }")


        # 입력한결과창
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(62, 60, 178, 59))
        self.label.setStyleSheet("QLabel { qproperty-alignment: \'AlignVCenter | AlignRight\'; border: 1px solid gray; font: 600 16pt; background-color : white;\n}"
"\n"
"")
        self.label.setObjectName("label")


        # 클리어버튼
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(0, 120, 61, 61))
        self.btn_clear.setStyleSheet(" QPushButton { background-color: rgb(215, 215, 215); border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.btn_clear.setObjectName("btn_clear")


        self.btn_plusMinus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plusMinus.setGeometry(QtCore.QRect(60, 120, 61, 61))
        self.btn_plusMinus.setStyleSheet(" QPushButton { background-color: rgb(215, 215, 215); border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.btn_plusMinus.setObjectName("btn_plusMinus")

        # 아래 porcent오타를 percent로 수정함
        self.btn_percent = QtWidgets.QPushButton(self.centralwidget)
        self.btn_percent.setGeometry(QtCore.QRect(120, 120, 61, 61))
        self.btn_percent.setStyleSheet(" QPushButton { background-color: rgb(215, 215, 215); border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7); }")
        self.btn_percent.setObjectName("btn_porcent")
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divide.setGeometry(QtCore.QRect(180, 120, 61, 61))
        self.btn_divide.setStyleSheet("QPushButton { background-color: #34C0D7; color: white; border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0CADB7, stop: 1 #34C0D7); }")
        self.btn_divide.setObjectName("btn_divide")
        self.btn_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multiply.setGeometry(QtCore.QRect(180, 180, 61, 61))
        self.btn_multiply.setStyleSheet("QPushButton { background-color: #34C0D7; color: white; border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0CADB7, stop: 1 #34C0D7); }")
        self.btn_multiply.setObjectName("btn_multiply")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 180, 61, 61))
        self.btn_7.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_7.setObjectName("btn_7")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(120, 180, 61, 61))
        self.btn_9.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_9.setObjectName("btn_9")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(60, 180, 61, 61))
        self.btn_8.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_8.setObjectName("btn_8")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(60, 300, 61, 61))
        self.btn_2.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_2.setObjectName("btn_2")
        self.btn_subtract = QtWidgets.QPushButton(self.centralwidget)
        self.btn_subtract.setGeometry(QtCore.QRect(180, 240, 61, 61))
        self.btn_subtract.setStyleSheet("QPushButton { background-color: #34C0D7; color: white; border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0CADB7, stop: 1 #34C0D7); }")
        self.btn_subtract.setObjectName("btn_subtract")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 300, 61, 61))
        self.btn_1.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_1.setObjectName("btn_1")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(120, 300, 61, 61))
        self.btn_3.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 240, 61, 61))
        self.btn_4.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_4.setObjectName("btn_4")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(120, 240, 61, 61))
        self.btn_6.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_6.setObjectName("btn_6")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(180, 300, 61, 61))
        self.btn_add.setStyleSheet("QPushButton { background-color: #34C0D7; color: white; border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0CADB7, stop: 1 #34C0D7); }")
        self.btn_add.setObjectName("btn_add")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(60, 240, 61, 61))
        self.btn_5.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_5.setObjectName("btn_5")
        self.btn_equals = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equals.setGeometry(QtCore.QRect(180, 360, 61, 61))
        self.btn_equals.setStyleSheet("QPushButton { background-color: #34C0D7; color: white; border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0CADB7, stop: 1 #34C0D7); }")
        self.btn_equals.setObjectName("btn_equals")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 360, 121, 61))
        self.btn_0.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); }")
        self.btn_0.setObjectName("btn_0")
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
        self.label_process.setText(_translate("MainWindow", "Process"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))
        self.btn_clear.setText(_translate("MainWindow", "C"))
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


