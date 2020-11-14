import cv2
import numpy as np


def nothing(x):
    pass


cv2.namedWindow("Trackbar")

cv2.createTrackbar("LH", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("LS", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("LV", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("UH", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("US", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("UV", "Trackbar", 0, 255, nothing)

cv2.setTrackbarPos("UH", "Trackbar", 180)
cv2.setTrackbarPos("US", "Trackbar", 255)
cv2.setTrackbarPos("UV", "Trackbar", 255)

while True:

    img = cv2.imread('vector_lion.jpg')
    bg = np.zeros((200, 800, 3), np.uint8)
    cv2.putText(bg, "To see the percentage of white pixels press 'e'", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
    cv2.putText(bg, "To exit from program press 'ESC'", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("LH", "Trackbar")
    ls = cv2.getTrackbarPos("LS", "Trackbar")
    lv = cv2.getTrackbarPos("LV", "Trackbar")
    uh = cv2.getTrackbarPos("UH", "Trackbar")
    us = cv2.getTrackbarPos("US", "Trackbar")
    uv = cv2.getTrackbarPos("UV", "Trackbar")

    lower_red = np.array([lh, ls, lv])
    upper_red = np.array([uh, us, uv])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    n_white_pix = np.sum(mask == 255)
    n_black_pix = np.sum(mask == 0)

    cv2.imshow("mask", mask)
    cv2.imshow("hsv", hsv)
    cv2.imshow("img", img)
    cv2.imshow("Note", bg)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == 101:

        print(img.shape)
        print("Number of white pixels:", n_white_pix)
        print("Number of black pixels:", n_black_pix)
        pixelCount = n_black_pix + n_white_pix
        print("In image that is shown percentage of white pixels is :",
              str(100 * (n_white_pix / pixelCount)))


cv2.destroyAllWindows()
