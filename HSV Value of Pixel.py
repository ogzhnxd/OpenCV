import cv2
import numpy as np

points = []


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ",", y)
        points.append([x, y])
        font = cv2.FONT_HERSHEY_SIMPLEX
        str_xy = str(x) + ", " + str(y)
        cv2.putText(img, str_xy, (x, y), font, 0.5, (255, 255, 0), 2)
        cv2.imshow("image", img)

    if event == cv2.EVENT_RBUTTONDOWN:
        h = img[y, x, 0]
        s = img[y, x, 1]
        v = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        str_hsv = str(h) + ", " + str(s) + "," + str(v)
        cv2.putText(img, str_hsv, (x, y), font, 0.5, (0, 255, 255), 2)
        cv2.imshow("image", img)


img = cv2.imread("road.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("image", img)

cv2.setMouseCallback("image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
