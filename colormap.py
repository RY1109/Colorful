# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 14:45:34 2021

@author: a
"""

import numpy as np
from scipy.interpolate import interp1d
def gen_colormap(r=np.array(range(16)).reshape(1,16)*16,
                 g=-np.array(range(16)).reshape(1,16)*16+240,
                 b=np.array(range(16)).reshape(1,16)*16):
    x = np.array(range(0, 256,17))
    nx = np.array(range(0,256,1))
    nr = interp1d(x,r)(nx).reshape([1,256])
    ng = interp1d(x, g)(nx).reshape([1,256])
    nb = interp1d(x, b)(nx).reshape([1,256])
    A = np.array([nr, ng, nb])
    A = np.swapaxes(A, 0, 1)
    A = np.swapaxes(A, 1, 2)
    A = A.astype('uint8')
    return A

import cv2 as cv

src = cv.imread('zy3.bmp')
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
colormap = gen_colormap()
dst = cv.LUT(src,colormap[:])
cv.imshow("output", dst)
cv.waitKey(0)

# 伪色彩
# image = cv.imread("作业3.jpg")
# color_image = cv.applyColorMap(image, cv.COLORMAP_JET)
# cv.imshow("image", image)
# cv.imshow("color_image", color_image)
# cv.waitKey(0)
# cv.destroyAllWindows()