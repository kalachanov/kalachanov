from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PIL import Image

app = QApplication([])
window = QWidget()
window.setGeometry(100, 100, 500, 500)
img = Image.open('C:/Users/alesk/OneDrive/Рабочий стол/Программирование/bobir.jpg')
resized_img = img.resize((500, 500))
resized_img.save('C:/Users/alesk/OneDrive/Рабочий стол/Программирование/resized_bobir.jpg')
bw_img = img.convert('L')
bw_img.save('C:/Users/alesk/OneDrive/Рабочий стол/Программирование/bw_bobir.jpg')
pixmap = QPixmap(img.filename)
label = QLabel(window)
label.setPixmap(pixmap)
label.move(0, 0)

window.show()
app.exec_()