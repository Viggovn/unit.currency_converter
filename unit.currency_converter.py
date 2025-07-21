from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMainWindow
from PySide6.QtCore import Qt
import json
import sys

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.temp_layout = QHBoxLayout()
        self.temp_button = QPushButton()
        self.temp_button.clicked.connect(self.change_window_currency)
        self.temp_layout.addWidget(self.temp_button)
        self.setLayout(self.temp_layout)

    def change_window_currency(self, checked):
        window = currency_converter_window()
        window.show()

class currency_converter_window(QWidget):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)
window = Mainwindow()
window.show()
app.exec()

