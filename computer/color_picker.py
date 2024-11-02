import cv2
import numpy as np

def cross(x):
    pass

img=np.zeros((350,512,3),np.uint8)#black image
cv2.namedWindow("Color Picker")

s='0:OFF 1:ON'
cv2.createTrackbar(s,"Color Picker",0,1,cross)

cv2.createTrackbar("R","Color Picker",0,255,cross)
cv2.createTrackbar("G","Color Picker",0,255,cross)
cv2.createTrackbar("B","Color Picker",0,255,cross)

while True:
    cv2.imshow("Color Picker",img)
    if cv2.waitKey(1) & 0xFF==27:
        break

    s1=cv2.getTrackbarPos(s,"Color Picker")
    r=cv2.getTrackbarPos("R","Color Picker")
    g=cv2.getTrackbarPos("G","Color Picker")
    b=cv2.getTrackbarPos("B","Color Picker")
    
    if s1==0:
       img[ : ]=0
    else:
        cl = '{},{},{}'.format(r, g, b)
        img[:, :] = [b, g, r]  # Set the entire image to the selected color
        img = cv2.putText(img, cl, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)



cv2.destroyAllWindows()