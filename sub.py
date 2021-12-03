# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication
from mainwindow import Ui_MainWindow

import sys


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)


class Child(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Child, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

    def OPEN(self):
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    ch = Child()
    main.show()
    main.pushButton.clicked.connect(ch.OPEN)
    sys.exit(app.exec_())
