from PySide6.QtWidgets import (QApplication, QLabel, QWidget, 
                               QVBoxLayout, QHBoxLayout, QPushButton, 
                               QStackedLayout, QLineEdit, QComboBox)
from PySide6.QtCore import Qt
import json
import sys
import stylesheets_converter
from currency_converter import SetUp, ConvertCurrency


class UnitConverterWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.MainLayout = QVBoxLayout()
        self.main_window = main_window

        #variables
        self.screen_index = 0
        self.value_1 = None
        self.value_2 = None
        self.unit_type_1 = "mm"
        self.unit_type_2 = "mm"
        self.metric_unit_list = ["mm", "cm", "dm", "m", "dam", "hm", "km"]

        #Title
        self.title_label = QLabel("Unit converter")
        self.title_label.setStyleSheet(stylesheets_converter.title_stylesheet)

        #Unit selection with combobox
        self.ComboBoxLayout = QHBoxLayout()

        self.select_unit_one = QComboBox()
        self.select_unit_one.addItems(self.metric_unit_list)
        self.select_unit_one.setStyleSheet(stylesheets_converter.combobox_stylesheet)
        self.select_unit_one.currentTextChanged.connect(lambda text: self.get_all_input_values(text, 1, "ComboBox"))

        self.select_unit_two = QComboBox()
        self.select_unit_two.addItems(self.metric_unit_list)
        self.select_unit_two.setStyleSheet(stylesheets_converter.combobox_stylesheet)
        self.select_unit_two.currentTextChanged.connect(lambda text: self.get_all_input_values(text, 2, "ComboBox"))


        self.ComboBoxLayout.addWidget(self.select_unit_one)
        self.ComboBoxLayout.addWidget(self.select_unit_two)

        #input user with line edit
        self.input_Layout = QHBoxLayout()

        self.input_1 = QLineEdit("")
        self.input_Layout.addWidget(self.input_1)
        self.input_1.setStyleSheet(stylesheets_converter.input_line_edit)
        self.input_1.textChanged.connect(lambda text: self.get_all_input_values(text, 1, "LineEdit"))

        self.input_2 = QLineEdit("")
        self.input_Layout.addWidget(self.input_2)
        self.input_2.setStyleSheet(stylesheets_converter.input_line_edit)
        self.input_2.textChanged.connect(lambda text: self.get_all_input_values(text, 2, "LineEdit"))

        #convert button
        self.Btn_Layout = QHBoxLayout()

        self.Btn_convert = QPushButton("convert")
        self.Btn_Layout.addWidget(self.Btn_convert)  
        self.Btn_convert.clicked.connect(lambda: self.calculate_unit_converted_amount(self.metric_unit_list))
        self.Btn_convert.setStyleSheet(stylesheets_converter.convert_Btn)

        #change window button
        self.change_window_btn = QPushButton("Currency converter")
        self.change_window_btn.clicked.connect(self.change_to_currency_converter)
        self.change_window_btn.setStyleSheet(stylesheets_converter.convert_Btn)

        #layouts logic
        self.MainLayout.addWidget(self.title_label)
        self.MainLayout.addStretch()
        self.MainLayout.addLayout(self.ComboBoxLayout)
        self.MainLayout.addLayout(self.input_Layout)
        self.MainLayout.addStretch()
        self.MainLayout.addLayout(self.Btn_Layout)
        self.MainLayout.addWidget(self.change_window_btn)
        self.setLayout(self.MainLayout)


    def change_to_currency_converter(self):
        #change to currency converter window with the change window button
        self.main_window.multiple_windows.setCurrentIndex(1)

    
    def get_all_input_values(self, text, current_input_field, input_type):
        #if the value in the combobox or line edit gets changed the new value will be stored in these variables that we can use later for calculations
        if input_type == "LineEdit":
            if current_input_field == 1:
                self.value_1 = text
            elif current_input_field == 2:
                self.value_2 = text

        elif input_type == "ComboBox":
            if current_input_field == 1:
                self.unit_type_1 = text
            elif current_input_field == 2:
                self.unit_type_2 = text

    
    def show_unit_LineEdit(self, value_1, value_2):
        #shows the calculated value in the other line edit box
        if value_1:
            self.input_2.setText(str(value_1))
        elif value_2:
            self.input_1.setText(str(value_2))


    def calculate_unit_converted_amount(self, metric_units):
        #tries to calculate to other unit (only support metric units currently)
        if metric_units:
            try:
                val_1 = float(self.value_1) if self.value_1 else None
                val_2 = float(self.value_2) if self.value_2 else None
                
                index_1 = self.metric_unit_list.index(self.unit_type_1)
                index_2 = self.metric_unit_list.index(self.unit_type_2)
                
                if val_1:
                    value_in_mm = val_1 * (10 ** index_1)
                    result = value_in_mm / (10 ** index_2)
                    self.show_unit_LineEdit(result, None)
                    
                elif val_2:
                    value_in_mm = val_2 * (10 ** index_2)
                    result = value_in_mm / (10 ** index_1)
                    self.show_unit_LineEdit(None, result)       
            except (ValueError, TypeError):
                pass


class CurrencyConverterWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.MainLayout = QVBoxLayout()
        self.main_window = main_window

        #variables
        self.screen_index = 0
        self.value_1 = None
        self.value_2 = None
        self.currency_type_1 = "USD"
        self.currency_type_2 = "USD"
        self.currencies = [
            "USD", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG",
            "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB",
            "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLF",
            "CLP", "CNH", "CNY", "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK",
            "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP",
            "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL",
            "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK",
            "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KID", "KMF", "KRW",
            "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD",
            "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK",
            "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR",
            "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD",
            "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE",
            "SLL", "SOS", "SRD", "SSP", "STN", "SYP", "SZL", "THB", "TJS", "TMT",
            "TND", "TOP", "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "UYU",
            "UZS", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XCG", "XDR", "XOF",
            "XPF", "YER", "ZAR", "ZMW", "ZWG", "ZWL"
        ]

        #Title
        self.title_label = QLabel("Currency converter")
        self.title_label.setStyleSheet(stylesheets_converter.title_stylesheet)

        #Unit selection with combobox
        self.ComboBoxLayout = QHBoxLayout()

        self.select_unit_one = QComboBox()
        self.select_unit_one.addItems(self.currencies)
        self.select_unit_one.setStyleSheet(stylesheets_converter.combobox_stylesheet)
        self.select_unit_one.currentTextChanged.connect(lambda text: self.get_all_input_values(text, 1, "ComboBox"))

        self.select_unit_two = QComboBox()
        self.select_unit_two.addItems(self.currencies)
        self.select_unit_two.setStyleSheet(stylesheets_converter.combobox_stylesheet)
        self.select_unit_two.currentTextChanged.connect(lambda text: self.get_all_input_values(text, 2, "ComboBox"))


        self.ComboBoxLayout.addWidget(self.select_unit_one)
        self.ComboBoxLayout.addWidget(self.select_unit_two)

        #input user with line edit
        self.input_Layout = QHBoxLayout()

        self.input_1 = QLineEdit("")
        self.input_Layout.addWidget(self.input_1)
        self.input_1.setStyleSheet(stylesheets_converter.input_line_edit)
        self.input_1.textChanged.connect(lambda text: self.get_all_input_values(text, 1, "LineEdit"))

        self.input_2 = QLineEdit("")
        self.input_Layout.addWidget(self.input_2)
        self.input_2.setStyleSheet(stylesheets_converter.input_line_edit)
        self.input_2.textChanged.connect(lambda text: self.get_all_input_values(text, 2, "LineEdit"))

        #convert button
        self.Btn_Layout = QHBoxLayout()

        self.Btn_convert = QPushButton("convert")
        self.Btn_Layout.addWidget(self.Btn_convert)  
        self.Btn_convert.clicked.connect(lambda: self.show_currency_LineEdit(self.value_1, self.value_2, 
                                                                             ConvertCurrency(self.value_1, self.value_2, 
                                                                             self.currency_type_1, self.currency_type_2)))
        self.Btn_convert.setStyleSheet(stylesheets_converter.convert_Btn)

        #change window button
        self.change_window_btn = QPushButton("Unit converter")
        self.change_window_btn.clicked.connect(self.change_to_currency_converter)
        self.change_window_btn.setStyleSheet(stylesheets_converter.convert_Btn)

        #layouts logic
        self.MainLayout.addWidget(self.title_label)
        self.MainLayout.addStretch()
        self.MainLayout.addLayout(self.ComboBoxLayout)
        self.MainLayout.addLayout(self.input_Layout)
        self.MainLayout.addStretch()
        self.MainLayout.addLayout(self.Btn_Layout)
        self.MainLayout.addWidget(self.change_window_btn)
        self.setLayout(self.MainLayout)

    
    def change_to_currency_converter(self):
        self.main_window.multiple_windows.setCurrentIndex(0)


    def get_all_input_values(self, text, current_input_field, input_type):
        #if the value in the combobox or line edit gets changed the new value will be stored in these variables that we can use later for calculations
        if input_type == "LineEdit":
            if current_input_field == 1:
                self.value_1 = text
            elif current_input_field == 2:
                self.value_2 = text

        elif input_type == "ComboBox":
            if current_input_field == 1:
                self.currency_type_1 = text
            elif current_input_field == 2:
                self.currency_type_2 = text


    def show_currency_LineEdit(self, value_1, value_2, converted_amount):
        #shows the calculated value in the other line edit box
        if value_1:
            self.input_2.setText(str(converted_amount))
        elif value_2:
            self.input_1.setText(str(converted_amount))


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setStyleSheet(stylesheets_converter.window)

        container_layout = QVBoxLayout(self)
        container_layout.setContentsMargins(5, 5, 5, 5)

        self.multiple_windows = QStackedLayout()
        container_layout.addLayout(self.multiple_windows)

        self.unit_window = UnitConverterWindow(self)
        self.currency_window = CurrencyConverterWindow(self)
        self.multiple_windows.addWidget(self.unit_window)
        self.multiple_windows.addWidget(self.currency_window)
        self.multiple_windows.setCurrentIndex(0)
        
  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 350)
    window.show()
    sys.exit(app.exec())
