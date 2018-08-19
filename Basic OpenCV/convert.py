import cv2
import numpy as np
import matplotlib as plt

# Read image
image = cv2.imread("C:\\Users\\Lenovo\\Pictures\\Untitled Export\\20171204181633_IMG_9922.jpg")
image = cv2.resize(image,(456,684))
cv2.imshow("image",image)
# cv2.waitKey()

# Get row and col
row = image.shape[0]
col = image.shape[1]
print (row,col)
print ("Channel:", len(image.shape))

# Convert RGB to gray
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow("gray",gray)
# cv2.waitKey()
print(gray.shape)

#Convert gray to binary
thresh, binImg = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
cv2.imshow("thresh",binImg)
cv2.waitKey()


#Resize image
# image_resize = cv2.resize(image,(1024,768))
# cv2.imshow("image",image_resize)
# cv2.waitKey()