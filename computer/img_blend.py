import cv2
img1=cv2.imread("D:\\photos\\IMG_3378.jpg")

img1=cv2.resize(img1,(600,800))
img2=cv2.imread("D:\\photos\\2.jpg")
img2=cv2.resize(img2,(600,800))
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
# result=img1+img2
# result=cv2.add(img1,img2) #blend
result=cv2.addWeighted(img1,0.5,img2,0.5,0) #blend
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()