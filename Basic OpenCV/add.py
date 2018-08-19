import cv2
import numpy
import matplotlib.pyplot as plt

img1 = cv2.imread("moon.JPG")
img1 = cv2.resize(img1,(648,432))
img2 = cv2.imread("lamp.jpg")
img2 = cv2.resize(img2,(648,432))

ret = cv2.addWeighted(img1,0.5,img2,0.5,0)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("img",ret)
cv2.waitKey()