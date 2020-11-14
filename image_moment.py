import cv2
import numpy as np

shape = cv2.imread("image_moment_test.png")
gray = cv2.cvtColor(shape, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
A = cv2.contourArea(contours[0])
perimeter = cv2.arcLength(contours[0], True)
M = cv2.moments(threshold)

print("Şekilinizin alanı =", A)
print("Şekilinizin çevresi =", perimeter)

X = int(M["m10"]/M["m00"])
Y = int(M["m01"]/M["m00"])
cv2.circle(shape, (X, Y), 5, (255, 0, 0), -1)

x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(shape, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Shape", shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
