import cv2 as cv

vid = cv.VideoCapture("D:\\computer\\video.mp4")
ret, image = vid.read()
count = 0

while ret:
    cv.imwrite("D:\\computer\\frame\\img%d.jpg" % count, image)
    vid.set(cv.CAP_PROP_POS_MSEC, count * 1000)  # Set frame position in milliseconds
   
    ret, image = vid.read()
    cv.imshow('image', image)
    count += 1
    if cv.waitKey(1) == ord('q'):
        break

vid.release()
cv.destroyAllWindows()
