import cv2
import numpy as np


def nothing(x):
    pass


vid = cv2.VideoCapture("C:\\Users\\THERMALTAKE\\PycharmProjects\\pythonProject\\doggo.mp4")

cv2.namedWindow('frame')
cv2.createTrackbar('Sensivity', 'frame', 0, 255, nothing)

while True:

    _, frame = vid.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    sensitivity = cv2.getTrackbarPos('Sensivity', 'frame')
    lower_white = np.array([0, 0, 255 - sensitivity])
    upper_white = np.array([255, sensitivity, 255])
    mask = cv2.inRange(hsv, lower_white, upper_white)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Video", frame)
    cv2.imshow("HSV", hsv)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", res)

    key = cv2.waitKey(5) or 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
