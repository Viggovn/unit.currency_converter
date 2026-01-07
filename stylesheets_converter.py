convert_Btn = """
QPushButton {
    background: qlineargradient(
        x1: 0, y1: 0,
        x2: 1, y2: ,
        stop: 0 #FF512F,
        stop: 1 #F09819
    );
    color: white;
    border: 1px;
    border-radius: 8px;
    font: bold 14px "Segoe UI";
    padding: 6px;
}
QPushButton:hover {
    background-color: gray;
    border-style: outset;
    border-width: 2px;
}
"""

input_line_edit = """
QLineEdit {
    background-color: #1e1e1e;
    color: white;
    border-style: outset;
    border-width: 1px;
    border-color: #e65300;
}
"""

window = """
#MainWindow {
    background-color: black;
    border: 5px solid #e65300;
    border-radius: 10px;
}
"""

combobox_stylesheet = """
QComboBox {
    background-color: #1e1e1e;
    color: white;
    border-style: outset;
    border-width: 1px;
}
"""

title_stylesheet = """
QLabel {
    color: white;
    padding: 20px;
    qproperty-alignment: 'AlignCenter';
    background-color: #2a2a2a;
    font-size: 24px;
    font-weight: bold;
    border: 1px outset #e65300;
    min-height: 60px;
}
"""