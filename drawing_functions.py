from typing import List

import numpy as np
import cv2 as cv
import random

def RNG():
    rand_nums: List[int] = []

    for i in range(20):
        rand_nums.append(random.randint(0, 512))
    return rand_nums

line_list = RNG()
rectangle_list = RNG()
circle_list = RNG()
ellipse_list = RNG()

img = np.zeros((512,512,3), np.uint8)

for j in range(5):

    cv.line(img,(line_list[j],line_list[j+1]),(line_list[j+2],line_list[j+3]),(255,0,0),2)

for j in range(5):

    cv.rectangle(img,(rectangle_list[j],rectangle_list[j+1]),(rectangle_list[j+2],rectangle_list[j+3]),(0,255,0),2)

for j in range(5):

    cv.circle(img,(rectangle_list[j],rectangle_list[j+1]),(rectangle_list[j+2]),(0,0,255),2)

for j in range(2):

    cv.ellipse(img,(ellipse_list[j],ellipse_list[j+1]),(ellipse_list[j+2],ellipse_list[j+3]),0,0,180,255,2)

cv.imshow("img",img)

cv.waitKey(0)

cv.destroyAllWindows()
