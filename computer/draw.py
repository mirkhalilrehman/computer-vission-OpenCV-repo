import cv2
import numpy as np


# img=cv2.imread("d:/computer/grey.png")
#line(image,starting,ending,color,size)
# img=np.zeros([512,512,3],np.uint8)*255#black image
img=np.ones([512,512,3],np.uint8)*255#white image

img=cv2.line(img,(120,0),(200,300),(144,2,234),3)

#arrowedline(image,starting,ending,color,size)
img=cv2.arrowedLine(img,(10,120),(200,500),(14,2,234),5)

img=cv2.rectangle(img,(200,60),(600,300),(14,2,234),3)#-3 for fill

img=cv2.circle(img,(400,80),45,(14,25,24),3)

img=cv2.putText(img,'Mir',(20,500),cv2.FONT_ITALIC,4,(144,2,234),2)

img=cv2.ellipse(img,(100,400),(300,200),0,0,180,155,4)
cv2.imshow("result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()