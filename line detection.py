import cv2
import numpy as np


def nothing():
    pass


vid = cv2.VideoCapture("road.mp4")

while True:

    _, frame = vid.read()
    frame = cv2.resize(frame, (640, 480))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([18, 94, 140], np.uint8)  # [18, 94, 140],[20, 100, 100]
    upper_yellow = np.array([48, 255, 255], np.uint8)  # [48, 255, 255],[30, 255, 255]

    sensitivity = 30
    lower_white = np.array([10, 10, 100], np.uint8)
    upper_white = np.array([25, 25, 250], np.uint8)

    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    white_mask = cv2.inRange(hsv, lower_white, upper_white)

    cv2.imshow("White Mask", white_mask)

    yellow_edges = cv2.Canny(yellow_mask, threshold1=75, threshold2=250)
    white_edges = cv2.Canny(white_mask, threshold1=75, threshold2=250)

    cv2.imshow("White Edges", white_edges)

    yellow_lines = cv2.HoughLinesP(yellow_edges, 1, np.pi / 180, 50, maxLineGap=50)
    white_lines = cv2.HoughLinesP(white_edges, 1, np.pi / 180, 50, maxLineGap=50)

    for line1 in yellow_lines:
        (x1, y1, x2, y2) = line1[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    for line2 in white_lines:
        (x1_2, y1_2, x2_2, y2_2) = line2[0]
        cv2.line(frame, (x1_2, y1_2), (x2_2, y2_2), (255, 0, 0), 5)

    cv2.imshow("IMG", frame)
    cv2.imshow("Yellow Mask", yellow_mask)
    cv2.imshow("Yellow Edges", yellow_edges)
    cv2.imshow("White Mask", white_mask)
    cv2.imshow("White Edges", white_edges)

    key = cv2.waitKey(1) & 0xff

    if key == ord('p'):

        while True:

            key2 = cv2.waitKey(1) or 0xff
            cv2.imshow('frame', frame)
            print("Beyaz pixellerdeki çizgilerin kordinatları\n", white_lines)
            print("Sarı pixellerdeki çizgilerin kordinatları\n", yellow_lines)

            if key2 == ord('p'):
                break

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
