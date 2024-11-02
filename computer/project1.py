import cv2
path=input("Enter the path for Image:\n")
img=cv2.imread(path,0)#0 greyscale image
img=cv2.resize(img,(700,600))
cv2.imshow("greyed",img)
k=cv2.waitKey()
if k==ord('s'):
    cv2.imwrite('grey.png',img)
else:
    cv2.destroyAllWindows()


