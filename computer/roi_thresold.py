import numpy
import cv2

img1=cv2.imread('D:\\computer\\hero1.jpg')
img2=cv2.imread('D:\\computer\\strom_breaker.jpg')

img1=cv2.resize(img1,(800,500))
img2=cv2.resize(img2,(500,500))

r,c,ch=img2.shape

roi=img1[0:r,0:c]

img2_gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

_,mask=cv2.threshold(img2_gray,50,255,cv2.THRESH_BINARY)
mask_inv=cv2.bitwise_not(mask)

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_bg=cv2.bitwise_and(img2,img2,mask=mask)
res=cv2.add(img1_bg,img2_bg)
final=img1
final[0:r,0:c]=res

cv2.imshow("final",final)

# cv2.imshow('img_bg',img1_bg)
# cv2.imshow('mask',mask)
# cv2.imshow('inmask',mask_inv)
# cv2.imshow('roi',roi)
# cv2.imshow('img1',img1)
# cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()