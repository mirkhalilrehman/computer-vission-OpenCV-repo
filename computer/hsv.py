import numpy as np
import cv2

frame=cv2.imread("D:\\computer\\ball.jpg")


while True:
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    u_v=np.array([130,235,225])
    l_v=np.array([110,50,50])

    mask=cv2.inRange(hsv,l_v,u_v)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()