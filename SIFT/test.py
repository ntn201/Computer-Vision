import cv2
import numpy as np

img = cv2.imread("Image/image.jpg")
mask = np.ones_like(img,dtype = np.float32)

cv2.imshow("hihi",mask)

cv2.waitKey()