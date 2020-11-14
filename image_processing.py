import cv2
import numpy as np
from matplotlib import pyplot as plt

"""img = cv2.imread("background.jpg")
plt.imshow(img)
plt.show()"""

img1 = cv2.imread('background.jpg')
img2 = cv2.imread('subject.jpg')

print(img1.shape)
print(img2.shape)

img3 = img1[0:183,0:275]

print(img3.shape)

cv2.imshow("img3",img3)
cv2.imshow("img2",img2)

dst = cv2.addWeighted(img2,0.8,img3,0.2,0)
cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()