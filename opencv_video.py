import cv2
import numpy as np

vid = cv2.VideoCapture("C:\\Users\\THERMALTAKE\\PycharmProjects\\pythonProject\\video_example.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
processed_video = cv2.VideoWriter('processed_video.avi', fourcc, 60.0, (1280, 720))

while True:

    boolean, frame = vid.read()
    if boolean == 1:
        processed_video.write(frame)
    cv2.imshow("video_example.mp4", frame)

    if cv2.waitKey(10) or 0xFF == ord("q"):
        break

vid.release()

cv2.destroyAllWindows()
