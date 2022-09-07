import numpy as np
import cv2


# マウスイベント時に処理を行う
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        upper[0] = hsv[y, x, 0] + num
        lower[0] = hsv[y, x, 0] - num

        upper[1] = hsv[y, x, 1] + num
        lower[1] = hsv[y, x, 1] - num

        upper[2] = hsv[y, x, 2] + num
        lower[2] = hsv[y, x, 2] - num
        if upper[0] > 180:
            u1[0] = upper[0] - 180
            l1[0] = 0
        elif lower[0] < 0:
            u1[0] = 180
            l1[0] = 180 + lower[0]
        else:
            u1[0] = 0
            l1[0] = 0
        print("H = ", upper[0] - num)
        print("S = ", upper[1] - num)
        print("V = ", upper[2] - num)


# 色フィルター設定
upper = np.array([180, 255, 255])
lower = np.array([170, 80, 80])

u1 = np.array([10, 255, 255])
l1 = np.array([0, 100, 100])

num = 10

cap = cv2.VideoCapture(0)

# ウィンドウのサイズを変更可能にする
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
# マウスイベント時に関数mouse_eventの処理を行う
cv2.setMouseCallback("img", mouse_event)

while (True):
    ret, img = cap.read()

    img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)

    height, width = img.shape[:2]
    # HSVに変換する
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # マスク処理
    mask = cv2.inRange(hsv, lower, upper)
    mask1 = cv2.inRange(hsv, l1, u1)

    mask = mask + mask1

    cv2.imshow("img", img)
    cv2.imshow("mask", mask)

    if cv2.waitKey(1) == 13:
        break

cv2.destroyAllWindows()