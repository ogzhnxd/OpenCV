import cv2
import numpy as np

image = cv2.imread("C:\\Users\\THERMALTAKE\\PycharmProjects\\pythonProject\\red_mercedes.jpg",0)

cv2.imshow("mercedes_image.jpeg", image)

button = cv2.waitKey(0)

if button == 27:
    cv2.destroyAllWindows()

else:
    cv2.imwrite("C:\\Users\\THERMALTAKE\\PycharmProjects\\pythonProject\\grey_mercedes_image.jpeg", image)
