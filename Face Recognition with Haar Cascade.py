import cv2
import numpy as np

img = cv2.imread("faces.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier("frontalface.xml")
faces = face_cascade.detectMultiScale(gray, 1.3, 7)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
