import cv2
import numpy as np

img=cv2.imread("D:\\photos\\1.jpg")
print(img.dtype)
print(img.shape)
print(type(img))
print(img.size)
b,g,r=cv2.split(img)
cv2.imshow('res',img)
cv2.imshow('blue',b)
cv2.imshow('green',g)
cv2.imshow('red',r)
cv2.waitKey(0)
cv2.destroyAllWindows()
