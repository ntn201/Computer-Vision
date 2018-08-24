import cv2
import numpy as np

img = cv2.imread("Image/DP7_EN_3.png")
cv2.imshow("Original",img)

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    cv2.imshow("Video",frame)
    key = cv2.waitKey(30)
    if key&0xFF == ord("s"):
        cv2.imwrite("image.jpg",frame)
    if key&0xFF == ord("q"):
        break

