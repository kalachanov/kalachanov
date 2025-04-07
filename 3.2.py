from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
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
        
        self.text_pole = QLineEdit(self)
        self.text_pole.setGeometry(0, 0, 100, 30)

        self.butsay = QPushButton(self)
        self.butsay.setText("Отправить")
        self.butsay.setGeometry(0, 30, 100, 30)
        self.butsay.clicked.connect(self.say)

        self.update()
        self.show()
    def btn(self):
        if self.button.isChecked():
            self.label.setText("Нажал")
        else:
            self.label.setText("Привет, PyQt!")
    def mousePressEvent(self, event):
        button = event.button()
        if button == 1:
            self.label.setText("Нажал ЛКМ")
        if button == 2:
            self.label.setText("Нажал ПКМ")
        if button == 4:
            self.label.setText("Нажал СКМ")
    def mouseDoubleClickEvent(self, event):
        button = event.button()
        if button == 1:
            self.label.setText("Double клик")
    def say(self):
        name = self.text_pole.text()
        message = "Привет " + name
        QMessageBox.information(window, "Приветствие", message)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())