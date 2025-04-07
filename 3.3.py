from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    my_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно")
        self.setGeometry(1000, 100, 300, 200)
        self.label = QLabel(self)
        self.label.setText("Привет, PyQt!")
        self.label.setGeometry(100, 50, 100, 30)
        
        self.button = QPushButton(self)
        self.button.setText("Нажми меня!")
        self.button.setCheckable(True)
        self.button.setGeometry(100, 100, 100, 30)
        self.button.toggled.connect(self.btn)

        self.checkbox = QCheckBox(self)
        self.checkbox.setText("Нажми меня!")
        self.checkbox.setGeometry(100, 130, 100, 30)

        lay = QVBoxLayout()
        lay.addWidget(self.button)
        lay.addWidget(self.checkbox)

        self.text_edit = QLineEdit(self)
        self.setCentralWidget(self.text_edit)
        self.text_changed = False
        self.text_edit.textChanged.connect(self.on_text_changed)
        self.text_edit.setGeometry(0, 0, 100, 30)

        lay2 = QHBoxLayout()
        lay2.addWidget(self.text_edit)
        
        self.update()
        self.show()

    def on_text_changed(self):
        text = self.text_edit.text()
        if text.isnumeric():
            self.label.setText("Вы ввели число")
        else:
            self.label.setText("Вы ввели текст")
    
    def btn(self):
        if self.button.isChecked():
            self.label.setText("Нажал")
            self.my_signal.emit()
        else:
            self.label.setText("Привет, PyQt!")
            self.my_signal.emit()

    def keyPressEvent(self, event):
        keys = str(event.key())
        self.label.setText(keys)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())