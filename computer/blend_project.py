import cv2 as cv
import numpy as np

img1=cv.imread("D:\\photos\\IMG_3378.jpg")
img1=cv.resize(img1,(400,600))
img2=cv.imread("D:\\photos\\2.jpg")
img2=cv.resize(img2,(400,600))

def blend(x):
    pass

img=np.zeros((400,400,3),np.uint8)
cv.namedWindow('win')
cv.createTrackbar('alpha','win',0,100,blend)
switch="0:off \n 1:on"
cv.createTrackbar(switch,'win',0,1,blend)

while True:
    s=cv.getTrackbarPos(switch,'win')
    a=cv.getTrackbarPos('alpha','win')
    n=float(a/100)

    if s==0:
        dst=img[:]
    else:
        dst=cv.addWeighted(img1,1-n,img2,n,0)
        cv.putText(dst,str(a),(20,50),cv.FONT_ITALIC,2,(0,125,125),2)

    cv.imshow('dst',dst)


    if cv.waitKey(1)==27 & 0xFF:
        break
