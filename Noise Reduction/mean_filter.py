import cv2
import numpy as np


img = cv2.imread("Image\\hand.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Image",gray)

# Access image's value
# for row in range(10):
#     for col in range(10):
#         print(gray[row][col],end = " ")
#     print()

# Assign image's value
# for row in range(50):
#     for col in range(20):
#         gray[row][col] = 0
# gray[0:50,0:20] = 0
# cv2.imshow("Image",gray)
# cv2.waitKey()

def mean3(row,col,gray4filter):
    sum_v = 0
    for i in range(row-1,row+2):
        for j in range(col-1,col+2):
            sum_v += gray4filter[i][j]
    sum_v/=9
    return sum_v

# Implement mean filter
gray4filter = gray.copy()
rows = gray4filter.shape[0]
cols = gray4filter.shape[1]
gray_new = gray4filter.copy()

for row in range(1, rows-1):
    for col in range(1,cols-1):
        gray_new[row][col] = mean3(row,col,gray4filter)

cv2.imshow("After filter",gray_new)
cv2.waitKey()