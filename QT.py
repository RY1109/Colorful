import os

from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog,QGraphicsScene
import sys
from colorUI import Ui_MainWindow
import cv2 as cv

class MyWindow(QMainWindow, Ui_MainWindow):
    Base_dir = os.path.curdir
    imgpath = None

    def __init__(self):
        super(MyWindow, self).__init__()
        QtGui.QFontDatabase.addApplicationFont("2.otf")
        self.setupUi(self)
        self.menubar.triggered[QAction].connect(self.processtrigger)
        self.setMouseTracking(True)


    def processtrigger(self, action: QAction):
        if action == self.actionopen:

            fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                    "choose_file", self.Base_dir
                                                                    ,  # 起始路径
                                                                    "Images (*.png *.jpg *.xpm *.bmp)")  # 设置文件扩展名过滤,用双分号间隔All Files (*)

            if fileName_choose == "":
                print("\ncancel")
                return

            print("\nThe file you choose:")
            print(fileName_choose)
            # self.centralwidget.setStyleSheet("background-image:url(%s);" % fileName_choose)
            self.src=cv.imread(fileName_choose)
            src = cv.cvtColor(self.src, cv.COLOR_BGR2RGB)
            x = self.src.shape[1]
            y = self.src.shape[0]
            frame = QtGui.QImage(src, x, y, x * 3, QtGui.QImage.Format_RGB888)
            pix = QtGui.QPixmap.fromImage(frame)
            self.scene = QGraphicsScene()
            self.scene.addPixmap(pix)
            self.graphicsView.setScene(self.scene)
            self.show_dst([0,0])

            self.imgpath = fileName_choose
            print("filetype: ", filetype)

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        pos = self.graphicsView.mapFromParent(a0.pos())
        # print(pos)
        pixmap = self.graphicsView.grab()
        img = pixmap.toImage()
        color = img.pixelColor(pos.x(), pos.y())
        # print(color.name())
        # tips = "position(%s,%s),color为：%s,%s,%s" % (pos.x(), pos.y(), color.red(),color.green(),color.blue())
        # self.centralwidget.setToolTip(tips)

    def mousePressEvent(self, a0:QtGui.QMouseEvent):  ##重载一下鼠标点击事件
        # 左键按下
        if a0.buttons() == QtCore.Qt.LeftButton:
            pos = self.graphicsView.mapFromParent(a0.pos())
            # print(pos)
            pixmap = self.graphicsView.grab()
            img = pixmap.toImage()
            color = img.pixelColor(pos.x(), pos.y())
            self.grayscale = color.red()
            print('grayscale is',str(self.grayscale))
            self.enable_scroll()
            self.RR.valueChanged.connect(lambda val: self.show_dst([ 1, val]))
            self.GG.valueChanged.connect(lambda val: self.show_dst([2, val]))
            self.BB.valueChanged.connect(lambda val: self.show_dst([3, val]))
            # self.GG.valueChanged.connect(lambda val: self.show_dst([self.grayscale, 2, val]))
            # self.BB.valueChanged.connect(lambda val: self.show_dst([self.gratscale, 3, val]))
            # image = QtGui.QPixmap.grabWidget(self).toImage()
            # color = QtGui.QColor(image.pixel(e.pos()))
            # print(color.name())
            # print("{}, {}, {}".format(color.red(), color.green(), color.blue()))
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     win = MyWindow()
#     win.show()
#     sys.exit(app.exec_())
if __name__ == "__main__":
    app = QApplication(sys.argv)#.processEvents()
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

