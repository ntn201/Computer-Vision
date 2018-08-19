import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image
image = cv2.imread("C:\\Users\\Lenovo\\Pictures\\Untitled Export\\IMG_0152.jpg",-1)

#Resize image
image = cv2.resize(image,(1024,768))
cv2.imshow("image",image)
b,g,r = cv2.split(image)
img2 = cv2.merge([r,g,b])
plt.imshow(img2)
plt.show()


# Read image from webcam
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    cv2.imshow("video",frame)
    key = cv2.waitKey(30)
    if key & 0xFF == ord('q'):
        break