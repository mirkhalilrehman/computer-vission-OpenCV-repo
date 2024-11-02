import cv2
import numpy as np

img=cv2.imread("D:\\computer\\ball.jpg")
img=cv2.resize(img,(400,400))
# cv2.imshow('img',img)
def nothing(x):
    pass

cv2.namedWindow('color adjustment')

cv2.createTrackbar('lower_H','color adjustment',0,255,nothing)
cv2.createTrackbar('lower_S','color adjustment',0,255,nothing)
cv2.createTrackbar('lower_V','color adjustment',0,255,nothing)

cv2.createTrackbar('upper_H','color adjustment',255,255,nothing)
cv2.createTrackbar('upper_S','color adjustment',255,255,nothing)
cv2.createTrackbar('upper_V','color adjustment',255,255,nothing)

while True:
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    l_h=cv2.getTrackbarPos('lower_H','color adjustment')
    l_s=cv2.getTrackbarPos('lower_S','color adjustment')
    l_v=cv2.getTrackbarPos('lower_V','color adjustment')

    u_h=cv2.getTrackbarPos('upper_H','color adjustment')
    u_s=cv2.getTrackbarPos('upper_S','color adjustment')
    u_v=cv2.getTrackbarPos('upper_V','color adjustment')
    u_v=np.array([u_h,u_s,u_v])
    l_v=np.array([l_h,l_s,l_v])

    mask=cv2.inRange(hsv,l_v,u_v)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('frame',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    if cv2.waitKey(1)==27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()