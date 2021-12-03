# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colorUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from scipy.interpolate import interp1d
import cv2 as cv
import numpy as np

class Ui_MainWindow(object):
    def __init__(self):
        self.grayscale = 2
        self.r = np.array(range(16)).reshape(1, 16) * 16
        self.g = -np.array(range(16)).reshape(1, 16) * 16 + 240
        self.b = np.array(range(16)).reshape(1, 16) * 16
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # self.centralwidget.setMinimumSize(QtCore.QSize(1280, 720))
        # self.centralwidget.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget.setMouseTracking(True)
        # self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));")
        # self.centralwidget = QtWidgets.QWidget(MainWindow)
        # self.centralwidget.setObjectName("centralwidget")


        # self.src = cv.imread('zy3.bmp')
        self.src = np.zeros([273,484,3]).astype('uint8')
        src = cv.cvtColor(self.src, cv.COLOR_BGR2RGB)
        x = self.src.shape[1]
        y = self.src.shape[0]
        frame = QtGui.QImage(src, x, y,x*3, QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(frame)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(15, 40, 520, 290))
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(pix)
        self.graphicsView.setScene(self.scene)

        colormap = self.gen_map([0,0])

        h = cv.LUT(self.src, colormap[:])
        h = cv.cvtColor(h, cv.COLOR_BGR2RGB)
        x2 = h.shape[1]
        y2 = h.shape[0]
        frame2 = QtGui.QImage(h, x2,y2, 3*x2 ,QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(frame2)
        self.graphicsView2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView2.setGeometry(QtCore.QRect(550, 40, 520, 290))
        self.graphicsView2.setObjectName("graphicsView")
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(pix)
        self.graphicsView2.setScene(self.scene)


        src3=np.repeat(colormap,repeats=50,axis=0)
        # src3=np.repeat(src3,int(np.ones([1,256])*2),axis=1)
        x = src3.shape[1]
        y = src3.shape[0]
        frame = QtGui.QImage(src3, x, y,x*3, QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(frame)
        self.graphicsView3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView3.setGeometry(QtCore.QRect(551, 350, 520, 71))
        self.graphicsView3.setObjectName("graphicsView")
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(pix)
        self.graphicsView3.setScene(self.scene)


        # self.color = QtWidgets.QLabel(self.centralwidget)
        # self.color.setGeometry(QtCore.QRect(551, 350, 490, 81))
        # self.color.setPixmap(QtGui.QPixmap('zy3.bmp'))
        # self.color.setObjectName("color")



        self.RR = QtWidgets.QScrollBar(self.centralwidget)
        self.RR.setGeometry(QtCore.QRect(70, 350, 465, 71))
        self.RR.setOrientation(QtCore.Qt.Horizontal)
        self.RR.setObjectName("RR")
        self.RR.setDisabled(1)


        self.R = QtWidgets.QLabel(self.centralwidget)
        self.R.setGeometry(QtCore.QRect(20, 340, 31, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(26)
        self.R.setFont(font)
        self.R.setObjectName("R")


        self.GG = QtWidgets.QScrollBar(self.centralwidget)
        self.GG.setGeometry(QtCore.QRect(70, 450, 465, 71))
        self.GG.setOrientation(QtCore.Qt.Horizontal)
        self.GG.setObjectName("GG")
        self.GG.setDisabled(1)

        self.G = QtWidgets.QLabel(self.centralwidget)
        self.G.setGeometry(QtCore.QRect(20, 440, 31, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(26)
        self.G.setFont(font)
        self.G.setObjectName("G")


        self.BB = QtWidgets.QScrollBar(self.centralwidget)
        self.BB.setGeometry(QtCore.QRect(590, 450, 465, 71))
        self.BB.setOrientation(QtCore.Qt.Horizontal)
        self.BB.setObjectName("BB")
        self.BB.setDisabled(1)

        self.B = QtWidgets.QLabel(self.centralwidget)
        self.B.setGeometry(QtCore.QRect(550, 440, 31, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(26)
        self.B.setFont(font)
        self.B.setObjectName("B")
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionopen.setStatusTip("choose")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setStatusTip("quit")
        self.actionexit.setObjectName("actionexit")
        self.menu.addAction(self.actionopen)
        self.menu.addAction(self.actionexit)
        self.menubar.addAction(self.menu.menuAction())


        self.actionexit.triggered.connect(MainWindow.close)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.R.setText(_translate("MainWindow", "R"))
        self.G.setText(_translate("MainWindow", "G"))
        self.B.setText(_translate("MainWindow", "B"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
    def show_dst(self,value):
        colormap = self.gen_map(value)
        h = cv.LUT(self.src, colormap[:])
        h = cv.cvtColor(h, cv.COLOR_BGR2RGB)
        x2 = h.shape[1]
        y2 = h.shape[0]
        frame2 = QtGui.QImage(h, x2,y2, 3*x2 ,QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(frame2)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(pix)
        # self.centralwidget.update()
        self.graphicsView2.setScene(self.scene)
        self.graphicsView2.viewport().repaint()

        src3=np.repeat(colormap,repeats=50,axis=0)
        # src3=np.repeat(src3,int(np.ones([1,256])*2),axis=1)
        x = src3.shape[1]
        y = src3.shape[0]
        frame = QtGui.QImage(src3, x, y, QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(frame)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(pix)
        self.graphicsView3.setScene(self.scene)
        self.graphicsView2.viewport().repaint()

    def gen_map(self,value=[0,0]):
        graylevel = int((self.grayscale + 1)/16)
        flag=value[0]
        color=value[1]
        if flag == 1:##r_mod
            print ('Colorscale is :',str(color))
            self.r[0,graylevel] =  int(color*22.5)
            pass
        elif flag == 2:##g_mod
            print('Colorscale is :',str(color))
            self.g[0,graylevel] =  int(color*25.5)
            pass
        elif flag == 3:##b_mod
            print('Colorscale is :',str(color))
            self.b[0,graylevel] =  int(color*25.5)
            pass
        elif flag == 0:##init_mod
            pass
        else:##gray_mod
            pass
        x = np.array(range(0, 256, 17))
        nx = np.array(range(0, 256, 1))
        nr = interp1d(x, self.r,kind='quadratic')(nx).reshape([1, 256])
        ng = interp1d(x, self.g,kind='quadratic')(nx).reshape([1, 256])
        nb = interp1d(x, self.b,kind='quadratic')(nx).reshape([1, 256])
        A = np.array([nr, ng, nb])
        A = np.swapaxes(A, 0, 1)
        A = np.swapaxes(A, 1, 2)
        A = A.astype('uint8')
        return A
    def enable_scroll(self):
        self.RR.setEnabled(1)
        self.GG.setEnabled(1)
        self.BB.setEnabled(1)
