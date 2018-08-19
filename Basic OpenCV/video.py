import numpy
import cv2

# Read image from webcam
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
while True:
    ret,frame = cap.read()
    # Convert image to hsv
    #hsvImg = cv2.cvtCOLOR(fram,cv2.COLOR_RGB2HSV)
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    thresh, _bin = cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
    # cv2.imshow("binary",_bin)
    faces = cascade.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
        cv2.rectangle(_bin,(x,y),(x+w,y+h),(255,0,0),1)
    cv2.imshow("video",frame)
    #_bin = cv2.bitwise_not(_bin)
    cv2.imshow("thresh",_bin)
    key = cv2.waitKey(30)
    if key&0xFF == ord('q'):
        break