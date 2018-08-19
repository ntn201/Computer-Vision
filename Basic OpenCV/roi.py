import cv2
import numpy

img = cv2.imread("moon.JPG")
img = cv2.resize(img,(648,432))
img[:,:,2] = 100
cv2.imshow("img",img)
cv2.waitKey()