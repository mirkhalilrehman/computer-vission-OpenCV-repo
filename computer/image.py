import cv2
#default 1 colourful
imgi=cv2.imread("D:\\photos\\1.jpg",1)#default 1 colourful
imgi=cv2.resize(imgi,(700,600))
cv2.imshow("original",imgi)
print(imgi)

#0 greyscale image
img=cv2.imread("D:\\photos\\1.jpg",0)#0 greyscale image
img=cv2.resize(img,(700,600))
cv2.imshow("grey scale",img)
print('grey scale=',img)

#-1 unchanged image
img1=cv2.imread("D:\\photos\\1.jpg",-1)#0 greyscale image
img1=cv2.resize(img1,(700,600))
cv2.imshow("unchanged",img1)
print('unchanged=',img1)

img=cv2.imread("D:\\photos\\1.jpg",0)#0 greyscale image
img=cv2.resize(img,(700,600))
img=cv2.flip(img,0)#0,1,-1
cv2.imshow("flipped",img)
print('flipped=',img)

cv2.waitKey()
cv2.destroyAllWindows()