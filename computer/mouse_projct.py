import cv2
import numpy as np

def mouse_event(event,x,y,flag,param):
    print(event,x,y,flag,param)
    font=cv2.FONT_HERSHEY_PLAIN
    if event==cv2.EVENT_LBUTTONDOWN:
        print('.',x,',',y)
        cord='.'+str(x)+','+str(y)
        cv2.putText(img, cord, (x, y), font, 1, (152, 255, 130), 2)
        #cv2.imshow()
    if event==cv2.EVENT_RBUTTONDOWN:
        b=img[y,x,0]
        g=img[y,x,1]
        r=img[y,x,2]
        cord_bgr='.'+str(b)+','+str(g)+','+str(r)
        cv2.putText(img, cord_bgr, (x, y), font, 1, (152, 255, 130), 2)
        #cv2.imshow()

cv2.namedWindow('res')
# img=np.zeros((512,512,3),np.uint8)
img=cv2.imread("D:\\photos\\1.jpg")
cv2.setMouseCallback("res",mouse_event)
while True:
    cv2.imshow('res',img)
    if cv2.waitKey()&0xFF==27:
        break
cv2.destroyAllWindows()
        
