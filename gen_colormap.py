import numpy as np
from scipy.interpolate import interp1d
import cv2 as cv

def gen_colormap(r=np.random.random([1,16]),g=np.random.random([1,16]),b=np.random.random([1,16])):
    x = np.array(range(0, 256,17))
    nx = np.array(range(0,256,1))
    nr = interp1d(x,r)(nx).reshape([1,256])
    ng = interp1d(x, g)(nx).reshape([1,256])
    nb = interp1d(x, b)(nx).reshape([1,256])
    A = np.array([nb, ng, nr])
    A = np.swapaxes(A, 0, 1)
    A = np.swapaxes(A, 1, 2)
    A = A*255
    A = A.astype('uint8')
    return A
if __name__ == '__main__':
    A = gen_colormap()


