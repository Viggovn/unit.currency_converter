from PySide6.QtWidgets import (QApplication, QLabel, QWidget, 
                               QVBoxLayout, QHBoxLayout, QPushButton, 
                               QStackedLayout, QLineEdit, QComboBox)
from PySide6.QtCore import Qt
import json
import sys

class UnitConverterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.MainLayout = QVBoxLayout()


        self.ComboBoxLayout = QHBoxLayout()

        self.select_unit_one = QComboBox()
        self.select_unit_one.addItems(["mm", "cm", "dm", "m", "dam", "hm", "km"])
        self.select_unit_two = QComboBox()
        self.select_unit_two.addItems(["mm", "cm", "dm", "m", "dam", "hm", "km"])
        self.ComboBoxLayout.addWidget(self.select_unit_one)
        self.ComboBoxLayout.addWidget(self.select_unit_two)


        self.input_Layout = QHBoxLayout()

        self.input = QLineEdit("")
        self.input_Layout.addWidget(self.input)
        self.input_2 = QLineEdit("")
        self.input_Layout.addWidget(self.input_2)

        
        self.Btn_Layout = QHBoxLayout()

        self.Btn_convert = QPushButton()
        self.Btn_convert.clicked.connect(self.temp_feature)   
        self.Btn_Layout.addWidget(self.Btn_convert)  


        self.MainLayout.addLayout(self.ComboBoxLayout)
        self.MainLayout.addLayout(self.input_Layout)
        self.MainLayout.addLayout(self.Btn_Layout)
        self.setLayout(self.MainLayout)

    def temp_feature(self):
        if self.input.text():
            print(self.input.text().strip())
        elif self.input_2.text():
            print(self.input.text().strip())
        else:
            print("no text")

class CurrencyConverterWindow(QWidget):
    def __init__(self):
        super().__init__()

class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.multiple_windows = QStackedLayout(self)
        self.unit_window = UnitConverterWindow()
        self.currency_window = CurrencyConverterWindow()
        self.multiple_windows.addWidget(self.unit_window)
        self.multiple_windows.addWidget(self.currency_window)
        self.multiple_windows.setCurrentIndex(0)

        

app = QApplication(sys.argv)
window = Mainwindow()
window.resize(800, 600)
window.show()
sys.exit(app.exec())

