import cv2
# import numpy as np

img = cv2.imread("knight.jpg")
img = cv2.bilateralFilter(img, 5, 250, 250)
cv2.imshow("Knight", img)

edges = cv2.Canny(img, 150, 300)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
