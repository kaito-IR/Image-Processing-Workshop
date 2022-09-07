import cv2
import numpy as np
cap = cv2.VideoCapture(0)
RedMin = np.array([0,140,0])
RedMax= np.array([5,210,255])
while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,dsize=None,fx=0.5,fy=0.5)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, RedMin, RedMax)
    cv2.imshow("Camera",frame)
    cv2.imshow("mask",mask)
    if cv2.waitKey(1) != -1:
        break