import numpy as np
import cv2

cap = cv2.VideoCapture('http://localhost:4747/mjpegfeed')
cascade = cv2.CascadeClassifier("chess_pieces.xml")

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    blur = cv2.blur(frame, (5, 5))
    blur_g = cv2.GaussianBlur(frame, (5, 5), cv2.BORDER_DEFAULT)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ROI = frame[60:220, 360:600]
    gray_ROI = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray_ROI, 150, 300)
    bg = np.zeros((gray_ROI.shape[0], gray_ROI.shape[1], 3), np.uint8)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        cv2.drawContours(bg, contours, i, (255, 0, 0), 2, 8)

    chess_pieces = cascade.detectMultiScale(gray, 1.3, 12)
    chess_pieces_win = cascade.detectMultiScale(bg, 1.3, 7)

    for x, y, w, h in chess_pieces:
        cv2.circle(frame, (int(x + (w / 2)), int(y + (h / 2))), w, (0, 255, 0), 2)

    for x, y, w, h in chess_pieces_win:
        cv2.circle(ROI, (int(x + (w / 2)), int(y + (h / 2))), w, (0, 255, 255), 2)

    cv2.rectangle(frame, (360, 60), (600, 220), (255, 255, 0), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    cv2.imshow('blur', blur)
    cv2.imshow('gaussian blur', blur_g)
    cv2.imshow('win', ROI)
    cv2.imshow('win', bg)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
