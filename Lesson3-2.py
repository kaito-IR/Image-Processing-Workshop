import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)
RedMin = np.array([0,140,0])
RedMax= np.array([5,210,255])
TimeList = []
while True:
    ret,frame = cap.read()
    StartTime = time.perf_counter()
    #frame = cv2.resize(frame,dsize=None,fx=0.5,fy=0.5)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, RedMin, RedMax)
    cnts, _ =cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#輪郭抽出
    cnts = max(cnts, key=lambda x: cv2.contourArea(x))#抽出された輪郭データの中から最も面積の大きいものを選択
    m = cv2.moments(cnts)#選択された輪郭データの重心データを取得
    if int(m["m00"]) > 0:#重心データが存在するなら
        cx = int(m["m10"]/m["m00"])
        cy = int(m["m01"]/m["m00"])
        cv2.circle(frame,(cx,cy),3,(255,255,255),-1)
    cv2.imshow("Camera",frame)
    cv2.imshow("mask",mask)
    EndTime = time.perf_counter()-StartTime
    print(EndTime)
    TimeList.append(EndTime)
    if cv2.waitKey(1) != -1:
        break
print("Average:"+str(np.average(TimeList)))