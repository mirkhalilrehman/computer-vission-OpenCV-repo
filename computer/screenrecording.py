import cv2 as cv
import pyautogui as p
import numpy as np

rs = p.size()

fn = input("Enter file path:\n")
fps = 20.0

fourcc = cv.VideoWriter_fourcc(*'XVID')
obj = cv.VideoWriter(fn, fourcc, fps, rs)

cv.namedWindow("Live Recording", cv.WINDOW_NORMAL)  # Create window outside the loop
cv.resizeWindow("Live Recording", (600, 400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = cv.cvtColor(f, cv.COLOR_BGR2RGB)
    obj.write(f)
    # cv.imshow("Live Recording", f)  # Update content in the existing window
    if cv.waitKey(1) == ord('q'):
        break

obj.release()
cv.destroyAllWindows()
