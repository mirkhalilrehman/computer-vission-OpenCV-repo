import numpy as np
import cv2
img=cv2.imread("D:\\photos\\1.jpg")
img=cv2.resize(img,(800,800))

#(160,0),(331,180)
roi=img[0:250,222:432]
#y=250,x=210
img[0:250,431:641]=roi
img[0:250,0:210]=roi


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()