import numpy as np
from scipy.interpolate import interp1d
import cv2 as cv
from PyQt5 import  QtGui

def gen_colormap(r=np.array(range(16)).reshape(1,16)*16,
                 g=-np.array(range(16)).reshape(1,16)*16+240,
                 b=np.array(range(16)).reshape(1,16)*16):
    x = np.array(range(0, 256, 17))
    nx = np.array(range(0, 256, 1))
    nr = interp1d(x, r)(nx).reshape([1, 256])
    ng = interp1d(x, g)(nx).reshape([1, 256])
    nb = interp1d(x, b)(nx).reshape([1, 256])
    A = np.array([nr, ng, nb])
    A = np.swapaxes(A, 0, 1)
    A = np.swapaxes(A, 1, 2)
    A = A.astype('uint8')
    return A

def load_image(self):
    src = cv.imread('zy3.bmp')
    # x = src.shape[1]
    # y = src.shape[0]
    # frame = QtGui.QImage(src, x, y, QtGui.QImage.Format_RGB888)
    # pix = QtGui.QPixmap.fromImage(frame)
    cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
    cv.imshow("input", src)
    colormap = gen_colormap()
    # dst = cv.LUT(src, colormap[:])
    # # cv.imshow("output", dst)
    # # cv.waitKey(0)