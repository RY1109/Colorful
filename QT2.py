from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap


def getPos(self , event):
    x = event.pos().x()
    y = event.pos().y()

image = QLabel()
image.setPixmap(QPixmap('ca_.jpg'))
image.setObjectName("image")
image.mousePressEvent = getPos

