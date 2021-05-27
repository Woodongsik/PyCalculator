# the Modules To import
from PyQt5 import QtWidgets
from ui_pycalculator import Ui_MainWindow

# Start
class CalculatorWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    firstNumber = None                         # 첫번째 입력된 숫자
    isUserTypingSecondNumber = False

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
        
        # 아래 porcent 오타를 percent로 수정함
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

        #4칙연산 버튼이 눌러졌을경우
        if ((self.btn_add.isChecked() or self.btn_subtract.isChecked() or
             self.btn_multiply.isChecked() or self.btn_divide.isChecked()) and
                not self.isUserTypingSecondNumber):

            newLabel = format(float(button.text()), ".15g")
            self.btn_decimal.setEnabled(True)

            self.isUserTypingSecondNumber = True

        #4칙연산버튼은 눌러지지 않았고, 숫자가 눌러졌을경우
        else:
            if (("." in self.label.text()) and (button.text() == "0")):
                newLabel = format(
                    self.label.text() + button.text(), ".15")
            else:
                newLabel = format(
                    float(self.label.text() + button.text()), ".15g")

        self.label.setText(newLabel)

    #소수점 '.'버튼이 눌러졌을경우
    def decimal_press(self):
        self.label.setText(self.label.text() + ".")
        self.btn_decimal.setEnabled(False)

    #버튼+/-'가 눌러졌거나, %가 눌러졌을때"
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

    #=버튼이 눌러졌을꼉우'
    def equals_pressed(self):
        secondNumber = float(self.label.text())

        if self.btn_add.isChecked():
            labelNumber = self.firstNumber + secondNumber
            newLabel = format(labelNumber, ".15g")
            self.label.setText(newLabel)
            self.btn_add.setChecked(False)

        elif self.btn_subtract.isChecked():
            labelNumber = self.firstNumber - secondNumber
            newLabel = format(labelNumber, ".15g")
            self.label.setText(newLabel)
            self.btn_subtract.setChecked(False)

        elif self.btn_multiply.isChecked():
            labelNumber = self.firstNumber * secondNumber
            newLabel = format(labelNumber, ".15g")
            self.label.setText(newLabel)
            self.btn_multiply.setChecked(False)

        elif self.btn_divide.isChecked():
            labelNumber = self.firstNumber / secondNumber
            newLabel = format(labelNumber, ".15g")
            self.label.setText(newLabel)
            self.btn_divide.setChecked(False)

        self.isUserTypingSecondNumber = False

    def clear_pressed(self):
        self.btn_add.setChecked(False)
        self.btn_subtract.setChecked(False)
        self.btn_multiply.setChecked(False)
        self.btn_divide.setChecked(False)

        self.isUserTypingSecondNumber = False

        self.label.setText("0")
