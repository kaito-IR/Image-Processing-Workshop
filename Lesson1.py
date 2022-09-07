import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    #frame = cv2.resize(frame,dsize=None,fx=0.5,fy=0.5)
    cv2.imshow("Camera",frame)
    if cv2.waitKey(1) != -1:
        break