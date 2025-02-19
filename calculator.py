# the Modules To import
from PyQt5 import QtWidgets
from ui_pycalculator import Ui_MainWindow

# calculator.py contains all functions of what to do when a button is clicked on PyCalculator

class CalculatorWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    firstNumber = None
    secondNumber = None
    labelNumber = None
    totalNumber = '0'

    isUserTypingSecondNumber = False
    isTheFirstTime = True
    calculation_record = ""


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect Buttons

        self.btn_0.clicked.connect(self.digit_press)
        self.btn_1.clicked.connect(self.digit_press)
        self.btn_2.clicked.connect(self.digit_press)
        self.btn_3.clicked.connect(self.digit_press)
        self.btn_4.clicked.connect(self.digit_press)
        self.btn_5.clicked.connect(self.digit_press)
        self.btn_6.clicked.connect(self.digit_press)
        self.btn_7.clicked.connect(self.digit_press)
        self.btn_8.clicked.connect(self.digit_press)
        self.btn_9.clicked.connect(self.digit_press)

        self.btn_decimal.clicked.connect(self.decimal_press)

        self.btn_plusMinus.clicked.connect(self.unary_operation_pressed)

        self.btn_cancel.clicked.connect(self.cancel_pressed)

        # amend a typo (from porcent to percent)
        self.btn_percent.clicked.connect(self.unary_operation_pressed)

        self.btn_add.clicked.connect(self.binary_operation_pressed)
        self.btn_subtract.clicked.connect(self.binary_operation_pressed)
        self.btn_multiply.clicked.connect(self.binary_operation_pressed)
        self.btn_divide.clicked.connect(self.binary_operation_pressed)

        self.btn_equals.clicked.connect(self.equals_pressed)

        self.btn_clear.clicked.connect(self.clear_pressed)

        self.btn_add.setCheckable(True)
        self.btn_subtract.setCheckable(True)
        self.btn_multiply.setCheckable(True)
        self.btn_divide.setCheckable(True)

    def digit_press(self):
        button = self.sender()

        if ((self.btn_add.isChecked() or self.btn_subtract.isChecked() or
             self.btn_multiply.isChecked() or self.btn_divide.isChecked()) and
                not self.isUserTypingSecondNumber):

            newLabel = format(float(button.text()), ".15g")
            self.btn_decimal.setEnabled(True)
            self.isUserTypingSecondNumber = True

        else:
            if (("." in self.label.text()) and (button.text() == "0")):
                newLabel = format(
                    self.label.text() + button.text(), ".15")
            else:
                newLabel = format(
                    float(self.label.text() + button.text()), ".15g")

        self.label.setText(newLabel)

    def decimal_press(self):
        self.label.setText(self.label.text() + ".")
        self.btn_decimal.setEnabled(False)

    def unary_operation_pressed(self):
        button = self.sender()
        labelNumber = float(self.label.text())

        if button.text() == "+/-":
            labelNumber *= -1
        else:
            labelNumber *= 0.01

        newLabel = format(labelNumber, ".15g")
        self.label.setText(newLabel)

    def binary_operation_pressed(self):
        button = self.sender()
        self.firstNumber = float(self.label.text())
        button.setChecked(True)

    def cancel_pressed(self):
        if self.totalNumber != '0':
            tmp_newLabel = format(self.totalNumber, ".7g")
            self.label.setText(tmp_newLabel)
        else:
            self.label.setText('0')
        self.isUserTypingSecondNumber = False

    def equals_pressed(self):
        self.secondNumber = float(self.label.text())

        if self.btn_add.isChecked():
            labelNumber = self.firstNumber + self.secondNumber
            self.totalNumber = labelNumber
            self.set_calculation_record('+')
            newLabel = format(labelNumber, ".15g")
            self.label.setText(newLabel)
            self.btn_add.setChecked(False)

        elif self.btn_subtract.isChecked():
            labelNumber = self.firstNumber - self.secondNumber
            self.totalNumber = labelNumber
            self.set_calculation_record('-')
            newLabel = format(labelNumber, ".15g")
            self.label.setText(newLabel)
            self.btn_subtract.setChecked(False)

        elif self.btn_multiply.isChecked():
            labelNumber = self.firstNumber * self.secondNumber
            self.totalNumber = labelNumber
            self.set_calculation_record('x')
            newLabel = format(labelNumber, ".15g")
            self.label.setText(newLabel)
            self.btn_multiply.setChecked(False)

        elif self.btn_divide.isChecked():
            labelNumber = self.firstNumber / self.secondNumber
            self.totalNumber = labelNumber
            self.set_calculation_record('/')
            newLabel = format(labelNumber, ".5g")
            self.label.setText(newLabel)
            self.btn_divide.setChecked(False)

        self.isUserTypingSecondNumber = False

    def clear_pressed(self):
        self.btn_add.setChecked(False)
        self.btn_subtract.setChecked(False)
        self.btn_multiply.setChecked(False)
        self.btn_divide.setChecked(False)
        self.isUserTypingSecondNumber = False
        self.calculation_record = ""
        self.label_process.setText("Calculation Log")
        self.label.setText("0")
        self.isTheFirstTime = True
        self.totalNumber = '0'

    def set_calculation_record(self, operator):
        if (self.isTheFirstTime):
            self.calculation_record = str(self.firstNumber)
            self.calculation_record = self.calculation_record + " " + operator + " " + str(self.secondNumber)
            self.isTheFirstTime = False
        else:
            self.calculation_record = self.calculation_record + " " + operator + " " + str(self.secondNumber)

        self.label_process.setText(self.calculation_record)