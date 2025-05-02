from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import sqlite3

conn = sqlite3.connect('C:/Users/alesk/OneDrive/Рабочий стол/sql/test.db')
cursor = conn.cursor()

cursor.execute('create table if not exists doctor (id integer primary key autoincrement, name text not null, surname text not null)')
cursor.execute('create table if not exists human (id integer primary key autoincrement, name text not null, surname text not null, god int not null)')
cursor.execute('create table if not exists zapis (id integer primary key autoincrement, data_priema text not null, doctor_id int, human_id int, FOREIGN KEY(doctor_id) REFERENCES doctor(id), FOREIGN KEY(human_id) REFERENCES human(id))')

conn.commit()

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно")
        self.setGeometry(400, 100, 900, 300)

        self.label = QLabel(self)
        self.label.setText("id, data_priema, d.id, h.id, h.name, h.suranme, h.god, d.name d.surname")
        self.label.setGeometry(10, 0, 400, 30)

        self.list = QListWidget(self)
        self.listh = QListWidget(self)
        self.listd = QListWidget(self)
        self.list.setGeometry(0, 30, 300, 120)
        self.listh.setGeometry(300, 30, 300, 120)
        self.listd.setGeometry(600, 30, 300, 120)
        self.f5()

        self.button_intput = QPushButton(self)
        self.button_intput.setText("Ввести")
        self.button_intput.setGeometry(0, 150, 100, 30)
        self.button_intput.clicked.connect(self.btninputdata)

        self.button_update = QPushButton(self)
        self.button_update.setText("Изменить")
        self.button_update.setGeometry(100, 150, 100, 30)
        self.button_update.clicked.connect(self.btnupdatedata)

        self.button_delete = QPushButton(self)
        self.button_delete.setText("Удалить")
        self.button_delete.setGeometry(200, 150, 100, 30)
        self.button_delete.clicked.connect(self.btndeletedata)

        self.button_intput_doctor = QPushButton(self)
        self.button_intput_doctor.setText("Ввести врача")
        self.button_intput_doctor.setGeometry(600, 150, 100, 30)
        self.button_intput_doctor.clicked.connect(self.btninputdatadoctor)

        self.button_update_doctor = QPushButton(self)
        self.button_update_doctor.setText("Изменить врача")
        self.button_update_doctor.setGeometry(700, 150, 100, 30)
        self.button_update_doctor.clicked.connect(self.btnupdatedatadoctor)

        self.button_delete_doctor = QPushButton(self)
        self.button_delete_doctor.setText("Удалить врача")
        self.button_delete_doctor.setGeometry(800, 150, 100, 30)
        self.button_delete_doctor.clicked.connect(self.btndeletedatadoctor)

        self.button_intput_human = QPushButton(self)
        self.button_intput_human.setText("Ввести пациента")
        self.button_intput_human.setGeometry(300, 150, 100, 30)
        self.button_intput_human.clicked.connect(self.btninputdatahuman)

        self.button_update_human = QPushButton(self)
        self.button_update_human.setText("Изменить пациента")
        self.button_update_human.setGeometry(400, 150, 100, 30)
        self.button_update_human.clicked.connect(self.btnupdatedatahuman)

        self.button_delete_human = QPushButton(self)
        self.button_delete_human.setText("Удалить пациента")
        self.button_delete_human.setGeometry(500, 150, 100, 30)
        self.button_delete_human.clicked.connect(self.btndeletedatahuman)

        lay = QHBoxLayout()
        lay.addWidget(self.list)

        lay.addWidget(self.button_intput)
        lay.addWidget(self.button_update)
        lay.addWidget(self.button_delete)

        lay.addWidget(self.button_intput_doctor)
        lay.addWidget(self.button_update_doctor)
        lay.addWidget(self.button_delete_doctor)

        lay.addWidget(self.button_intput_human)
        lay.addWidget(self.button_update_human)
        lay.addWidget(self.button_delete_human)
        
        self.update()
        self.show()

    def f5(self):
        cursor.execute('select * from zapis inner join human on zapis.human_id = human.id inner join doctor on zapis.doctor_id = doctor.id')
        self.list.clear()
        zapis = cursor.fetchall()
        for z in zapis:
            self.list.addItem(f"{z[0]}, {z[1]}, {z[2]}, {z[3]}, {z[5]}, {z[6]}, {z[7]}, {z[9]}, {z[10]}")
        conn.commit()
        
        cursor.execute('select * from human')
        self.listh.clear()
        human = cursor.fetchall()
        for h in human:
            self.listh.addItem(f"{h[0]}, {h[1]}, {h[2]}, {h[3]}")
        conn.commit()

        cursor.execute('select * from doctor')
        self.listd.clear()
        doctor = cursor.fetchall()
        for d in doctor:
            self.listd.addItem(f"{d[0]}, {d[1]}, {d[2]}")
        conn.commit()

    def btninputdata(self):
        name = QInputDialog.getText(self, 'Input','Input data priema')
        did = QInputDialog.getInt(self, 'Input','Input doctor id')
        hid = QInputDialog.getInt(self, 'Input','Input human id')
        cursor.execute("insert into zapis (data_priema, doctor_id, human_id) VALUES (?, ?, ?)", (name[0], did[0], hid[0]))
        conn.commit()
        self.f5()

    def btnupdatedata(self):
        id = QInputDialog.getInt(self, 'Input','Input id')
        did = QInputDialog.getInt(self, 'Input','Input doctor id')
        hid = QInputDialog.getInt(self, 'Input','Input human id')
        cursor.execute("update zapis set doctor_id = (?), human_id = (?) WHERE id=(?)", (did[0], hid[0], id[0]))
        conn.commit()
        self.f5()
    
    def btndeletedata(self):
        id = QInputDialog.getInt(self, 'Input','Input id')
        cursor.execute("DELETE FROM zapis WHERE id = (?)", (id[0]))
        conn.commit()
        self.f5()

    def btninputdatadoctor(self):
        name = QInputDialog.getText(self, 'Input','Input name')
        surname = QInputDialog.getText(self, 'Input','Input surname')
        cursor.execute("insert into doctor (name, surname) VALUES (?, ?)", (name[0], surname[0]))
        conn.commit()
        self.f5()

    def btnupdatedatadoctor(self):
        id = QInputDialog.getInt(self, 'Input','Input human id')
        name = QInputDialog.getText(self, 'Input','Input name')
        surname = QInputDialog.getText(self, 'Input','Input surname')
        cursor.execute("update doctor set name = (?), surname = (?), WHERE id=(?)", (name[0], surname[0], id[0]))
        conn.commit()
        self.f5()
    
    def btndeletedatadoctor(self):
        id = QInputDialog.getInt(self, 'Input','Input id')
        cursor.execute("DELETE FROM doctor WHERE id = (?)", (id[0]))
        conn.commit()
        self.f5()

    def btninputdatahuman(self):
        name = QInputDialog.getText(self, 'Input','Input name')
        surname = QInputDialog.getText(self, 'Input','Input surname')
        god = QInputDialog.getText(self, 'Input','Input god')
        cursor.execute("insert into human (name, surname, god) VALUES (?, ?, ?)", (name[0], surname[0], god[0]))
        conn.commit()
        self.f5()

    def btnupdatedatahuman(self):
        id = QInputDialog.getInt(self, 'Input','Input human id')
        name = QInputDialog.getText(self, 'Input','Input name')
        surname = QInputDialog.getText(self, 'Input','Input surname')
        god = QInputDialog.getText(self, 'Input','Input god')
        cursor.execute("update human set name = (?), surname = (?), god = (?) WHERE id=(?)", (name[0], surname[0], god[0], id[0]))
        conn.commit()
        self.f5()
    
    def btndeletedatahuman(self):
        id = QInputDialog.getInt(self, 'Input','Input id')
        cursor.execute("DELETE FROM human WHERE id = (?)", (id[0]))
        conn.commit()
        self.f5()

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
conn.close()