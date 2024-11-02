import numpy as np
import cv2
img=cv2.imread("D:\\photos\\1.jpg")
img=cv2.resize(img,(800,800))

bgdr=cv2.copyMakeBorder(img,10,10,15,15,cv2.BORDER_CONSTANT,value=[255,0,255])


cv2.imshow('img',bgdr)
cv2.waitKey(0)
cv2.destroyAllWindows()