import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()

    #frame = np.full((100,80,3), 12, np.uint8)
    frame = cv2.medianBlur(frame,3)

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,170,0])
    upper_red = np.array([30,255,255])

    mask = cv2.inRange(hsv,lower_red,upper_red)

    res = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow("Camera",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",res)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break