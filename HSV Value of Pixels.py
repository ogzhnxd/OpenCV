import cv2
from matplotlib import pyplot as plt

img = cv2.imread('road.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img = cv2.resize(img, (640, 480))

plt.imshow(img)
plt.show()

cv2.imshow('image', img)

print(img.shape)

points = []

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        pixel = img[x, y]
        print(pixel)
        strXY = str(x) + ", " + str(y)
        cv2.putText(img, strXY, (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (255,255,0), 2)


cv2.setMouseCallback('image', mouse_click)

cv2.waitKey(0)

cv2.destroyAllWindows()
