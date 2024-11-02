import cv2
import numpy as np

img=cv2.imread('D:\\computer\\grey.png',0)
img=cv2.resize(img,(300,300))
cv2.imshow('img',img)
th1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
_,th5=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('th5',th5)

cv2.waitKey(0)
cv2.destroyAllWindows()