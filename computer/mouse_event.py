import cv2
import numpy as np

def draw(event,x,y,flag,param):
    print("x",x,"y",y,'flag',flag,'param',param)
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(123,0,100),1)
    elif event==cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img,(x,y),(x+100,y+100),(14,2,234),3)
                      
cv2.namedWindow(winname='res')

img=np.zeros((512,512,3),np.uint8)
cv2.setMouseCallback("res",draw)

while True:
    cv2.imshow('res',img)
    if cv2.waitKey(1)& 0xFF==27:
        break
cv2.destroyAllWindows()
