src = cv2.imread("D:\\1.jpg")
# img = src[1650:2400, 2150:3500]
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
x = img.shape[1]
y = img.shape[0]
frame = QtGui.QImage(img, x, y, QtGui.QImage.Format_1RGB888)
pix = QtGui.QPixmap.fromImage(frame)
self.scene = QGraphicsScene()
self.scene.addPixmap(pix)
self.graphicsView.setScene(self.scene)