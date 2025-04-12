from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import sqlite3

conn = sqlite3.connect('C:/Users/alesk/OneDrive/Рабочий стол/sql/test.db')
cursor = conn.cursor()

cursor.execute('drop table if exists kord')

cursor.execute('create table if not exists kord (id integer primary key autoincrement, x text not null, y text not null)')

cursor.execute("insert into kord (x, y) VALUES (?, ?)", (10, 20))
cursor.execute("insert into kord (x, y) VALUES (?, ?)", (20, 10))

cursor.execute("select x from kord")
x = cursor.fetchall()
cursor.execute("select y from kord")
y = cursor.fetchall()

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно")
        self.setGeometry(1000, 100, 300, 200)
        self.label = QLabel(self)
        self.label.setText("Привет, PyQt!")
        self.label.setGeometry(100, 50, 100, 30)
        
        self.button = QPushButton(self)
        self.button.setText("Считать файл")
        self.button.setCheckable(True)
        self.button.setGeometry(100, 100, 100, 30)
        self.button.toggled.connect(self.btn)

        self.checkbox = QCheckBox(self)
        self.checkbox.setText("Нажми меня!")
        self.checkbox.setGeometry(100, 130, 100, 30)

        self.text_edit = QLineEdit(self)
        self.text_changed = False
        self.text_edit.textChanged.connect(self.on_text_changed)
        self.text_edit.setGeometry(0, 0, 100, 30)

        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(0, 30, 100, 30)
        for kord in x:
            self.combo_box.addItem(kord[0])
        
        self.combo_boy = QComboBox(self)
        self.combo_boy.setGeometry(0, 60, 100, 30)
        for kord in y:
            self.combo_boy.addItem(kord[0])
        
        self.text_a = QPlainTextEdit()
        self.text_a.setGeometry(0, 90, 100, 30)
        

        lay = QHBoxLayout()
        lay.addWidget(self.combo_box)
        lay.addWidget(self.combo_boy)
        
        self.update()
        self.show()

    def on_text_changed(self):
        text = self.text_edit.text()
        if text.isnumeric():
            self.label.setText("Вы ввели число")
        else:
            self.label.setText("Вы ввели текст")
    
    def btn(self):
        self.text = open('C:/Users/alesk/OneDrive/Рабочий стол/Программирование/.exe.txt').read()
        self.text_a.setPlainText(self.text)
        self.label.setText("Считан")

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())