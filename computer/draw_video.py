import cv2
import datetime
video=cv2.VideoCapture("D:\\computer\\video.mp4")#0 to open webcam
print("width :",video.get(2))
print("height :",video.get(4))
while (video.isOpened()):
    ret,frame=video.read()
    frame=cv2.resize(frame,(500,500))
    text="Width: "+str(video.get(3))+" Height: "+str(video.get(4))
    time=str(datetime.datetime.now())
    time=time[:-7]
    font=cv2.FONT_HERSHEY_COMPLEX_SMALL
    frame=cv2.putText(frame,text,(10,20),font,1,(0,120,0),1,cv2.LINE_AA)
    frame=cv2.putText(frame,time,(10,50),font,1,(0,120,0),1,cv2.LINE_AA)
    frame=cv2.rectangle(frame,(200,100),(400,250),(14,2,234),3)
    if ret==True:
        cv2.imshow("Frame",frame)

        if cv2.waitKey(25)==ord('q') & 0xFF:
            break

video.release()
cv2.destroyAllWindows()