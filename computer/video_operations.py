import cv2

# res=cv2.VideoCapture('D:\\computer\\video.mp4')

# while True:
#     ret,frame=res.read()
#     frame=cv2.resize(frame,(700,500))
#     grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#convert frame to grey 
#     cv2.imshow("frame",frame)
#     cv2.imshow("grey",grey)
#     k=cv2.waitKey(25)#playback speed
#     if k==ord('q') & 0xFF:
#         break 
# res.release()
# cv2.destroyAllWindows()

#capture video from webcam and save in memory

res=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter('next.mp4',fourcc,20.0,(500,450),1)#last parameter 0 for grey 1 or deafult for color
while res.isOpened():
    ret,frame=res.read()
    if ret==True:
        frame=cv2.resize(frame,(700,500))
        # grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#convert frame to grey 
        cv2.imshow("frame",frame)
        # cv2.imshow("grey",grey)
        output.write(frame)
        k=cv2.waitKey(25)#playback speed
        if k==ord('q') & 0xFF:
         break

output.release()
res.release()
cv2.destroyAllWindows()