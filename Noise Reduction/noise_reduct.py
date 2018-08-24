import cv2
import numpy
from median_filter import median_filter3

img  = cv2.imread("Image/girl.png")
cv2.imshow("Image",img)

# cv2.imshow("Image",img)
img3 = img.copy()
img2 = img.copy()

def mean_filter3(row,col,gray4filter):
    sum_v = 0
    for i in range(row-1,row+2):
        for j in range(col-1,col+2):
            sum_v += gray4filter[i][j]
    sum_v/=9
    return sum_v

for k in range (3):
    img_filter = img[::,::,k]
    for i in range(1,img.shape[0]-1):
        for j in range (1,img.shape[1]-1):
            img[i][j][k] = median_filter3(i,j,img_filter)

for k in range (3):
    img_filter = img2[::,::,k]
    for i in range(1,img.shape[0]-1):
        for j in range (1,img.shape[1]-1):
            img2[i][j][k] = mean_filter3(i,j,img_filter)

img3 = cv2.GaussianBlur(img3,(3,3),0,0)


check = cv2.bitwise_xor(img2,img)
cv2.imshow("Gaussian",img3)
cv2.imshow("Mean",img2)
cv2.imshow("Median",img)
cv2.imshow("Check",check)

cv2.waitKey()